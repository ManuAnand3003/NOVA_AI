# image_generation.py
from diffusers import StableDiffusionXLPipeline
import torch

# Load the SDXL pipeline (first time will download weights)
def get_sdxl_pipeline():
    if torch.cuda.is_available():
        return StableDiffusionXLPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-base-1.0",
            torch_dtype=torch.float16
        ).to("cuda")
    else:
        return StableDiffusionXLPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-base-1.0",
            torch_dtype=torch.float32
        ).to("cpu")

pipeline = None

def generate_image(prompt, output_path="generated_image.png"):
    global pipeline
    if pipeline is None:
        pipeline = get_sdxl_pipeline()
    image = pipeline(prompt).images[0]
    image.save(output_path)
    return output_path
