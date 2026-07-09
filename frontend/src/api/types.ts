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
