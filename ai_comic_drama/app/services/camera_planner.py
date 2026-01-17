from ..domain.models import Shot


class CameraPlannerService:
    async def plan_camera(self, shots: list[Shot]) -> list[dict]:
        plan: list[dict] = []
        for index, shot in enumerate(shots):
            plan.append(
                {
                    "shot_id": shot.id,
                    "order": index,
                    "duration": 3.0,
                    "movement": "static",
                }
            )
        return plan
