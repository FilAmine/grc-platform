import { api } from './client';
import type { RiskSource, RiskSourceCreate } from './types';

export async function getRiskSources(): Promise<RiskSource[]> {
  const { data } = await api.get<RiskSource[]>('/risk-sources');
  return data;
}

export async function createRiskSource(payload: RiskSourceCreate): Promise<RiskSource> {
  const { data } = await api.post<RiskSource>('/risk-sources', payload);
  return data;
}
