#!/usr/local/bin/python3

import requests
import json

url = 'http://10.10.244.246:9200/_search?q=password'
headers = {'Content-Type': 'application/json'}
r = requests.get(url=url, headers=headers)
print(json.dumps(r.json(), indent=4))
