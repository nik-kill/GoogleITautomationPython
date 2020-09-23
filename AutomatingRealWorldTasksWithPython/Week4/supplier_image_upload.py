#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
path = "supplier-data/images/"
for file in os.listdir(path):
    f = file.split('.')
    if f[-1]=="jpeg":
      with open(path+file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
