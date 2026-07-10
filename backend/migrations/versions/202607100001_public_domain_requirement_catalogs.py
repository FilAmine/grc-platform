"""load real requirement text for NIST CSF, HIPAA, NIS2, DORA

Revision ID: 202607100001
Revises: 202607090007
Create Date: 2026-07-10 00:01:00

Adds real requirement rows for the NIST CSF 2.0, HIPAA Security Rule, NIS2,
and DORA framework versions seeded by 202607090002. Deliberately excludes
ISO 27001/27002/27005, CIS Controls, SOC 2, and PCI DSS: those are
commercially licensed standards whose official requirement text this project
has no rights to reproduce, so they remain catalog-only (name/code/version,
no requirement rows) by design -- see docs/database.md and docs/roadmap.md.

NIST CSF 2.0 and the HIPAA Security Rule (45 CFR Part 164) are US federal
government works and are in the public domain (17 U.S.C. Sec. 105). NIS2 and
DORA are EU legislation; the rows below paraphrase the legal obligations in
original wording rather than quoting the directive/regulation text, and cite
article/chapter numbers rather than full legal citations.

Unlike prior seed migrations, this one looks up each framework's
already-seeded (and therefore not statically known) framework_version_id via
a runtime SELECT, so it has no meaningful `--sql` offline preview -- offline
mode has no real rows to select, so upgrade()/downgrade() are no-ops there
(this only affects `alembic upgrade head --sql`; a real `alembic upgrade
head` against a live database, including the CI Postgres service container,
runs normally).
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607100001"
down_revision: str | None = "202607090007"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

REQUIREMENTS_BY_FRAMEWORK: dict[str, list[tuple[str, str, str]]] = {
    "nist-csf": [
        ("GV.OC", "Organizational Context", "The organization's mission, stakeholder expectations, legal and regulatory requirements, and cybersecurity risk tolerance are understood and inform cybersecurity risk management decisions."),
        ("GV.RM", "Risk Management Strategy", "The organization's priorities, constraints, risk tolerance and appetite statements, and assumptions are established, communicated, and used to support operational risk decisions."),
        ("GV.RR", "Roles, Responsibilities, and Authorities", "Cybersecurity roles, responsibilities, and authorities are established, communicated, and understood to foster accountability, performance assessment, and continuous improvement."),
        ("GV.PO", "Policy", "Organizational cybersecurity policy is established, communicated, and enforced."),
        ("GV.SC", "Cybersecurity Supply Chain Risk Management", "Cyber supply chain risk management processes are identified, established, managed, monitored, and improved by organizational stakeholders."),
        ("ID.AM", "Asset Management", "Assets that enable the organization to achieve business purposes are identified and managed consistent with their relative importance to organizational objectives and the risk strategy."),
        ("ID.RA", "Risk Assessment", "The cybersecurity risk to the organization, assets, and individuals is understood by the organization."),
        ("PR.AA", "Identity Management, Authentication, and Access Control", "Access to physical and logical assets is limited to authorized users, services, and hardware, and is managed commensurate with the assessed risk of unauthorized access."),
        ("PR.DS", "Data Security", "Data is managed consistent with the organization's risk strategy to protect the confidentiality, integrity, and availability of information."),
        ("DE.CM", "Continuous Monitoring", "Assets are monitored to find anomalies, indicators of compromise, and other potentially adverse events."),
        ("DE.AE", "Adverse Event Analysis", "Anomalies, indicators of compromise, and other potentially adverse events are analyzed to characterize the events and detect cybersecurity incidents."),
        ("RS.MA", "Incident Management", "Responses to detected cybersecurity incidents are managed."),
        ("RS.CO", "Incident Response Reporting and Communication", "Response activities are coordinated with internal and external stakeholders as required by laws, regulations, or policies."),
        ("RC.RP", "Incident Recovery Plan Execution", "Restoration activities are performed to ensure operational availability of systems and services affected by cybersecurity incidents."),
    ],
    "hipaa": [
        ("164.308(a)(1)", "Security Management Process", "Implement policies and procedures to prevent, detect, contain, and correct security violations, including a risk analysis and risk management program."),
        ("164.308(a)(2)", "Assigned Security Responsibility", "Identify the security official responsible for developing and implementing the entity's security policies and procedures."),
        ("164.308(a)(3)", "Workforce Security", "Implement policies and procedures to ensure workforce members have appropriate access to electronic protected health information and to prevent unauthorized access."),
        ("164.308(a)(4)", "Information Access Management", "Implement policies and procedures for authorizing access to electronic protected health information consistent with the applicable requirements."),
        ("164.308(a)(5)", "Security Awareness and Training", "Implement a security awareness and training program for all workforce members, including management."),
        ("164.308(a)(6)", "Security Incident Procedures", "Implement policies and procedures to address security incidents, including identification, response, and documentation."),
        ("164.308(a)(7)", "Contingency Plan", "Establish policies and procedures for responding to an emergency or other occurrence that damages systems containing electronic protected health information, including data backup, disaster recovery, and emergency mode operation plans."),
        ("164.310(a)", "Facility Access Controls", "Implement policies and procedures to limit physical access to electronic information systems and the facilities housing them, while ensuring properly authorized access is allowed."),
        ("164.310(d)", "Device and Media Controls", "Implement policies and procedures governing the receipt, removal, and movement of hardware and electronic media containing electronic protected health information."),
        ("164.312(a)", "Access Control", "Implement technical policies and procedures for electronic information systems that maintain electronic protected health information to allow access only to authorized persons or software programs."),
        ("164.312(b)", "Audit Controls", "Implement hardware, software, and procedural mechanisms that record and examine activity in information systems containing or using electronic protected health information."),
        ("164.312(c)", "Integrity", "Implement policies and procedures to protect electronic protected health information from improper alteration or destruction."),
        ("164.312(e)", "Transmission Security", "Implement technical security measures to guard against unauthorized access to electronic protected health information transmitted over an electronic communications network."),
    ],
    "nis2": [
        ("Art.21.2.a", "Risk Analysis and Information System Security Policies", "Adopt policies on risk analysis and information system security as part of the entity's cybersecurity risk-management measures."),
        ("Art.21.2.b", "Incident Handling", "Establish incident handling processes to prevent, detect, and respond to security incidents affecting network and information systems."),
        ("Art.21.2.c", "Business Continuity and Crisis Management", "Maintain business continuity measures, such as backup management and disaster recovery, and crisis management arrangements."),
        ("Art.21.2.d", "Supply Chain Security", "Address the security of the supply chain, including security-related aspects of relationships between the entity and its direct suppliers or service providers."),
        ("Art.21.2.g", "Cyber Hygiene Practices and Training", "Implement basic cyber hygiene practices and cybersecurity training for personnel."),
        ("Art.21.2.j", "Access Control and Multi-Factor Authentication", "Use multi-factor authentication or continuous authentication solutions, secured voice/video/text communications, and secured emergency communication systems where appropriate."),
    ],
    "dora": [
        ("Ch.II", "ICT Risk Management", "Establish and maintain a sound, comprehensive, and well-documented ICT risk management framework as part of the entity's overall risk management system."),
        ("Ch.III", "ICT-Related Incident Reporting", "Establish and implement an ICT-related incident management process to detect, manage, and notify major ICT-related incidents."),
        ("Ch.IV", "Digital Operational Resilience Testing", "Establish, maintain, and review a sound and comprehensive digital operational resilience testing programme as part of the ICT risk management framework."),
        ("Ch.V", "ICT Third-Party Risk Management", "Manage ICT third-party risk as an integral component of ICT risk, including monitoring of risk arising from third-party ICT providers."),
        ("Ch.VI", "Information Sharing Arrangements", "Enter into arrangements to exchange cyber threat information and intelligence among financial entities to enhance digital operational resilience."),
    ],
}


def _framework_version_table() -> sa.Table:
    return sa.table(
        "framework_versions",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("framework_id", postgresql.UUID(as_uuid=True)),
    )


def _frameworks_table() -> sa.Table:
    return sa.table(
        "frameworks",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("code", sa.String),
    )


def _requirements_table() -> sa.Table:
    return sa.table(
        "requirements",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("framework_version_id", postgresql.UUID(as_uuid=True)),
        sa.column("code", sa.String),
        sa.column("title", sa.String),
        sa.column("description", sa.Text),
        sa.column("created_at", sa.DateTime(timezone=True)),
        sa.column("updated_at", sa.DateTime(timezone=True)),
    )


def _version_id_by_framework_code(bind: sa.engine.Connection) -> dict[str, object]:
    frameworks = _frameworks_table()
    versions = _framework_version_table()
    rows = bind.execute(
        sa.select(versions.c.id, frameworks.c.code)
        .select_from(versions.join(frameworks, versions.c.framework_id == frameworks.c.id))
        .where(frameworks.c.code.in_(REQUIREMENTS_BY_FRAMEWORK.keys()))
    ).all()
    return {code: version_id for version_id, code in rows}


def upgrade() -> None:
    if context.is_offline_mode():
        return
    bind = op.get_bind()
    version_id_by_code = _version_id_by_framework_code(bind)
    now = datetime.now(UTC)

    requirement_rows = [
        {
            "id": uuid4(),
            "framework_version_id": version_id_by_code[framework_code],
            "code": code,
            "title": title,
            "description": description,
            "created_at": now,
            "updated_at": now,
        }
        for framework_code, requirements in REQUIREMENTS_BY_FRAMEWORK.items()
        for code, title, description in requirements
    ]
    op.bulk_insert(_requirements_table(), requirement_rows)


def downgrade() -> None:
    if context.is_offline_mode():
        return
    bind = op.get_bind()
    version_id_by_code = _version_id_by_framework_code(bind)
    requirements = _requirements_table()

    for framework_code, requirement_rows in REQUIREMENTS_BY_FRAMEWORK.items():
        version_id = version_id_by_code[framework_code]
        codes = [code for code, _, _ in requirement_rows]
        op.execute(
            requirements.delete().where(
                sa.and_(
                    requirements.c.framework_version_id == version_id,
                    requirements.c.code.in_(codes),
                )
            )
        )
