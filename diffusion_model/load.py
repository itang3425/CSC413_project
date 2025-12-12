import torch
from diffusers import StableDiffusionXLPipeline, AutoencoderKL

# epoch100warmup100lr-6antinoodles
# epoch10batch2warmup10
# epoch10warmup100lr
# epoch10warmup100lr-6
# epoch50warmup100lr-5antinoodles
# less_text_batched
# less_text_more_steps
# less_text_more_steps_batch2
# less_text_original
# sd21_genshin_lora_base

# folder="3w_2/checkpoint-20000"

SAVE_DIR=f"output/3w_2_2w/"
# LORA=f"/home/ubuntu/{folder}"
LORA= "mary-ruiliii/genshin-style_character_generator"

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

pipe.load_lora_weights(LORA, weight_dtype=torch.float16)

# Invoke pipeline to generate image
prompt = "A human Genshin-style character, uses a claymore, has a Electro vision, medium male body figure, from Mondstadt"
image = pipe(
    prompt = prompt,
    num_inference_steps=50,
    height=512,
    width=512,
    # guidance_scale=7.0,
).images[0]
filename=SAVE_DIR+f"{prompt}.png"
image.save(filename)

# # prompt = "A short anime female from Genshin. uses a polearm. has a Pyro vision."
# prompt = "A human Genshin-style character. uses a polearm. has a Pyro vision. short female body figure."
# image = pipe(
#     prompt = prompt,
#     num_inference_steps=50,
#     height=400,
#     width=400,
#     # guidance_scale=7.0,
# ).images[0]
# filename=SAVE_DIR+f"{prompt}.png"
# image.save(filename)

# # prompt = "A tall anime female from Genshin. uses a sword. has a hydro vision."
# prompt = "A human Genshin-style character. uses a sword. has a hydro vision. tall female body figure."
# image = pipe(
#     prompt = prompt,
#     num_inference_steps=50,
#     height=400,
#     width=400,
#     # guidance_scale=7.0,
# ).images[0]
# filename=SAVE_DIR+f"{prompt}.png"
# image.save(filename)

# # prompt = "A short anime female from Genshin. uses a claymore. has a Electro  vision."
# prompt = "A human Genshin-style character. uses a claymore. has a Electro vision. short female body figure."
# image = pipe(
#     prompt = prompt,
#     num_inference_steps=50,
#     height=400,
#     width=400,
#     # guidance_scale=7.0,
# ).images[0]
# filename=SAVE_DIR+f"{prompt}.png"
# image.save(filename)


