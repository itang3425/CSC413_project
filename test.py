import requests
from bs4 import BeautifulSoup

name = "阿贝多"
url = f"https://wiki.biligame.com/ys/{name}"

r = requests.get(url)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "html.parser")

img = soup.select_one('img[data-file-width][data-file-height]')
print("Found:", img)
