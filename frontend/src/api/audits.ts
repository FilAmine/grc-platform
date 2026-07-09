import { api } from './client';
import type {
  Audit,
  AuditCreate,
  AuditReport,
  AuditStatus,
  ChecklistItem,
  ChecklistItemStatus,
  CorrectiveAction,
  CorrectiveActionStatus,
  Finding,
  FindingSeverity,
  FindingStatus,
} from './types';

export async function getAudits(): Promise<Audit[]> {
  const { data } = await api.get<Audit[]>('/audits');
  return data;
}

export async function getAudit(auditId: string): Promise<Audit> {
  const { data } = await api.get<Audit>(`/audits/${auditId}`);
  return data;
}

export async function createAudit(payload: AuditCreate): Promise<Audit> {
  const { data } = await api.post<Audit>('/audits', payload);
  return data;
}

export async function updateAuditStatus(auditId: string, status: AuditStatus): Promise<Audit> {
  const { data } = await api.patch<Audit>(`/audits/${auditId}/status`, { status });
  return data;
}

export async function getAuditReport(auditId: string): Promise<AuditReport> {
  const { data } = await api.get<AuditReport>(`/audits/${auditId}/report`);
  return data;
}

export async function getChecklistItems(auditId: string): Promise<ChecklistItem[]> {
  const { data } = await api.get<ChecklistItem[]>(`/audits/${auditId}/checklist-items`);
  return data;
}

export async function createChecklistItem(auditId: string, description: string): Promise<ChecklistItem> {
  const { data } = await api.post<ChecklistItem>(`/audits/${auditId}/checklist-items`, { description });
  return data;
}

export async function updateChecklistItemStatus(
  itemId: string,
  status: ChecklistItemStatus,
  notes: string,
): Promise<ChecklistItem> {
  const { data } = await api.put<ChecklistItem>(`/audits/checklist-items/${itemId}/status`, { status, notes });
  return data;
}

export async function getFindings(auditId: string): Promise<Finding[]> {
  const { data } = await api.get<Finding[]>(`/audits/${auditId}/findings`);
  return data;
}

export async function createFinding(
  auditId: string,
  payload: { title: string; description: string; severity: FindingSeverity; checklist_item_id?: string | null },
): Promise<Finding> {
  const { data } = await api.post<Finding>(`/audits/${auditId}/findings`, payload);
  return data;
}

export async function updateFindingStatus(findingId: string, status: FindingStatus): Promise<Finding> {
  const { data } = await api.patch<Finding>(`/audits/findings/${findingId}/status`, { status });
  return data;
}

export async function getCorrectiveActions(findingId: string): Promise<CorrectiveAction[]> {
  const { data } = await api.get<CorrectiveAction[]>(`/audits/findings/${findingId}/corrective-actions`);
  return data;
}

export async function createCorrectiveAction(
  findingId: string,
  payload: { description: string; owner: string; due_date?: string | null },
): Promise<CorrectiveAction> {
  const { data } = await api.post<CorrectiveAction>(`/audits/findings/${findingId}/corrective-actions`, payload);
  return data;
}

export async function updateCorrectiveActionStatus(
  actionId: string,
  status: CorrectiveActionStatus,
): Promise<CorrectiveAction> {
  const { data } = await api.patch<CorrectiveAction>(`/audits/corrective-actions/${actionId}/status`, { status });
  return data;
}
