import { api } from './client';
import type { Approval, ApprovalDecision, DocumentCreate, DocumentVersion, GrcDocument, VersionCreate } from './types';

export async function getDocuments(): Promise<GrcDocument[]> {
  const { data } = await api.get<GrcDocument[]>('/documents');
  return data;
}

export async function getDocument(documentId: string): Promise<GrcDocument> {
  const { data } = await api.get<GrcDocument>(`/documents/${documentId}`);
  return data;
}

export async function createDocument(payload: DocumentCreate): Promise<GrcDocument> {
  const { data } = await api.post<GrcDocument>('/documents', payload);
  return data;
}

export async function archiveDocument(documentId: string): Promise<GrcDocument> {
  const { data } = await api.post<GrcDocument>(`/documents/${documentId}/archive`);
  return data;
}

export async function getVersions(documentId: string): Promise<DocumentVersion[]> {
  const { data } = await api.get<DocumentVersion[]>(`/documents/${documentId}/versions`);
  return data;
}

export async function createVersion(documentId: string, payload: VersionCreate): Promise<DocumentVersion> {
  const { data } = await api.post<DocumentVersion>(`/documents/${documentId}/versions`, payload);
  return data;
}

export async function submitForApproval(versionId: string): Promise<DocumentVersion> {
  const { data } = await api.post<DocumentVersion>(`/documents/versions/${versionId}/submit-for-approval`);
  return data;
}

export async function decideApproval(versionId: string, payload: ApprovalDecision): Promise<Approval> {
  const { data } = await api.post<Approval>(`/documents/versions/${versionId}/approval`, payload);
  return data;
}

export async function getApprovals(versionId: string): Promise<Approval[]> {
  const { data } = await api.get<Approval[]>(`/documents/versions/${versionId}/approvals`);
  return data;
}
