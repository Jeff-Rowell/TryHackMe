# Ignite

## Task 1 - Root It!
```
export IP=10.10.146.17
```

Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Ignite$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-30 18:44 MDT
Nmap scan report for 10.10.146.17
Host is up (0.15s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry
|_/fuel/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Welcome to FUEL CMS

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 53.28 seconds
```

Initial gobuster scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Ignite$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.146.17
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/30 18:44:21 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
[ERROR] 2020/05/30 18:44:48 [!] Get http://10.10.146.17/_old: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/05/30 18:44:49 [!] Get http://10.10.146.17/_pages: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
/0 (Status: 200)
/assets (Status: 301)
/home (Status: 200)
/index (Status: 200)
/index.php (Status: 200)
/offline (Status: 200)
/robots.txt (Status: 200)
/server-status (Status: 403)
===============================================================
2020/05/30 18:48:37 Finished
===============================================================
```

### 1 -- User.txt

### 2 -- Root.txt
