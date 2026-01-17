from ..schemas.story import StoryCreate
from ..services.camera_planner import CameraPlannerService
from ..services.image_generator import ImageGeneratorService
from ..services.story_writer import StoryWriterService
from ..services.storyboarder import StoryboarderService
from ..services.video_renderer import VideoRendererService


class StoryCreationWorkflow:
    def __init__(
        self,
        story_writer: StoryWriterService | None = None,
        storyboarder: StoryboarderService | None = None,
        image_generator: ImageGeneratorService | None = None,
        camera_planner: CameraPlannerService | None = None,
        video_renderer: VideoRendererService | None = None,
    ) -> None:
        self.story_writer = story_writer or StoryWriterService()
        self.storyboarder = storyboarder or StoryboarderService()
        self.image_generator = image_generator or ImageGeneratorService()
        self.camera_planner = camera_planner or CameraPlannerService()
        self.video_renderer = video_renderer or VideoRendererService()

    async def run(self, story: StoryCreate) -> str:
        script = await self.story_writer.generate_script(story)
        shots = await self.storyboarder.generate_shots(script)
        images = await self.image_generator.generate_images(shots)
        camera_plan = await self.camera_planner.plan_camera(shots)
        video_url = await self.video_renderer.render_video(images, camera_plan)
        return video_url
