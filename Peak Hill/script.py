#!/usr/bin/python3

import pickle
from natsort import natsorted

data = pickle.load(open('creds.pickle', 'rb'))
sorted_data = natsorted(data)

u = []
p = []
for item in sorted_data:
    if 'user' in item[0]:
        u.append(item[1])
    else:
        p.append(item[1])


print(''.join(u))
print(''.join(p))
