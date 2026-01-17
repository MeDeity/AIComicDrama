from ..domain.models import Shot


class ImageGeneratorService:
    async def generate_images(self, shots: list[Shot]) -> list[str]:
        images: list[str] = []
        for shot in shots:
            images.append(f"/generated_images/{shot.id}.png")
        return images
