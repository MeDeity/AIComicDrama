from typing import Dict, Optional

from ..domain.models import StoryTask


_TASKS: Dict[str, StoryTask] = {}


class DatabaseSession:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


def save_task(task: StoryTask) -> None:
    _TASKS[task.id] = task


def get_task(task_id: str) -> Optional[StoryTask]:
    return _TASKS.get(task_id)
