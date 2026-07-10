import { api } from './client';
import type { SsoConnection, SsoConnectionUpdate } from './types';

export async function getSsoConnection(): Promise<SsoConnection | null> {
  const { data } = await api.get<SsoConnection | null>('/sso/connection');
  return data;
}

export async function configureSso(payload: SsoConnectionUpdate): Promise<SsoConnection> {
  const { data } = await api.put<SsoConnection>('/sso/connection', payload);
  return data;
}

export async function deleteSso(): Promise<void> {
  await api.delete('/sso/connection');
}
