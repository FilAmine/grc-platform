import { api } from './client';
import type { RiskTreatment, RiskTreatmentCreate } from './types';

export async function getRiskTreatments(): Promise<RiskTreatment[]> {
  const { data } = await api.get<RiskTreatment[]>('/risk-treatments');
  return data;
}

export async function createRiskTreatment(payload: RiskTreatmentCreate): Promise<RiskTreatment> {
  const { data } = await api.post<RiskTreatment>('/risk-treatments', payload);
  return data;
}
