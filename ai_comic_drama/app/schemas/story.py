from typing import Optional

from pydantic import BaseModel


class StoryCreate(BaseModel):
    title: Optional[str] = None
    content: str
    tone: Optional[str] = None
    target_length: Optional[int] = None


class Story(BaseModel):
    id: str
    title: Optional[str] = None
    content: str

