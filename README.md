# Genshin-Style Character Generation  
**Controllable image generation using Stable Diffusion + LoRA + Attribute MLP**

This project explores how generative models can create *new* Genshin Impact–style characters while respecting explicit stylistic and semantic constraints. Our system is designed as an artist-assist pipeline, allowing users to specify structured character attributes, such as region, vision, rarity, and body type, and generate visually consistent portraits in the Genshin art style.

The pipeline combines:

- **Stable Diffusion** as the base generator  
- **LoRA fine-tuning** to learn the Genshin art style  
- **An attribute-to-embedding MLP** to encode structured character metadata  
- **A projector** to map CLIP-space offsets into SDXL’s embedding space for conditioning  

This repository includes training code, inference utilities, checkpoints, and a notebook for generating new characters.

---

## Features

- Generate *new* Genshin-style characters from structured attributes  
- LoRA-refined Stable Diffusion for stylistic fidelity  
- Attribute-driven embeddings for semantic control  
- End-to-end inference pipeline (Jupyter notebook included)  
- Trained weights available for reproducibility  

---

# Dataset
Dataset includes 72 official character portraits and structured metadata.
Hugging Face repo: mary-ruiliii/Genshin-character-portrait-image-character-data-all

# Model Overview

### **1. Stable Diffusion (Base Model)**  
We use the following base model:
- `stabilityai/stable-diffusion-xl-base-1.0`

### **2. LoRA Fine-Tuning**  
LoRA is used to adapt SDXL to the Genshin art style without retraining the entire UNet.  
The LoRA model captures stylistic features such as:

- line art  
- soft gradients  
- character portrait composition  

### **3. Attribute MLP Encoder**  
Character attributes are encoded using:

- one-hot vectors for categorical attributes  
- CLIP text embeddings for textual attributes  

The combined vector passes through an MLP that predicts a **semantic offset in CLIP space**.

### **4. Projector**  
Stable Diffusion’s text-conditioning uses a 2048-dimensional embedding.  
We train a projector MLP to map the CLIP-space offset into SDXL’s embedding space.  
The resulting vector replaces the final token in SDXL’s conditioning sequence, enabling semantic control.

---

# Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/genshin-character-generation.git
cd genshin-character-generation
```

### 2. Install dependencies
```bash
pip install -r pipeline_requirements.txt
```

# Run the notebook
Open:
```bash
notebooks/CSC413_pipeline.ipynb
```
Follow the prompts in the cells!
```