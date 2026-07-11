import { api } from './client';
import type { Vulnerability, VulnerabilityCreate } from './types';

export async function getVulnerabilities(): Promise<Vulnerability[]> {
  const { data } = await api.get<Vulnerability[]>('/vulnerabilities');
  return data;
}

export async function createVulnerability(payload: VulnerabilityCreate): Promise<Vulnerability> {
  const { data } = await api.post<Vulnerability>('/vulnerabilities', payload);
  return data;
}
