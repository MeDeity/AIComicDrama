from ..domain.models import Script
from ..schemas.story import StoryCreate


class StoryWriterService:
    async def generate_script(self, story: StoryCreate) -> Script:
        title = story.title or "Untitled"
        summary = story.content[:100]
        return Script(title=title, summary=summary)

