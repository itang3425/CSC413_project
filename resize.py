from PIL import Image
import os

src = "/home/mary/utm/csc413/CSC413_project/characters"
dst = "/home/mary/utm/csc413/CSC413_project/characters1024"
os.makedirs(dst, exist_ok=True)

for name in os.listdir(src):
    if name.lower().endswith(".png"):
        img = Image.open(os.path.join(src, name))
        img = img.resize((1024, 1024), Image.LANCZOS)
        img.save(os.path.join(dst, name))

