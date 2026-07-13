import { api } from './client';
import type { StrategicScenario, StrategicScenarioCreate } from './types';

export async function getStrategicScenarios(): Promise<StrategicScenario[]> {
  const { data } = await api.get<StrategicScenario[]>('/strategic-scenarios');
  return data;
}

export async function createStrategicScenario(
  payload: StrategicScenarioCreate,
): Promise<StrategicScenario> {
  const { data } = await api.post<StrategicScenario>('/strategic-scenarios', payload);
  return data;
}
