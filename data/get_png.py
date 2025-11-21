import os
import csv
import requests
from bs4 import BeautifulSoup

BASE = "https://wiki.biligame.com/ys/"
os.makedirs("characters", exist_ok=True)

def download_png(name):
    url = f"{BASE}{name}"
    print("Fetching:", url)

    r = requests.get(url)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")

    # 找 alt 含“立绘” + 含角色名 的 img
    # alt="阿贝多立绘.png"
    selector = f'img[alt*="{name}"][alt*="立绘"]'
    img = soup.select_one(selector)

    if not img:
        print("No artwork img for", name)
        return

    img_url = img.get("src")
    if img_url.startswith("//"):   # 修正 // 开头的 URL
        img_url = "https:" + img_url

    print("Downloading:", img_url)

    png = requests.get(img_url).content
    with open(f"characters/{name}.png", "wb") as f:
        f.write(png)

    print(f"{name} saved.")

# ---- CSV 读取 ----
names = []
with open("names.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        names.append(row["name"].strip())

# ---- 下载 ----
for n in names:
    if n:
        download_png(n)
