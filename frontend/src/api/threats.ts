import { api } from './client';
import type { Threat, ThreatCreate } from './types';

export async function getThreats(): Promise<Threat[]> {
  const { data } = await api.get<Threat[]>('/threats');
  return data;
}

export async function createThreat(payload: ThreatCreate): Promise<Threat> {
  const { data } = await api.post<Threat>('/threats', payload);
  return data;
}
