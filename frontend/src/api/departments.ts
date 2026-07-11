import { api } from './client';
import type { Department, DepartmentCreate } from './types';

export async function getDepartments(): Promise<Department[]> {
  const { data } = await api.get<Department[]>('/departments');
  return data;
}

export async function createDepartment(payload: DepartmentCreate): Promise<Department> {
  const { data } = await api.post<Department>('/departments', payload);
  return data;
}
