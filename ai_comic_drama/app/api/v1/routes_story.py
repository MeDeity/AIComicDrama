from fastapi import APIRouter, Depends

from ...schemas.story import StoryCreate
from ...schemas.task import TaskStatusResponse
from ...services.story_writer import StoryWriterService


router = APIRouter()


def get_story_writer() -> StoryWriterService:
    return StoryWriterService()


@router.post("/", response_model=TaskStatusResponse)
async def submit_story(
    story: StoryCreate,
    writer: StoryWriterService = Depends(get_story_writer),
) -> TaskStatusResponse:
    script = await writer.generate_script(story)
    task_id = f"task-{hash(script.title)}"
    return TaskStatusResponse(task_id=task_id, status="pending")


@router.get("/{task_id}", response_model=TaskStatusResponse)
async def get_task_status(task_id: str) -> TaskStatusResponse:
    return TaskStatusResponse(task_id=task_id, status="pending")

