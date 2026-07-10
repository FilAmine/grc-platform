import { api } from './client';
import type { Notification } from './types';

export async function getNotifications(): Promise<Notification[]> {
  const { data } = await api.get<Notification[]>('/notifications');
  return data;
}

export async function markNotificationRead(notificationId: string): Promise<Notification> {
  const { data } = await api.post<Notification>(`/notifications/${notificationId}/read`);
  return data;
}
