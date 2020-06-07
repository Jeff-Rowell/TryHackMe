# Anthem
```
export IP=10.10.50.108
```




## Task 1 - Website Analysis
### 1 - Let's run nmap and check what ports are open.
```bash
jeffrowell@kali:~/Documents/TryHackMe/Anthem$ nmap -sC -sV -Pn -oN nmap/inital $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-06 22:29 MDT
Nmap scan report for 10.10.50.108
Host is up (0.13s latency).
Not shown: 995 closed ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info:
|   Target_Name: WIN-LU09299160F
|   NetBIOS_Domain_Name: WIN-LU09299160F
|   NetBIOS_Computer_Name: WIN-LU09299160F
|   DNS_Domain_Name: WIN-LU09299160F
|   DNS_Computer_Name: WIN-LU09299160F
|   Product_Version: 10.0.17763
|_  System_Time: 2020-06-07T04:28:15+00:00
| ssl-cert: Subject: commonName=WIN-LU09299160F
| Not valid before: 2020-04-04T22:56:38
|_Not valid after:  2020-10-04T22:56:38
|_ssl-date: 2020-06-07T04:29:29+00:00; -1m50s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -1m50s, deviation: 0s, median: -1m50s
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2020-06-07T04:28:20
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 111.05 seconds
```

Also, running a `gobuster` scan gives us some potentially useful enumeration of
the web pages:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Anthem$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.50.108
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/06/06 22:32:07 Starting gobuster
===============================================================
/search (Status: 200)
/blog (Status: 200)
/sitemap (Status: 200)
/rss (Status: 200)
/archive (Status: 301)
/categories (Status: 200)
/authors (Status: 200)
/Search (Status: 200)
/tags (Status: 200)
/install (Status: 302)
/RSS (Status: 200)
/Blog (Status: 200)
/Archive (Status: 301)
/SiteMap (Status: 200)
/siteMap (Status: 200)
/INSTALL (Status: 302)
/Sitemap (Status: 200)
/1073 (Status: 200)
/Rss (Status: 200)
/Categories (Status: 200)
/1074 (Status: 301)
/1078 (Status: 200)
/Authors (Status: 200)
/1075 (Status: 200)
/1079 (Status: 200)
/1076 (Status: 200)
Progress: 12198 / 220561 (5.53%)^C
[!] Keyboard interrupt detected, terminating.
===============================================================
2020/06/06 23:10:00 Finished
===============================================================
```

### 2 - What port is for the web server?
```
80
```

### 3 - What port is for remote desktop service?
```
3389
```

### 4 - What is a possible password in one of the pages web crawlers check for?
In the `robots.txt` file we see a couple of interesting directories, but we also find
a string that looks like it could potentially be a password.

![robots](https://user-images.githubusercontent.com/32188816/83960419-df40d800-a845-11ea-96cf-e1b5e6008be9.png)

```
UmbracoIsTheBest!
```

### 5 - What CMS is the website using?
```
umbraco
```

### 6 - What is the domain of the website?
```
anthem.com
```

### 7 - What's the name of the Administrator
Looking through the blog posts linked in the home page, when looking at the post
we notice an interesting note about the admin and a poem:

![poem](https://user-images.githubusercontent.com/32188816/83960800-2c26ad80-a84a-11ea-9f21-5b7ccdf9fc81.png)

When tossing this poem into Google we find that the poem references `Solomon Grundy`, who
is the administrator:

![admin](https://user-images.githubusercontent.com/32188816/83960798-29c45380-a84a-11ea-8104-4d4b9ba4db51.png)


### 8 - Can we find find the email address of the administrator?
Looking at the `/rss` endpoint found from our `gobuster` scan, we can enumerate all of
these directories to see if there is any useful information, and indeed we found an email
that when used in conjunction with the Administrator's name, we can guess the email.

![email_hint](https://user-images.githubusercontent.com/32188816/83960704-2b414c00-a849-11ea-89fc-e969200900ca.png)

Since the other email is `JD@anthem.com`, we can safely assume that the first to
letters are initials to a name, so the admin email would be:

```
SG@anthem.com
```




## Task 2 - Spot the Flags
### 1 - What is flag 1?
On the endpoint `/archive/we-are-hiring` were we cound the other person's email earlier, we
can also find the first flag hidden in a meta tag:

![flag1](https://user-images.githubusercontent.com/32188816/83961346-56c73500-a84f-11ea-8cb7-d19797f23d48.png)

```
THM{L0L_WH0_US3S_M3T4}
```


### 2 - What is flag 2?
As we continue looking through the website, on the home page there are some links
to read the articles that brings us to other pages, we will look at that later.
If we view the HTML source of the page, we find the second flag:

![flag2](https://user-images.githubusercontent.com/32188816/83960598-a86bc180-a847-11ea-9f21-d759ab2aac2d.png)


```
THM{G!t_G00D}
```


### 3 - What is flag 3?
Browsing through the website we stumble upon the `/authors/jane-doe/` endpoint,
which contains another flag:


![flag3](https://user-images.githubusercontent.com/32188816/83960495-9b9a9e00-a846-11ea-894e-17daa321d6d0.png)



```
THM{L0L_WH0_D15}
```

### 4 - What is flag 4?
Inspecting the elements on all of the pages we are able to stumble upon the
fourth and final flag on the `/archive/a-cheers-to-our-it-department/` endpoint:


![flag4](https://user-images.githubusercontent.com/32188816/83960943-b3c0ec00-a84b-11ea-9f0b-e43e203c49db.png)



```
THM{AN0TH3R_M3TA}
```






## Task 3 - Final Stage
### 1 - Let's figure out the username and password to log in to the box.(The box is not on a domain)
We can log in with a guess of the username and the actual password we found earlier `sgrundy:UmbracoIsTheBest!`:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Anthem$ rdesktop -u SG -p 'UmbracoIsTheBest!' $IP
Autoselecting keyboard map 'en-us' from locale
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.
Failed to initialize NLA, do you have correct Kerberos TGT initialized ?
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.
Connection established using SSL.
```


### 2 - Gain initial access to the machine, what is the contents of user.txt?
The `user.txt` file is found on the desktop once we first log in:


![user txt](https://user-images.githubusercontent.com/32188816/83961711-07830380-a853-11ea-94c5-443a43eac7f1.png)


```
THM{N00T_NO0T}
```


### 3 - Can we spot the admin password?
Looking around in the `C:\` drive, we find a `backups` directory and inside there is
a `restore.txt` file that currently has no permissions set so we can't view it. However,
since there are no permissions set we can easily change the permissions so that we
can view the file and see what is inside. Upon changing the permissions and opening
the file, we get the admin password:


![adminpass](https://user-images.githubusercontent.com/32188816/83962008-567e6800-a856-11ea-8a69-831cc51b701a.png)


### 4 - Escalate your privileges to root, what is the contents of root.txt?
Now that we have the Administrator password we can run the `cmd` prompt as
Administrator:

```bash
Microsoft Windows [Version 10.0.17763.1131]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
win-lu09299160f\administrator
```

Now all we need to do is look in the Administrator home directory `C:\Users\Administrator\Desktop`,
and view the file:

```bash
C:\Users\Administrator\Desktop>more root.txt
THM{Y0U_4R3_1337}
```
