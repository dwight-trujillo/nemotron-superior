"""
Herramientas para Nemotron 3 Nano Omni
Se integran con el ToolExecutor existente
"""
from typing import Dict, Any
from src.infrastructure.model_client.omni_client import OmniModelClient, OmniModality


async def execute_omni_vision(args: Dict[str, Any]) -> Dict[str, Any]:
    image_url = args.get("image_url") or args.get("image_base64")
    prompt = args.get("prompt", "Describe this image in detail")
    if not image_url:
        return {"result": "Error: No image provided", "success": False}
    client = OmniModelClient()
    result = await client.process(OmniModality.IMAGE, image_url, prompt, args.get("max_tokens", 512))
    if result.is_err():
        return {"result": f"Vision failed: {result.error.message}", "success": False}
    return {"result": result.value, "success": True}


async def execute_omni_document(args: Dict[str, Any]) -> Dict[str, Any]:
    doc_url = args.get("document_url")
    prompt = args.get("prompt", "Extract and summarize key information")
    if not doc_url:
        return {"result": "Error: No document provided", "success": False}
    client = OmniModelClient()
    result = await client.process(OmniModality.DOCUMENT, doc_url, prompt)
    if result.is_err():
        return {"result": f"Document analysis failed: {result.error.message}", "success": False}
    return {"result": result.value, "success": True}


async def execute_omni_audio(args: Dict[str, Any]) -> Dict[str, Any]:
    audio_url = args.get("audio_url")
    prompt = args.get("prompt", "Transcribe and summarize this audio")
    if not audio_url:
        return {"result": "Error: No audio provided", "success": False}
    client = OmniModelClient()
    result = await client.process(OmniModality.AUDIO, audio_url, prompt)
    return {"result": result.value if result.is_ok() else f"Error: {result.error.message}", "success": result.is_ok()}


async def execute_omni_video(args: Dict[str, Any]) -> Dict[str, Any]:
    video_url = args.get("video_url")
    prompt = args.get("prompt", "Analyze this video and describe what happens")
    if not video_url:
        return {"result": "Error: No video provided", "success": False}
    client = OmniModelClient()
    result = await client.process(OmniModality.VIDEO, video_url, prompt)
    return {"result": result.value if result.is_ok() else f"Error: {result.error.message}", "success": result.is_ok()}


async def execute_omni_gui(args: Dict[str, Any]) -> Dict[str, Any]:
    screenshot_url = args.get("screenshot_url")
    task = args.get("task", "What is visible on this screen?")
    if not screenshot_url:
        return {"result": "Error: No screenshot provided", "success": False}
    client = OmniModelClient()
    result = await client.process(OmniModality.GUI, screenshot_url, f"Task: {task}\nNavigate and understand this user interface.")
    return {"result": result.value if result.is_ok() else f"GUI analysis failed: {result.error.message}", "success": result.is_ok()}
