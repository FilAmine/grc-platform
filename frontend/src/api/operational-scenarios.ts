import { api } from './client';
import type { OperationalScenario, OperationalScenarioCreate } from './types';

export async function getOperationalScenarios(): Promise<OperationalScenario[]> {
  const { data } = await api.get<OperationalScenario[]>('/operational-scenarios');
  return data;
}

export async function createOperationalScenario(
  payload: OperationalScenarioCreate,
): Promise<OperationalScenario> {
  const { data } = await api.post<OperationalScenario>('/operational-scenarios', payload);
  return data;
}
