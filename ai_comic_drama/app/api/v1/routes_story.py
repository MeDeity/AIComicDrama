from uuid import uuid4

from fastapi import APIRouter, HTTPException

from ...domain.models import StoryTask
from ...infrastructure.db import get_task, save_task
from ...pipeline.workflow import StoryCreationWorkflow
from ...schemas.story import StoryCreate
from ...schemas.task import TaskStatusResponse


router = APIRouter()


@router.post("/", response_model=TaskStatusResponse)
async def submit_story(story: StoryCreate) -> TaskStatusResponse:
    task_id = f"task-{uuid4().hex}"
    task = StoryTask(id=task_id, story_title=story.title or None, status="processing")
    save_task(task)
    workflow = StoryCreationWorkflow()
    video_url = await workflow.run(story)
    task.status = "success"
    task.video_url = video_url
    save_task(task)
    return TaskStatusResponse(task_id=task.id, status="success", video_url=task.video_url)


@router.get("/{task_id}", response_model=TaskStatusResponse)
async def get_task_status(task_id: str) -> TaskStatusResponse:
    task = get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskStatusResponse(task_id=task.id, status=task.status, message=task.message, video_url=task.video_url)
