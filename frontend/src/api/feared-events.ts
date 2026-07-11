import { api } from './client';
import type { FearedEvent, FearedEventCreate } from './types';

export async function getFearedEvents(): Promise<FearedEvent[]> {
  const { data } = await api.get<FearedEvent[]>('/feared-events');
  return data;
}

export async function createFearedEvent(payload: FearedEventCreate): Promise<FearedEvent> {
  const { data } = await api.post<FearedEvent>('/feared-events', payload);
  return data;
}
