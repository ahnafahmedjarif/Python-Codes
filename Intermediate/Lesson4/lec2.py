""" Let's download images with python """

import requests

img_url = "https://banner2.cleanpng.com/20180412/kye/avffc0w7m.webp"

r = requests.get(img_url)

with open("python.png", "wb") as f:
    f.write(r.content)