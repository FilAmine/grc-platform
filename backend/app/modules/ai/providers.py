"""AI provider abstraction.

Every provider-specific detail (endpoint shape, auth header, payload format)
lives here and nowhere else. The rest of the ``ai`` module only ever talks to
the ``AIProvider`` protocol, so adding a new provider never touches
service.py, api.py, or any other module.
"""

from __future__ import annotations

import hashlib
import math
from typing import Protocol

import httpx
from backend.app.core.config import Settings


class AIProviderError(Exception):
    pass


class AIProvider(Protocol):
    def chat(self, system_prompt: str, messages: list[tuple[str, str]]) -> str:
        """``messages`` is a list of (role, content) pairs; returns the assistant reply."""
        raise NotImplementedError

    def embed(self, text: str) -> list[float]:
        raise NotImplementedError


class EchoProvider:
    """Deterministic, network-free provider. The default so the platform is usable
    (and testable) with zero external configuration; swap in a real provider via
    ``settings.ai_provider`` once credentials are available."""

    EMBEDDING_DIMENSIONS = 32

    def chat(self, system_prompt: str, messages: list[tuple[str, str]]) -> str:
        last_user_message = next((content for role, content in reversed(messages) if role == "user"), "")
        return f"[echo] {last_user_message}"

    def embed(self, text: str) -> list[float]:
        digest = hashlib.sha256(text.encode("utf-8")).digest()
        return [(b / 255.0) * 2 - 1 for b in digest[: self.EMBEDDING_DIMENSIONS]]


class OpenAIProvider:
    def __init__(self, api_key: str, model: str) -> None:
        self._api_key = api_key
        self._model = model

    def chat(self, system_prompt: str, messages: list[tuple[str, str]]) -> str:
        payload = {
            "model": self._model,
            "messages": [{"role": "system", "content": system_prompt}]
            + [{"role": role, "content": content} for role, content in messages],
        }
        response = httpx.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {self._api_key}"},
            json=payload,
            timeout=30.0,
        )
        if response.status_code != 200:
            raise AIProviderError(f"OpenAI chat request failed: {response.status_code} {response.text}")
        return response.json()["choices"][0]["message"]["content"]

    def embed(self, text: str) -> list[float]:
        response = httpx.post(
            "https://api.openai.com/v1/embeddings",
            headers={"Authorization": f"Bearer {self._api_key}"},
            json={"model": "text-embedding-3-small", "input": text},
            timeout=30.0,
        )
        if response.status_code != 200:
            raise AIProviderError(f"OpenAI embedding request failed: {response.status_code} {response.text}")
        return response.json()["data"][0]["embedding"]


class AzureOpenAIProvider:
    def __init__(self, endpoint: str, api_key: str, deployment: str) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._api_key = api_key
        self._deployment = deployment

    def chat(self, system_prompt: str, messages: list[tuple[str, str]]) -> str:
        url = f"{self._endpoint}/openai/deployments/{self._deployment}/chat/completions?api-version=2024-06-01"
        payload = {
            "messages": [{"role": "system", "content": system_prompt}]
            + [{"role": role, "content": content} for role, content in messages],
        }
        response = httpx.post(url, headers={"api-key": self._api_key}, json=payload, timeout=30.0)
        if response.status_code != 200:
            raise AIProviderError(f"Azure OpenAI chat request failed: {response.status_code} {response.text}")
        return response.json()["choices"][0]["message"]["content"]

    def embed(self, text: str) -> list[float]:
        url = f"{self._endpoint}/openai/deployments/{self._deployment}/embeddings?api-version=2024-06-01"
        response = httpx.post(url, headers={"api-key": self._api_key}, json={"input": text}, timeout=30.0)
        if response.status_code != 200:
            raise AIProviderError(f"Azure OpenAI embedding request failed: {response.status_code} {response.text}")
        return response.json()["data"][0]["embedding"]


class OllamaProvider:
    def __init__(self, base_url: str, model: str) -> None:
        self._base_url = base_url.rstrip("/")
        self._model = model

    def chat(self, system_prompt: str, messages: list[tuple[str, str]]) -> str:
        payload = {
            "model": self._model,
            "messages": [{"role": "system", "content": system_prompt}]
            + [{"role": role, "content": content} for role, content in messages],
            "stream": False,
        }
        response = httpx.post(f"{self._base_url}/api/chat", json=payload, timeout=60.0)
        if response.status_code != 200:
            raise AIProviderError(f"Ollama chat request failed: {response.status_code} {response.text}")
        return response.json()["message"]["content"]

    def embed(self, text: str) -> list[float]:
        response = httpx.post(
            f"{self._base_url}/api/embeddings", json={"model": self._model, "prompt": text}, timeout=60.0
        )
        if response.status_code != 200:
            raise AIProviderError(f"Ollama embedding request failed: {response.status_code} {response.text}")
        return response.json()["embedding"]


def get_ai_provider(settings: Settings) -> AIProvider:
    provider = settings.ai_provider.lower()
    if provider == "openai" and settings.openai_api_key:
        return OpenAIProvider(settings.openai_api_key, settings.openai_model)
    azure_configured = (
        settings.azure_openai_endpoint and settings.azure_openai_api_key and settings.azure_openai_deployment
    )
    if provider == "azure_openai" and azure_configured:
        return AzureOpenAIProvider(
            settings.azure_openai_endpoint, settings.azure_openai_api_key, settings.azure_openai_deployment
        )
    if provider == "ollama":
        return OllamaProvider(settings.ollama_base_url, settings.ollama_model)
    return EchoProvider()


def cosine_similarity(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)
