"""Split into a pure, session-injected function plus a thin Celery-task
wrapper -- same separation ``rate_limit.py`` uses between check-logic and
FastAPI plumbing. The pure function is what tests call directly (no real
Celery/Redis needed in CI); the task wrapper is what Celery Beat actually
invokes in a worker process, which has no HTTP request to hang a
``Depends()`` off, hence ``SessionLocal()`` instead of the DI-based
``get_session``.
"""

import structlog
from backend.app.core.celery_app import celery_app
from backend.app.database import SessionLocal
from backend.app.modules.compliance.repository import (
    SqlAlchemyAssessmentRepository,
    SqlAlchemyComplianceScoreRepository,
    SqlAlchemyFrameworkRepository,
)
from backend.app.modules.compliance.service import (
    AssessmentService,
    AssessmentStatus,
    ComplianceScoringService,
)
from backend.app.modules.organizations.repository import SqlAlchemyOrganizationRepository
from backend.app.modules.organizations.service import OrganizationService
from sqlalchemy.orm import Session

logger = structlog.get_logger(__name__)


def _recompute_all_compliance_scores(session: Session) -> int:
    # IN_PROGRESS only: AssessmentStatus's state machine has an explicit
    # "reopen" (COMPLETED -> IN_PROGRESS) transition, signaling COMPLETED is
    # meant to be a locked/final state. Recomputing on a schedule would
    # silently rewrite a "final" score behind that workflow's back.
    organizations = OrganizationService(SqlAlchemyOrganizationRepository(session)).list_organizations()
    assessments_service = AssessmentService(
        SqlAlchemyAssessmentRepository(session), SqlAlchemyFrameworkRepository(session)
    )
    scoring_service = ComplianceScoringService(
        assessments_service, SqlAlchemyComplianceScoreRepository(session)
    )
    recomputed = 0
    for organization in organizations:
        for assessment in assessments_service.list_assessments(organization.id):
            if assessment.status != AssessmentStatus.IN_PROGRESS:
                continue
            scoring_service.compute_and_store(assessment)
            recomputed += 1
    return recomputed


@celery_app.task(name="backend.app.core.tasks.recompute_all_compliance_scores")
def recompute_all_compliance_scores() -> int:
    with SessionLocal() as session:
        count = _recompute_all_compliance_scores(session)
        logger.info("compliance_scores_recomputed", count=count)
        return count
