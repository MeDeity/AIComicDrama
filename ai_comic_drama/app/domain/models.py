from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Character:
    name: str
    role: Optional[str] = None
    personality: Optional[str] = None
    appearance_hint: Optional[str] = None


@dataclass
class Dialogue:
    speaker: str
    text: str
    emotion: Optional[str] = None


@dataclass
class Beat:
    id: str
    summary: str
    dialogues: List[Dialogue] = field(default_factory=list)
    narration: Optional[str] = None


@dataclass
class Scene:
    id: str
    title: str
    location: Optional[str] = None
    time: Optional[str] = None
    mood: Optional[str] = None
    description: Optional[str] = None
    beats: List[Beat] = field(default_factory=list)


@dataclass
class Script:
    title: str
    summary: Optional[str] = None
    scenes: List[Scene] = field(default_factory=list)
    characters: List[Character] = field(default_factory=list)


@dataclass
class StoryTask:
    id: str
    story_title: Optional[str] = None
    status: str = "pending"
    message: Optional[str] = None

