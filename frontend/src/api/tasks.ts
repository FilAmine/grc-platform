import { api } from './client';
import type { Task, TaskCreate, TaskStatus } from './types';

export async function getTasks(): Promise<Task[]> {
  const { data } = await api.get<Task[]>('/tasks');
  return data;
}

export async function createTask(payload: TaskCreate): Promise<Task> {
  const { data } = await api.post<Task>('/tasks', payload);
  return data;
}

export async function updateTaskStatus(taskId: string, status: TaskStatus): Promise<Task> {
  const { data } = await api.patch<Task>(`/tasks/${taskId}/status`, { status });
  return data;
}
