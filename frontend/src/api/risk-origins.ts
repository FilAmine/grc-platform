import { api } from './client';
import type { RiskOrigin, RiskOriginCreate } from './types';

export async function getRiskOrigins(): Promise<RiskOrigin[]> {
  const { data } = await api.get<RiskOrigin[]>('/risk-origins');
  return data;
}

export async function createRiskOrigin(payload: RiskOriginCreate): Promise<RiskOrigin> {
  const { data } = await api.post<RiskOrigin>('/risk-origins', payload);
  return data;
}
