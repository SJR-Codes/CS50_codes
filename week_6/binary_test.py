"""
* CS50P Problem Set 6
* Notes for week 6
* by Samu Reinikainen 27.07.2022
"""

import sys
from PIL import Image

images = []

#remember slicing
for arg in sys.argv.[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif",
    save_all=True,
    append_images[images[1]],
    duration=200,
    loop=0,
)