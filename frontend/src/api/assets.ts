import { api } from './client';
import type { Asset, AssetCreate, AssetLifecycleStage } from './types';

export async function getAssets(): Promise<Asset[]> {
  const { data } = await api.get<Asset[]>('/assets');
  return data;
}

export async function getAsset(assetId: string): Promise<Asset> {
  const { data } = await api.get<Asset>(`/assets/${assetId}`);
  return data;
}

export async function createAsset(payload: AssetCreate): Promise<Asset> {
  const { data } = await api.post<Asset>('/assets', payload);
  return data;
}

export async function updateAssetLifecycle(assetId: string, lifecycle_stage: AssetLifecycleStage): Promise<Asset> {
  const { data } = await api.patch<Asset>(`/assets/${assetId}/lifecycle`, { lifecycle_stage });
  return data;
}
