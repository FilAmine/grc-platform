import { api } from './client';
import type { Incident, IncidentCreate, IncidentStatus } from './types';

export async function getIncidents(): Promise<Incident[]> {
  const { data } = await api.get<Incident[]>('/incidents');
  return data;
}

export async function createIncident(payload: IncidentCreate): Promise<Incident> {
  const { data } = await api.post<Incident>('/incidents', payload);
  return data;
}

export async function updateIncidentStatus(incidentId: string, status: IncidentStatus): Promise<Incident> {
  const { data } = await api.patch<Incident>(`/incidents/${incidentId}/status`, { status });
  return data;
}
