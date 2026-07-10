import { api } from './client';
import type {
  Assessment,
  AssessmentCreate,
  AssessmentResult,
  AssessmentResultUpdate,
  AssessmentStatus,
  ComplianceScore,
  Evidence,
  EvidenceCreate,
  Framework,
  FrameworkVersion,
  Requirement,
} from './types';

export async function getFrameworks(): Promise<Framework[]> {
  const { data } = await api.get<Framework[]>('/compliance/frameworks');
  return data;
}

export async function getFrameworkVersions(frameworkId: string): Promise<FrameworkVersion[]> {
  const { data } = await api.get<FrameworkVersion[]>(`/compliance/frameworks/${frameworkId}/versions`);
  return data;
}

export async function getRequirements(frameworkVersionId: string): Promise<Requirement[]> {
  const { data } = await api.get<Requirement[]>(`/compliance/framework-versions/${frameworkVersionId}/requirements`);
  return data;
}

export async function getFrameworkCatalog(): Promise<{
  frameworks: Framework[];
  versionsByFramework: Record<string, FrameworkVersion[]>;
}> {
  const frameworks = await getFrameworks();
  const versionsByFramework: Record<string, FrameworkVersion[]> = {};
  await Promise.all(
    frameworks.map(async (framework) => {
      versionsByFramework[framework.id] = await getFrameworkVersions(framework.id);
    }),
  );
  return { frameworks, versionsByFramework };
}

export async function getAssessments(): Promise<Assessment[]> {
  const { data } = await api.get<Assessment[]>('/compliance/assessments');
  return data;
}

export async function getAssessment(assessmentId: string): Promise<Assessment> {
  const { data } = await api.get<Assessment>(`/compliance/assessments/${assessmentId}`);
  return data;
}

export async function createAssessment(payload: AssessmentCreate): Promise<Assessment> {
  const { data } = await api.post<Assessment>('/compliance/assessments', payload);
  return data;
}

export async function updateAssessmentStatus(assessmentId: string, status: AssessmentStatus): Promise<Assessment> {
  const { data } = await api.patch<Assessment>(`/compliance/assessments/${assessmentId}/status`, { status });
  return data;
}

export async function getAssessmentResults(assessmentId: string): Promise<AssessmentResult[]> {
  const { data } = await api.get<AssessmentResult[]>(`/compliance/assessments/${assessmentId}/results`);
  return data;
}

export async function upsertAssessmentResult(
  assessmentId: string,
  requirementId: string,
  payload: AssessmentResultUpdate,
): Promise<AssessmentResult> {
  const { data } = await api.put<AssessmentResult>(
    `/compliance/assessments/${assessmentId}/results/${requirementId}`,
    payload,
  );
  return data;
}

export async function computeScore(assessmentId: string): Promise<ComplianceScore> {
  const { data } = await api.post<ComplianceScore>(`/compliance/assessments/${assessmentId}/compute-score`);
  return data;
}

export async function getScore(assessmentId: string): Promise<ComplianceScore | null> {
  const { data } = await api.get<ComplianceScore | null>(`/compliance/assessments/${assessmentId}/score`);
  return data;
}

export async function createEvidence(payload: EvidenceCreate): Promise<Evidence> {
  const { data } = await api.post<Evidence>('/compliance/evidence', payload);
  return data;
}

export async function getEvidenceForResult(assessmentResultId: string): Promise<Evidence[]> {
  const { data } = await api.get<Evidence[]>(`/compliance/assessments/results/${assessmentResultId}/evidence`);
  return data;
}
