import torch
from diffusers import StableDiffusionXLPipeline, AutoencoderKL

base = "/home/ubuntu/.cache/huggingface/hub/models--stabilityai--stable-diffusion-xl-base-1.0/snapshots/462165984030d82259a11f4367a4eed129e94a7b"

vae = AutoencoderKL.from_pretrained(
    "/home/ubuntu/.cache/huggingface/hub/models--madebyollin--sdxl-vae-fp16-fix/snapshots/207b116dae70ace3637169f1ddd2434b91b3a8cd",
    torch_dtype=torch.float16,
)

pipe = StableDiffusionXLPipeline.from_pretrained(
    base,
    torch_dtype=torch.float16,
    use_safetensors=True,
    add_watermarker=False,
    vae=vae
)
pipe.to("cuda")

print("Loaded OK!")

pipe.load_lora_weights("mary-ruiliii/genshin-style_character_generator", weight_dtype=torch.float16)

# Invoke pipeline to generate image
image = pipe(
    prompt = "Genshin-style 5 stars anime character named Ranni. uses a catalyst. has a cryo vision. tall female body figure. constellation is  Age of the Stars. from Nod-Krai. she is princess of the Carian Royal Family,",
    num_inference_steps=50,
    height=400,
    width=400,
    # guidance_scale=7.0,
).images[0]
image.save("ranni.png")

