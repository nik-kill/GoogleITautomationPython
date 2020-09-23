#! /usr/bin/env python3

import os
import requests

filePath = "supplier-data/descriptions/"
for file in os.listdir(filePath):
    data = {}
    with open(filePath+file,'r') as f:
        lines = f.readlines()
        data["name"] = lines[0].strip()
        data["weight"] = int((lines[1].strip().split())[0])
        data["description"] = lines[2].strip()
        fr = file.split('.')
        fr[-1] = "jpeg"
        img = ".".join(fr)
        data["image_name"] = img
    print(data)
    response = requests.post("http://127.0.0.1:80/fruits/", json=data)
    print(response,response.status_code,)
