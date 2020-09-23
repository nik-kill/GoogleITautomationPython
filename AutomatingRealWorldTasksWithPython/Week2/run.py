#! /usr/bin/env python3

import os
import requests

feedbackPath = "/data/feedback/"
for file in os.listdir(feedbackPath):
    data = {}
    with open(feedbackPath+file,'r') as f:
        lines = f.readlines()
        data["title"] = lines[0].strip()
        data["name"] = lines[1].strip()
        data["date"] = lines[2].strip()
        data["feed"] = lines[3].strip()
    print(data)
    response = requests.post("http://35.222.93.0/feedback/", json=data)
    print(response,response.status_code,)

