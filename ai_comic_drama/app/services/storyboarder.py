from ..domain.models import Script, Shot


class StoryboarderService:
    async def generate_shots(self, script: Script) -> list[Shot]:
        shots: list[Shot] = []
        for scene in script.scenes:
            for beat in scene.beats:
                shot_id = f"{scene.id}-{beat.id}-1"
                description = beat.summary
                prompt = beat.summary
                shot = Shot(
                    id=shot_id,
                    scene_id=scene.id,
                    beat_id=beat.id,
                    description=description,
                    prompt=prompt,
                )
                shots.append(shot)
        return shots
