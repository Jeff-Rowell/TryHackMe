#!/usr/local/bin/python3

import base64


with open('b64.txt', 'r') as handle:
    data = handle.read()

while 1:
    try:
        data = base64.b64decode(data)
    except:
        print('Found the flag!')
        print(data.decode('utf-8'))
        break
