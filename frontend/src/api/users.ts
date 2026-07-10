import { api } from './client';
import type { User, UserCreate, UserUpdate } from './types';

export async function getUsers(): Promise<User[]> {
  const { data } = await api.get<User[]>('/users');
  return data;
}

export async function getUser(userId: string): Promise<User> {
  const { data } = await api.get<User>(`/users/${userId}`);
  return data;
}

export async function createUser(payload: UserCreate): Promise<User> {
  const { data } = await api.post<User>('/users', payload);
  return data;
}

export async function updateUser(userId: string, payload: UserUpdate): Promise<User> {
  const { data } = await api.patch<User>(`/users/${userId}`, payload);
  return data;
}

export async function assignRole(userId: string, roleId: string): Promise<void> {
  await api.post(`/users/${userId}/roles/${roleId}`);
}

export async function removeRole(userId: string, roleId: string): Promise<void> {
  await api.delete(`/users/${userId}/roles/${roleId}`);
}
