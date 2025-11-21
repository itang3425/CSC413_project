from diffusers import DiffusionPipeline
import torch

def force_half(model):
    for child in model.children():
        try:
            child.to(torch.float16)
        except:
            pass
        force_half(child)

# Load Stable Diffusion XL Base1.0
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    variant="fp16",
    use_safetensors=True,
    device_map="balanced",
    max_memory={0: "3GiB", "cpu": "16GiB"}
)

# Loading Trained DreamBooth LoRA Weights
pipe.load_lora_weights("mary-ruiliii/genshin-style_character_generator")

force_half(pipe.unet)
force_half(pipe.vae)
force_half(pipe.text_encoder)
force_half(pipe.text_encoder_2)

prompt = "栗黎尔"

# Invoke pipeline to generate image
with torch.inference_mode():
    image = pipe(
        prompt = prompt,
        num_inference_steps=50,
        height=512,
        width=512,
        guidance_scale=7.0,
    ).images[0]
image.save(f"{prompt}.png")
