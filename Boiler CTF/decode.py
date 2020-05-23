#!/usr/bin/python3

import binascii
import base64


robots_string = "079 084 108 105 077 068 089 050 077 071 078 107 079 084 086 104 090 071 086 104 077 122 073 051 089 122 085 048 077 084 103 121 089 109 070 104 078 084 069 049 079 068 081 075"
decoded = [chr(int(n)) for n in robots_string.split()]
b64_decoded = base64.b64decode(''.join(decoded)).decode('utf-8').replace('\n', '')
print(b64_decoded)
