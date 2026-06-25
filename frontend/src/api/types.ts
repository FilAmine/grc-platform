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

export type ComplianceSummary = {
  organizations: number;
  risks_open: number;
  controls_active: number;
  posture: 'healthy' | 'attention_required';
};
