from abc import ABC, abstractmethod
from typing import Optional

import httpx

from ..core.config import get_settings


class LLMClient(ABC):
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        raise NotImplementedError


class DummyLLMClient(LLMClient):
    async def generate(self, prompt: str) -> str:
        return "根据提供的故事大纲生成一段简要的剧情概述，用于后续分镜和画面设计。"


class OllamaLLMClient(LLMClient):
    def __init__(self, base_url: str, model: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model

    async def generate(self, prompt: str) -> str:
        async with httpx.AsyncClient(base_url=self.base_url, timeout=60) as client:
            response = await client.post(
                "/api/chat",
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    "stream": False,
                },
            )
            response.raise_for_status()
            data = response.json()
            message = data.get("message") or {}
            content: Optional[str] = message.get("content")
            if not content:
                return ""
            return str(content).strip()


def get_llm_client() -> LLMClient:
    settings = get_settings()
    provider = settings.llm_provider.lower()
    if provider == "ollama":
        return OllamaLLMClient(
            base_url=settings.ollama_base_url,
            model=settings.ollama_model,
        )
    return DummyLLMClient()

