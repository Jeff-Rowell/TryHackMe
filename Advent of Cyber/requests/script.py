#!/usr/bin/python3

import requests


c = ''
next = []
value = []
url = 'http://10.10.169.100:3000/'

while 1:
    r_json = requests.get(url + c).json()
    c = r_json['next']
    if c == 'end':
        break
    value.append(r_json['value'])


print('Flag is ' + ''.join(value))
