from datasets import load_dataset
ds = load_dataset("mary-ruiliii/Genshin-character-portrait-image")
print(ds["train"][0])

