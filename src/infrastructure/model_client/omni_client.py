"""
Cliente para NVIDIA Nemotron 3 Nano Omni
Soporta texto, imagen, audio, video y documentos
"""
import structlog
import aiohttp
import asyncio
import base64
from typing import Optional, Dict, Any, Union
from tenacity import retry, stop_after_attempt, wait_exponential

from src.infrastructure.config import settings
from src.shared.result import Result, ok, err
from src.shared.errors import DomainError, model_inference_error

logger = structlog.get_logger(__name__)


class OmniModality:
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    DOCUMENT = "document"
    GUI = "gui"


class OmniModelClient:
    
    def __init__(self, session: Optional[aiohttp.ClientSession] = None):
        self._session = session
        self._base_url = getattr(settings, "OMNI_MODEL_URL", "https://build.nvidia.com/nvidia/nemotron-3-nano-omni")
        self._api_key = getattr(settings, "NVIDIA_API_KEY", None)
        self._timeout = aiohttp.ClientTimeout(total=60)
    
    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            headers = {"Authorization": f"Bearer {self._api_key}"} if self._api_key else {}
            headers["Content-Type"] = "application/json"
            self._session = aiohttp.ClientSession(headers=headers, timeout=self._timeout)
        return self._session
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
    async def process(self, modality: str, content: Union[str, bytes], prompt: str, max_tokens: int = 4096, temperature: float = 0.7) -> Result[str, DomainError]:
        try:
            session = await self._get_session()
            payload = {
                "model": "nemotron-3-nano-omni",
                "prompt": prompt,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "modality": modality
            }
            if modality == OmniModality.TEXT:
                payload["text"] = content
            elif modality in [OmniModality.IMAGE, OmniModality.GUI]:
                if isinstance(content, bytes):
                    payload["image_base64"] = base64.b64encode(content).decode()
                else:
                    payload["image_url"] = content
            elif modality == OmniModality.AUDIO and isinstance(content, bytes):
                payload["audio_base64"] = base64.b64encode(content).decode()
            elif modality == OmniModality.VIDEO and isinstance(content, bytes):
                payload["video_base64"] = base64.b64encode(content).decode()
            elif modality == OmniModality.DOCUMENT:
                payload["document_url"] = content if isinstance(content, str) else ""
            
            logger.info("omni_model_call", modality=modality)
            async with session.post(f"{self._base_url}/v1/completions", json=payload) as response:
                if response.status != 200:
                    error_text = await response.text()
                    return err(model_inference_error(f"Omni API error: {response.status}"))
                data = await response.json()
                result = data.get("choices", [{}])[0].get("text", "")
                return ok(result)
        except Exception as e:
            return err(model_inference_error(str(e)))
    
    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()
