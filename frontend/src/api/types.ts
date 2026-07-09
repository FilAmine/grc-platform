export type Organization = {
  id: string;
  name: string;
  slug: string;
  created_at: string;
  updated_at: string;
};

export type RiskSeverity = 'low' | 'medium' | 'high' | 'critical';
export type RiskStatus = 'open' | 'mitigating' | 'accepted' | 'closed';

export type Risk = {
  id: string;
  organization_id: string;
  title: string;
  description: string;
  severity: RiskSeverity;
  status: RiskStatus;
  owner: string;
  created_at: string;
  updated_at: string;
};

export type RiskCreate = {
  title: string;
  description: string;
  severity: RiskSeverity;
  owner: string;
};

export type ControlStatus = 'draft' | 'active' | 'retired';

export type Control = {
  id: string;
  organization_id: string;
  name: string;
  description: string;
  framework: string;
  status: ControlStatus;
  created_at: string;
  updated_at: string;
};

export type ControlCreate = {
  name: string;
  description: string;
  framework: string;
};

export type ComplianceSummary = {
  organizations: number;
  risks_open: number;
  controls_active: number;
  posture: 'healthy' | 'attention_required';
};

export type User = {
  id: string;
  organization_id: string;
  email: string;
  full_name: string;
  is_active: boolean;
  is_superuser: boolean;
  created_at: string;
  updated_at: string;
};

export type TokenResponse = {
  access_token: string;
  refresh_token: string;
  token_type: string;
};

export type RegisterOrganizationRequest = {
  organization_name: string;
  organization_slug: string;
  admin_email: string;
  admin_full_name: string;
  admin_password: string;
};

export type Notification = {
  id: string;
  organization_id: string;
  recipient_id: string;
  subject: string;
  body: string;
  read_at: string | null;
  created_at: string;
};

// --- Audits -----------------------------------------------------------------

export type AuditStatus = 'planned' | 'in_progress' | 'completed' | 'closed';
export type ChecklistItemStatus = 'pending' | 'done' | 'not_applicable';
export type FindingSeverity = 'minor' | 'major' | 'critical';
export type FindingStatus = 'open' | 'in_remediation' | 'closed';
export type CorrectiveActionStatus = 'open' | 'in_progress' | 'done';

export type Audit = {
  id: string;
  organization_id: string;
  title: string;
  scope: string;
  lead_auditor: string;
  status: AuditStatus;
  period_start: string | null;
  period_end: string | null;
  created_at: string;
  updated_at: string;
};

export type AuditCreate = {
  title: string;
  scope: string;
  lead_auditor: string;
  period_start?: string | null;
  period_end?: string | null;
};

export type ChecklistItem = {
  id: string;
  audit_id: string;
  description: string;
  status: ChecklistItemStatus;
  notes: string;
  created_at: string;
  updated_at: string;
};

export type Finding = {
  id: string;
  audit_id: string;
  checklist_item_id: string | null;
  title: string;
  description: string;
  severity: FindingSeverity;
  status: FindingStatus;
  created_at: string;
  updated_at: string;
};

export type CorrectiveAction = {
  id: string;
  finding_id: string;
  description: string;
  owner: string;
  due_date: string | null;
  status: CorrectiveActionStatus;
  completed_at: string | null;
  created_at: string;
  updated_at: string;
};

export type AuditReport = {
  audit: Audit;
  checklist_total: number;
  checklist_done: number;
  findings_by_severity: Record<string, number>;
  open_findings: number;
  corrective_actions_total: number;
  corrective_actions_done: number;
};

// --- Documents ----------------------------------------------------------------

export type DocumentType = 'policy' | 'procedure' | 'standard' | 'guideline' | 'template';
export type DocumentStatus = 'draft' | 'in_review' | 'published' | 'archived';
export type VersionStatus = 'draft' | 'pending_approval' | 'approved' | 'rejected';

export type GrcDocument = {
  id: string;
  organization_id: string;
  title: string;
  document_type: DocumentType;
  status: DocumentStatus;
  owner: string;
  published_version_id: string | null;
  created_at: string;
  updated_at: string;
};

export type DocumentCreate = {
  title: string;
  document_type: DocumentType;
  owner: string;
  file_reference: string;
};

export type DocumentVersion = {
  id: string;
  document_id: string;
  version_number: number;
  file_reference: string;
  change_summary: string;
  status: VersionStatus;
  created_by_id: string | null;
  created_at: string;
  updated_at: string;
};

export type VersionCreate = {
  file_reference: string;
  change_summary: string;
};

export type ApprovalDecision = {
  approve: boolean;
  comment: string;
  signature_reference?: string | null;
};

export type Approval = {
  id: string;
  document_version_id: string;
  approver_id: string;
  decision: VersionStatus;
  comment: string;
  signature_reference: string | null;
  decided_at: string | null;
  created_at: string;
};
