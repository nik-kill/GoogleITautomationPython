#!/usr/bin/env python3
from PIL import Image
import  os

path = "supplier-data/images/"
for file in os.listdir(path):
    loc = path+file
    f = file.split('.')
    if f[-1] == "tiff":
      f[-1] = "jpeg"
      file = ".".join(f)
      if Image.open(loc):
        im = Image.open(loc)
        im  = im.resize((600,400))
        im = im.convert("RGB")
        im.save(path+file,"JPEG")
