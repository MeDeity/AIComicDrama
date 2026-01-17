from typing import Literal, Optional

from pydantic import BaseModel


TaskStatus = Literal["pending", "processing", "success", "failed"]


class TaskStatusResponse(BaseModel):
    task_id: str
    status: TaskStatus
    message: Optional[str] = None
    video_url: Optional[str] = None
