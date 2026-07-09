import { api } from './client';
import type {
  ComplianceSummary,
  Control,
  ControlCreate,
  Organization,
  Risk,
  RiskCreate,
} from './types';

export async function getSummary(): Promise<ComplianceSummary> {
  const { data } = await api.get<ComplianceSummary>('/dashboard/summary');
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

export async function createRisk(payload: RiskCreate): Promise<Risk> {
  const { data } = await api.post<Risk>('/risks', payload);
  return data;
}

export async function getControls(): Promise<Control[]> {
  const { data } = await api.get<Control[]>('/controls');
  return data;
}

export async function createControl(payload: ControlCreate): Promise<Control> {
  const { data } = await api.post<Control>('/controls', payload);
  return data;
}
