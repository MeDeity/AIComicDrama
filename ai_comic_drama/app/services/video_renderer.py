class VideoRendererService:
    async def render_video(self, images: list[str], camera_plan: list[dict]) -> str:
        return "/videos/generated_video.mp4"
