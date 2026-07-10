import { api } from './client';
import type { Permission, Role, RoleCreate } from './types';

export async function getRoles(): Promise<Role[]> {
  const { data } = await api.get<Role[]>('/roles');
  return data;
}

export async function createRole(payload: RoleCreate): Promise<Role> {
  const { data } = await api.post<Role>('/roles', payload);
  return data;
}

export async function setRolePermissions(roleId: string, permissionCodes: string[]): Promise<Role> {
  const { data } = await api.put<Role>(`/roles/${roleId}/permissions`, { permission_codes: permissionCodes });
  return data;
}

export async function getPermissions(): Promise<Permission[]> {
  const { data } = await api.get<Permission[]>('/permissions');
  return data;
}
