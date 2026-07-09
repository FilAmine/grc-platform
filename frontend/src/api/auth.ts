import { api, authClient } from './client';
import type { RegisterOrganizationRequest, TokenResponse, User } from './types';

export async function login(email: string, password: string): Promise<TokenResponse> {
  const form = new URLSearchParams();
  form.set('username', email);
  form.set('password', password);
  const { data } = await authClient.post<TokenResponse>('/auth/login', form, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  });
  return data;
}

export async function registerOrganization(payload: RegisterOrganizationRequest): Promise<TokenResponse> {
  const { data } = await authClient.post<TokenResponse>('/auth/register-organization', payload);
  return data;
}

export async function logout(refreshToken: string): Promise<void> {
  await authClient.post('/auth/logout', { refresh_token: refreshToken });
}

export async function getMe(): Promise<User> {
  const { data } = await api.get<User>('/auth/me');
  return data;
}
