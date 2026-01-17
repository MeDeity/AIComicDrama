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
class CharacterInShot:
    name: str
    position: Optional[str] = None
    pose: Optional[str] = None
    expression: Optional[str] = None


@dataclass
class Shot:
    id: str
    scene_id: str
    beat_id: str
    shot_type: str = "medium"
    camera_angle: Optional[str] = None
    composition: Optional[str] = None
    description: Optional[str] = None
    prompt: Optional[str] = None
    negative_prompt: Optional[str] = None
    characters: List[CharacterInShot] = field(default_factory=list)


@dataclass
class StoryTask:
    id: str
    story_title: Optional[str] = None
    status: str = "pending"
    message: Optional[str] = None
    video_url: Optional[str] = None
