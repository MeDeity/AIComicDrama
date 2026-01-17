from ..domain.models import Beat, Scene, Script
from ..infrastructure.llm_client import LLMClient, get_llm_client
from ..schemas.story import StoryCreate


class StoryWriterService:
    def __init__(self, llm_client: LLMClient | None = None) -> None:
        self.llm_client = llm_client or get_llm_client()

    async def generate_script(self, story: StoryCreate) -> Script:
        title = story.title or "Untitled"
        base_prompt = (
            "你是一个资深漫剧编剧，请根据下面的故事内容，用中文写一段不超过 300 字的剧情概述，"
            "要求结构清晰，适合后续拆分成分镜和镜头，不要输出任何解释说明。\n\n"
            f"故事内容：\n{story.content}\n"
        )
        try:
            summary = await self.llm_client.generate(base_prompt)
        except Exception:
            summary = story.content[:300]
        if not summary:
            summary = story.content[:300] or "暂无剧情概述"
        beat = Beat(id="beat-1", summary=summary)
        scene = Scene(id="scene-1", title=title, description=summary, beats=[beat])
        return Script(title=title, summary=summary, scenes=[scene])
