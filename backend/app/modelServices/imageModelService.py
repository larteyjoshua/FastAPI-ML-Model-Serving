from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO


def generateImage(textPrompt: str):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")

    # prompt = "a photo of an astronaut riding a horse on mars"
    image = pipe(textPrompt).images[0]  
    image.save("astronaut_rides_horse.png")
    generatedImage = BytesIO()
    image.save(generatedImage, "PNG")
    return generatedImage.seek(0)
    
        
    