from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .api.v1.routes_story import router as story_router
from .core.config import get_settings


settings = get_settings()

app = FastAPI(title=settings.app_name)

app.mount("/static", StaticFiles(directory="ai_comic_drama/app/static"), name="static")
templates = Jinja2Templates(directory="ai_comic_drama/app/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.include_router(story_router, prefix="/api/v1/story", tags=["story"])
