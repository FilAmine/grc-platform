import { api } from './client';
import type { ComplianceSummary, Control, Organization, Risk } from './types';

export async function getSummary(): Promise<ComplianceSummary> {
  const { data } = await api.get<ComplianceSummary>('/system/summary');
  return data;
}

export async function getOrganizations(): Promise<Organization[]> {
  const { data } = await api.get<Organization[]>('/organizations');
  return data;
}

export async function getRisks(): Promise<Risk[]> {
  const { data } = await api.get<Risk[]>('/risks');
  return data;
}

export async function getControls(): Promise<Control[]> {
  const { data } = await api.get<Control[]>('/controls');
  return data;
}
