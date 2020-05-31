#!/usr/local/bin/python3

import requests

url = 'http://10.10.44.2:8080/host-manager/'
auth = ('skyfuck', '8730281lkjlkjdqlksalks')

r = requests.get(url=url, auth=auth)
print(r)
print(r.text)
