import { api } from './client';
import type {
  ChatMessage,
  ChatMessageCreate,
  ChatSession,
  ChatSessionCreate,
  KnowledgeBaseDocumentCreate,
  PromptTemplate,
  PromptTemplateCreate,
} from './types';

export async function getChatSessions(): Promise<ChatSession[]> {
  const { data } = await api.get<ChatSession[]>('/ai/chat/sessions');
  return data;
}

export async function createChatSession(payload: ChatSessionCreate = {}): Promise<ChatSession> {
  const { data } = await api.post<ChatSession>('/ai/chat/sessions', payload);
  return data;
}

export async function getChatMessages(sessionId: string): Promise<ChatMessage[]> {
  const { data } = await api.get<ChatMessage[]>(`/ai/chat/sessions/${sessionId}/messages`);
  return data;
}

export async function sendChatMessage(sessionId: string, payload: ChatMessageCreate): Promise<ChatMessage> {
  const { data } = await api.post<ChatMessage>(`/ai/chat/sessions/${sessionId}/messages`, payload);
  return data;
}

export async function getPromptTemplates(): Promise<PromptTemplate[]> {
  const { data } = await api.get<PromptTemplate[]>('/ai/prompts');
  return data;
}

export async function createPromptTemplate(payload: PromptTemplateCreate): Promise<PromptTemplate> {
  const { data } = await api.post<PromptTemplate>('/ai/prompts', payload);
  return data;
}

export async function addKnowledgeBaseDocument(payload: KnowledgeBaseDocumentCreate): Promise<void> {
  await api.post('/ai/knowledge-base', payload);
}
