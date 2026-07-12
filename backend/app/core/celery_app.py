"""Celery has been a declared dependency since day one but never actually
wired up -- this is that wiring. Broker and result backend both reuse the
Redis connection already configured for rate limiting
(``backend/app/core/config.py``'s ``settings.redis_url``); no new
infrastructure dependency.

Only one real task exists so far (``backend/app/core/tasks.py``'s
``recompute_all_compliance_scores``, run nightly via the beat schedule
below). Other candidate uses (async document/evidence file processing,
scheduled notification digests) stay undone until there's a real pipeline
to hang them off -- see docs/roadmap.md.
"""

from backend.app.core.config import settings
from celery import Celery
from celery.schedules import crontab

celery_app = Celery("grc_platform", broker=settings.redis_url, backend=settings.redis_url)
celery_app.conf.timezone = "UTC"
celery_app.conf.beat_schedule = {
    "recompute-all-compliance-scores-nightly": {
        "task": "backend.app.core.tasks.recompute_all_compliance_scores",
        "schedule": crontab(hour=2, minute=0),
    },
}
