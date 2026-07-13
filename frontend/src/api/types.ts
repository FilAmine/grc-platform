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
  // EBIOS-RM-flavored structural links -- settable at creation only, see
  // docs/roadmap.md for the stated boundary (no Risk detail page/update yet).
  asset_id: string | null;
  threat_id: string | null;
  vulnerability_id: string | null;
  feared_event_id: string | null;
};

export type RiskCreate = {
  title: string;
  description: string;
  severity: RiskSeverity;
  owner: string;
  asset_id?: string | null;
  threat_id?: string | null;
  vulnerability_id?: string | null;
  feared_event_id?: string | null;
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
  role_ids: string[];
  created_at: string;
  updated_at: string;
};

export type UserCreate = {
  email: string;
  full_name: string;
  password: string;
  is_superuser?: boolean;
};

export type UserUpdate = {
  full_name?: string;
  is_active?: boolean;
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

// --- Notifications -----------------------------------------------------------

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

// --- Assets / CMDB -------------------------------------------------------------

export type AssetType = 'hardware' | 'software' | 'cloud_service' | 'application' | 'business_asset' | 'service';
export type AssetLifecycleStage = 'planned' | 'in_use' | 'maintenance' | 'retired' | 'disposed';
export type ClassificationLevel = 'low' | 'medium' | 'high';

export type Asset = {
  id: string;
  organization_id: string;
  name: string;
  asset_type: AssetType;
  description: string;
  owner: string;
  supplier: string;
  lifecycle_stage: AssetLifecycleStage;
  confidentiality: ClassificationLevel;
  integrity: ClassificationLevel;
  availability: ClassificationLevel;
  created_at: string;
  updated_at: string;
};

export type AssetCreate = {
  name: string;
  asset_type: AssetType;
  owner: string;
  description?: string;
  supplier?: string;
  confidentiality?: ClassificationLevel;
  integrity?: ClassificationLevel;
  availability?: ClassificationLevel;
};

// --- Compliance (frameworks, assessments, evidence) -----------------------------

export type AssessmentStatus = 'draft' | 'in_progress' | 'completed' | 'archived';
export type RequirementResultStatus =
  | 'not_assessed'
  | 'compliant'
  | 'partially_compliant'
  | 'non_compliant'
  | 'not_applicable';

export type Framework = {
  id: string;
  organization_id: string | null;
  code: string;
  name: string;
  description: string;
  is_system: boolean;
  created_at: string;
  updated_at: string;
};

export type FrameworkVersion = {
  id: string;
  framework_id: string;
  version: string;
  published_at: string | null;
  created_at: string;
  updated_at: string;
};

export type Requirement = {
  id: string;
  framework_version_id: string;
  category_id: string | null;
  code: string;
  title: string;
  description: string;
  created_at: string;
  updated_at: string;
};

export type Assessment = {
  id: string;
  organization_id: string;
  framework_version_id: string;
  name: string;
  status: AssessmentStatus;
  period_start: string | null;
  period_end: string | null;
  created_at: string;
  updated_at: string;
};

export type AssessmentCreate = {
  framework_version_id: string;
  name: string;
  period_start?: string | null;
  period_end?: string | null;
};

export type AssessmentResult = {
  id: string;
  assessment_id: string;
  requirement_id: string;
  status: RequirementResultStatus;
  notes: string;
  created_at: string;
  updated_at: string;
};

export type AssessmentResultUpdate = {
  status: RequirementResultStatus;
  notes?: string;
};

export type Evidence = {
  id: string;
  organization_id: string;
  assessment_result_id: string | null;
  control_id: string | null;
  title: string;
  description: string;
  file_reference: string;
  uploaded_by_id: string | null;
  created_at: string;
  updated_at: string;
};

export type EvidenceCreate = {
  title: string;
  description?: string;
  file_reference: string;
  assessment_result_id?: string | null;
  control_id?: string | null;
};

export type ComplianceScore = {
  id: string;
  organization_id: string;
  assessment_id: string;
  framework_version_id: string;
  score: number;
  computed_at: string;
};

// --- RBAC (roles, permissions) ---------------------------------------------------

export type Role = {
  id: string;
  organization_id: string | null;
  name: string;
  description: string;
  is_system: boolean;
  permission_codes: string[];
  created_at: string;
  updated_at: string;
};

export type RoleCreate = {
  name: string;
  description?: string;
  permission_codes?: string[];
};

export type RolePermissionsUpdate = {
  permission_codes: string[];
};

export type Permission = {
  id: string;
  code: string;
  description: string;
  created_at: string;
  updated_at: string;
};

// --- AI (chat, prompt library, knowledge base) -----------------------------------

export type ChatMessageRole = 'user' | 'assistant';

export type ChatSession = {
  id: string;
  organization_id: string;
  user_id: string;
  title: string;
  created_at: string;
  updated_at: string;
};

export type ChatSessionCreate = {
  title?: string;
};

export type ChatMessage = {
  id: string;
  session_id: string;
  role: ChatMessageRole;
  content: string;
  created_at: string;
};

export type ChatMessageCreate = {
  content: string;
};

export type PromptTemplate = {
  id: string;
  organization_id: string | null;
  name: string;
  template_text: string;
  description: string;
  created_at: string;
  updated_at: string;
};

export type PromptTemplateCreate = {
  name: string;
  template_text: string;
  description?: string;
};

export type KnowledgeBaseDocumentCreate = {
  title: string;
  content: string;
};

// --- SSO (per-organization OIDC connection) --------------------------------------

export type SsoConnection = {
  id: string;
  organization_id: string;
  issuer: string;
  client_id: string;
  default_role_id: string | null;
  is_enabled: boolean;
  created_at: string;
  updated_at: string;
};

export type SsoConnectionUpdate = {
  issuer: string;
  client_id: string;
  client_secret: string;
  default_role_id?: string | null;
  is_enabled: boolean;
};

// --- Departments -----------------------------------------------------------

export type Department = {
  id: string;
  organization_id: string;
  name: string;
  description: string;
  parent_department_id: string | null;
  created_at: string;
  updated_at: string;
};

export type DepartmentCreate = {
  name: string;
  description?: string;
  parent_department_id?: string | null;
};

// --- Threats -----------------------------------------------------------------

export type ThreatCategory = 'human' | 'technical' | 'environmental' | 'organizational';
export type ThreatLikelihood = 'low' | 'medium' | 'high';

export type Threat = {
  id: string;
  organization_id: string;
  name: string;
  description: string;
  category: ThreatCategory;
  likelihood: ThreatLikelihood;
  created_at: string;
  updated_at: string;
};

export type ThreatCreate = {
  name: string;
  category: ThreatCategory;
  description?: string;
  likelihood?: ThreatLikelihood;
};

// --- Vulnerabilities -----------------------------------------------------------

export type VulnerabilitySeverity = 'low' | 'medium' | 'high' | 'critical';
export type VulnerabilityStatus = 'open' | 'mitigated' | 'accepted' | 'closed';

export type Vulnerability = {
  id: string;
  organization_id: string;
  name: string;
  description: string;
  severity: VulnerabilitySeverity;
  status: VulnerabilityStatus;
  created_at: string;
  updated_at: string;
};

export type VulnerabilityCreate = {
  name: string;
  severity: VulnerabilitySeverity;
  description?: string;
};

// --- Incidents -----------------------------------------------------------------

export type IncidentSeverity = 'low' | 'medium' | 'high' | 'critical';
export type IncidentStatus = 'open' | 'investigating' | 'resolved' | 'closed';

export type Incident = {
  id: string;
  organization_id: string;
  title: string;
  description: string;
  severity: IncidentSeverity;
  status: IncidentStatus;
  reported_by: string;
  resolved_at: string | null;
  created_at: string;
  updated_at: string;
};

export type IncidentCreate = {
  title: string;
  severity: IncidentSeverity;
  reported_by: string;
  description?: string;
};

// --- Feared Events ---------------------------------------------------------------

export type FearedEventCriterion = 'confidentiality' | 'integrity' | 'availability';
export type FearedEventGravity = 'low' | 'medium' | 'high' | 'critical';

export type FearedEvent = {
  id: string;
  organization_id: string;
  title: string;
  description: string;
  asset_id: string;
  criterion: FearedEventCriterion;
  gravity: FearedEventGravity;
  created_at: string;
  updated_at: string;
};

export type FearedEventCreate = {
  title: string;
  asset_id: string;
  criterion: FearedEventCriterion;
  gravity: FearedEventGravity;
  description?: string;
};

// --- Tasks -----------------------------------------------------------------------

export type TaskStatus = 'open' | 'in_progress' | 'done';

export type Task = {
  id: string;
  organization_id: string;
  title: string;
  description: string;
  status: TaskStatus;
  due_date: string | null;
  assignee: string;
  created_at: string;
  updated_at: string;
};

export type TaskCreate = {
  title: string;
  assignee: string;
  description?: string;
  due_date?: string | null;
};

// --- EBIOS RM Workshop 2: risk sources + risk origins (SR/OV pairing) ------------

export type RiskSourceCategory =
  | 'state'
  | 'organized_crime'
  | 'terrorist'
  | 'activist'
  | 'vengeful_individual'
  | 'amateur'
  | 'specialized_firm';
export type RiskSourceLevel = 'low' | 'moderate' | 'significant' | 'very_high';
export type RiskSourceActivity = 'low' | 'medium' | 'high';

export type RiskSource = {
  id: string;
  organization_id: string;
  name: string;
  description: string;
  category: RiskSourceCategory;
  motivation: RiskSourceLevel;
  resources: RiskSourceLevel;
  activity: RiskSourceActivity;
  created_at: string;
  updated_at: string;
};

export type RiskSourceCreate = {
  name: string;
  category: RiskSourceCategory;
  description?: string;
  motivation?: RiskSourceLevel;
  resources?: RiskSourceLevel;
  activity?: RiskSourceActivity;
};

export type RiskOriginPertinence = 'low' | 'medium' | 'high' | 'critical';

export type RiskOrigin = {
  id: string;
  organization_id: string;
  risk_source_id: string;
  target_objective: string;
  feared_event_id: string | null;
  pertinence: RiskOriginPertinence;
  retained: boolean;
  created_at: string;
  updated_at: string;
};

export type RiskOriginCreate = {
  risk_source_id: string;
  target_objective: string;
  feared_event_id?: string | null;
  pertinence?: RiskOriginPertinence;
  retained?: boolean;
};

// --- EBIOS RM Workshop 3: ecosystem parties + strategic scenarios ----------------

export type EcosystemPartyCategory = 'provider' | 'subcontractor' | 'partner' | 'client';
export type EcosystemPartyLevel = 'low' | 'medium' | 'high';

export type EcosystemParty = {
  id: string;
  organization_id: string;
  name: string;
  description: string;
  category: EcosystemPartyCategory;
  dependency_level: EcosystemPartyLevel;
  cyber_maturity: EcosystemPartyLevel;
  created_at: string;
  updated_at: string;
};

export type EcosystemPartyCreate = {
  name: string;
  category: EcosystemPartyCategory;
  description?: string;
  dependency_level?: EcosystemPartyLevel;
  cyber_maturity?: EcosystemPartyLevel;
};

export type StrategicScenarioLikelihood = 'low' | 'medium' | 'high' | 'critical';

export type StrategicScenario = {
  id: string;
  organization_id: string;
  risk_origin_id: string;
  feared_event_id: string;
  ecosystem_party_id: string | null;
  name: string;
  description: string;
  likelihood: StrategicScenarioLikelihood;
  created_at: string;
  updated_at: string;
};

export type StrategicScenarioCreate = {
  risk_origin_id: string;
  feared_event_id: string;
  name: string;
  ecosystem_party_id?: string | null;
  description?: string;
  likelihood?: StrategicScenarioLikelihood;
};
