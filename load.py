from diffusers import DiffusionPipeline
import torch

# Load Stable Diffusion XL Base1.0
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    dtype=torch.float16,
    variant="fp16",
    use_safetensors=True
)
pipe.to("cuda")

# Optional CPU offloading to save some GPU Memory
pipe.enable_model_cpu_offload()

# Loading Trained DreamBooth LoRA Weights
pipe.load_lora_weights("mary-ruiliii/genshin-style_character_generator", weight_dtype=torch.float16)

# Invoke pipeline to generate image
image = pipe(
    prompt = "genshen-style character",
    num_inference_steps=50,
    height=400,
    width=400,
    # guidance_scale=7.0,
).images[0]
image.save("test400.png")

