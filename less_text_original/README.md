---
base_model: stabilityai/stable-diffusion-xl-base-1.0
library_name: diffusers
license: creativeml-openrail-m
inference: true
tags:
- stable-diffusion-xl
- stable-diffusion-xl-diffusers
- text-to-image
- diffusers
- diffusers-training
- lora
- stable-diffusion-xl
- stable-diffusion-xl-diffusers
- text-to-image
- diffusers
- diffusers-training
- lora
---

<!-- This model card has been generated automatically according to the information the training script had access to. You
should probably proofread and complete it, then remove this comment. -->


# LoRA text2image fine-tuning - mary-ruiliii/genshin-style_character_generator

These are LoRA adaption weights for stabilityai/stable-diffusion-xl-base-1.0. The weights were fine-tuned on the mary-ruiliii/Genshin-character-portrait-image dataset. You can find some example images in the following. 



LoRA for the text encoder was enabled: False.

Special VAE used for training: madebyollin/sdxl-vae-fp16-fix.


## Intended uses & limitations

#### How to use

```python
# TODO: add an example code snippet for running this diffusion pipeline
```

#### Limitations and bias

[TODO: provide examples of latent issues and potential remediations]

## Training details

[TODO: describe the data used to train the model]