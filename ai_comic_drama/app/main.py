from fastapi import FastAPI

from .api.v1.routes_story import router as story_router
from .core.config import get_settings


settings = get_settings()

app = FastAPI(title=settings.app_name)

app.include_router(story_router, prefix="/api/v1/story", tags=["story"])

