import { api } from './client';
import type { EcosystemParty, EcosystemPartyCreate } from './types';

export async function getEcosystemParties(): Promise<EcosystemParty[]> {
  const { data } = await api.get<EcosystemParty[]>('/ecosystem-parties');
  return data;
}

export async function createEcosystemParty(payload: EcosystemPartyCreate): Promise<EcosystemParty> {
  const { data } = await api.post<EcosystemParty>('/ecosystem-parties', payload);
  return data;
}
