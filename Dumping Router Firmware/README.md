# Dumping Router Firmware

## Task 1 -- Preparation

Ensure tools are installed:
```bash
sudo pip3 install cstruct
sudo git clone https://github.com/sviehb/jefferson
cd jefferson && sudo python setup.py install
```

## Task 2 -- Investigating Firmware
I needed to fix the zip archive to be able to extract the actual firmware image:

```bash
jeffrowell@kali:~/Documents/TryHackMe/Dumping Router Firmware$ zip -F FW_WRT1900ACSV2_2.0.3.201002_prod.zip --out fixed.zip
Fix archive (-F) - assume mostly intact archive
 copying: FW_WRT1900ACSV2_2.0.3.201002_prod.img
jeffrowell@kali:~/Documents/TryHackMe/Dumping Router Firmware$
jeffrowell@kali:~/Documents/TryHackMe/Dumping Router Firmware$ unzip fixed.zip
Archive:  fixed.zip
  inflating: FW_WRT1900ACSV2_2.0.3.201002_prod.img  
  error:  invalid compressed data to inflate
error: invalid zip file with overlapped components (possible zip bomb)
```

### 1 Running strings on the file, what does the first clear text line say?
```bash
jeffrowell@kali:~/Documents/TryHackMe/Dumping Router Firmware$ strings FW_WRT1900ACSV2_2.0.3.201002_prod.img | less
Linksys WRT1900ACS Router
@ #!
!1C "
 -- System halted
Attempting division by 0!
Uncompressing Linux...
decompressor returned an error
```

### 2 Also using strings, what operating system is the device running?
```
Linux
```

### 5 What option within Binwalk will allow us to extract files from the firmware image?
```
-e
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/Dumping Router Firmware$ binwalk -e FW_WRT1900ACSV2_2.0.3.201002_prod.img

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             uImage header, header size: 64 bytes, header CRC: 0xFF40CAEC, created: 2020-04-22 11:07:26, image size: 4229755 bytes, Data Address: 0x8000, Entry Point: 0x8000, data CRC: 0xABEBC439, OS: Linux, CPU: ARM, image type: OS Kernel Image, compression type: none, image name: "Linksys WRT1900ACS Router"
64            0x40            Linux kernel ARM boot executable zImage (little-endian)
2380          0x94C           device tree image (dtb)
17280         0x4380          device tree image (dtb)
22528         0x5800          device tree image (dtb)
26736         0x6870          gzip compressed data, maximum compression, from Unix, last modified: 1970-01-01 00:00:00 (null date)
4214256       0x404DF0        device tree image (dtb)
6291456       0x600000        JFFS2 filesystem, little endian
```

### 6 Now that we know how to extract the contents of the firmware image, what was the first item
extracted?

```
uImage header
```

### 7 What was the creation date?
```
2020-04-22 11:07:26
```

### 8 What is the CRC of the image?
```
0xABEBC439
```

**Note:** The `header CRC` is not the same as the `data CRC`

### 9 What is the image size?
```
4229755 bytes
```

### 10 What architecture does the device run?
```
ARM
```

### 11 Researching the results to question 10, is that true?
```
Yes
```

### 12 Interestingly enough, a copy of the Linux kernel is included. What version is it for?
```
3.10.3
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/Dumping Router Firmware$ cd _FW_WRT1900ACSV2_2.0.3.201002_prod.img.extracted
jeffrowell@kali:~/Documents/TryHackMe/Dumping Router Firmware/_FW_WRT1900ACSV2_2.0.3.201002_prod.img.extracted$ binwalk -e 6870

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
492           0x1EC           device tree image (dtb)
1904228       0x1D0E64        SHA256 hash constants, little endian
4112676       0x3EC124        SHA256 hash constants, little endian
5877920       0x59B0A0        Linux kernel version 3.10.3
6176102       0x5E3D66        Unix path: /var/run/rpcbind.sock
6261498       0x5F8AFA        MPEG transport stream data
6261758       0x5F8BFE        MPEG transport stream data
6902132       0x695174        Unix path: /dev/vc/0
6993884       0x6AB7DC        xz compressed data
7027944       0x6B3CE8        Unix path: /lib/firmware/updates/3.10.39
7194599       0x6DC7E7        Copyright string: "Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>"
7218153       0x6E23E9        Copyright string: "Copyright(c) Pierre Ossman"
7301128       0x6F6808        Unix path: /etc/init.d/ipv6_react_to_ra.sh
7304520       0x6F7548        Neighborly text, "NeighborSolicits6InDatagrams"
7304540       0x6F755C        Neighborly text, "NeighborAdvertisementsorts"
7309086       0x6F871E        Neighborly text, "neighbor %.2x%.2x.%pM lost rename link %s to %s"
7946423       0x7940B7        LZMA compressed data, properties: 0xC0, dictionary size: 0 bytes, uncompressed size: 64 bytes
7970360       0x799E38        ASCII cpio archive (SVR4 with no CRC), file name: "dev", file name length: "0x00000004", file size: "0x00000000"
7970476       0x799EAC        ASCII cpio archive (SVR4 with no CRC), file name: "dev/console", file name length: "0x0000000C", file size: "0x00000000"
7970600       0x799F28        ASCII cpio archive (SVR4 with no CRC), file name: "root", file name length: "0x00000005", file size: "0x00000000"
7970716       0x799F9C        ASCII cpio archive (SVR4 with no CRC), file name: "TRAILER!!!", file name length: "0x0000000B", file size: "0x00000000"
7996352       0x7A03C0        CRC32 polynomial table, little endian
8075823       0x7B3A2F        LZMA compressed data, properties: 0xC0, dictionary size: 0 bytes, uncompressed size: 32 bytes
8227376       0x7D8A30        Copyright string: "Copyright 2000~2013, Marvell International Ltd."
8275455       0x7E45FF        LZMA compressed data, properties: 0xC0, dictionary size: 0 bytes, uncompressed size: 192 bytes
```


## Task 3 - Mounting and Analysis of the Router's Firmware


### 1 Where does linuxrc link to?
```
bin/busybox
```

```bash
jeffrowell@kali:/mnt/jffs2_file$ ls -al
total 7
drwxr-xr-x 17 root root    0 Dec 31  1969 .
drwxr-xr-x  3 root root 4096 May 22 20:25 ..
drwxr-xr-x  2 root root    0 Apr 22 05:10 bin
drwxr-xr-x  2 root root    0 Apr 22 05:44 cgroup
drwxr-xr-x  2 root root    0 Apr 22 05:44 dev
drwxr-xr-x 17 root root    0 Apr 22 05:42 etc
drwxr-xr-x  2 root root    0 Apr 22 05:42 home
drwxr-xr-x  3 root root    0 Apr 22 05:39 JNAP
drwxr-xr-x  2 root root    0 Apr 22 05:44 lib
lrwxrwxrwx  1 root root   11 Apr 22 05:10 linuxrc -> bin/busybox
lrwxrwxrwx  1 root root    8 Apr 22 05:42 mnt -> /tmp/mnt
-r--r--r--  1 root root   20 Apr 22 05:44 .mtoolsrc
lrwxrwxrwx  1 root root    8 Apr 22 05:42 opt -> /tmp/opt
drwxr-xr-x  2 root root    0 Apr 22 05:42 proc
drwxr-xr-x  2 root root    0 Apr 22 05:42 root
drwxr-xr-x  2 root root    0 Apr 22 05:44 sbin
drwxr-xr-x  2 root root    0 Apr 22 05:42 sys
drwxr-xr-x  2 root root    0 Apr 22 05:42 tmp
drwxr-xr-x  2 root root    0 Apr 22 05:36 usr
lrwxrwxrwx  1 root root    8 Apr 22 05:42 var -> /tmp/var
drwxr-xr-x  2 root root    0 Apr 22 05:37 www
```

### 2 What parent folder does mnt, opt, and var link to?
```
/tmp/
```

### 3 What folder would store the routers HTTP server?
```
/www/
```

### 4 The first of the folders that isn't empty is /bin/, where do a majority of the files link to?

```
busybox
```

Busybox is integrated into almost all Linux systems and provides common functionality and commands in the OS, including but not limited to these:

```
[, [[, adjtimex, arping, ash, awk, basename, bunzip2, bzcat, bzip2, cal, cat, chgrp,
chmod, chown, chroot, chvt, clear, cmp, cp, cpio, cut, date, dc, dd, deallocvt, df, dirname,
dmesg, dos2unix, du, dumpkmap, echo, egrep, env, expr, false, fgrep, find, fold, free,
ftpget, ftpput, getopt, grep, gunzip, gzip, head, hexdump, hostid, hostname, httpd, id,
ifconfig, ip, ipcalc, kill, killall, klogd, last, length, ln, loadfont, loadkmap, logger,
logname, logread, losetup, ls, lzmacat, md5sum, mkdir, mkfifo, mknod, mktemp, more, mount,
mt, mv, nameif, nc, netstat, nslookup, od, openvt, patch, pidof, ping, ping6, printf,
ps, pwd, rdate, readlink, realpath, renice, reset, rm, rmdir, route, rpm, rpm2cpio, run-parts,
sed, setkeycodes, sh, sha1sum, sleep, sort, start-stop-daemon, strings, stty, swapoff,
swapon, sync, sysctl, syslogd, tail, tar, tee, telnet, test, tftp, time, top, touch,
tr, traceroute, true, tty, umount, uname, uncompress, uniq, unix2dos, unlzma, unzip,
uptime, usleep, uudecode, uuencode, vi, watch, watchdog, wc, wget, which, who, whoami,
xargs, yes, zcat
```

### 5 Within the bin folder, interestingly enough, what database would be running if the router was online?
Go into `bin` directory and run ls, we see an sqlite3 executable.

```
sqlite3
```

### 6 We can even see the build date of the device. What is the build date?
```bash
jeffrowell@kali:/mnt/jffs2_file/etc$ cat builddate
2020-04-22 11:44
```

### 7 There are even files related to the SSH server on the device. What SSH server does the device run?

In `/etc` we can see two files `dropbear_dss_host_key` and `dropbear_rsa_host_key`

```
dropbear
```

### 8 We can even see the file for the media server, which company developed it?

```bash
jeffrowell@kali:/mnt/jffs2_file/etc$ cat mediaserver.ini
#! Cisco MediaServer ini file ( twonky revision ) / charset UTF-8
#! change settings by editing this file
#! version 5.1.05
```

### 9 Which file within /etc/ contains a list of common Network services and their associated port numbers?

```
services
```

### 10 Which file contains the default system settings?

```
system_defaults
```

### 11 Within the /etc/ folder, what is the version specific firmware version?

```bash
jeffrowell@kali:/mnt/jffs2_file/etc$ cat version
2.0.3.201002
```

### 12 What 3 networks have a folder withint /JNAP/modules?
```
guest_lan,lan,wan
```


```bash
jeffrowell@kali:/mnt/jffs2_file$ cd JNAP/modules/
jeffrowell@kali:/mnt/jffs2_file/JNAP/modules$ ls
core_server.lua                   firewall_server.lua          httpproxy_server.lua           openvpn_server.lua          routerlog_server.lua         ui_server.lua                  wirelessscheduler_server.lua
ddns_server.lua                   firmwareupdate_server.lua    lan                            ownednetwork_server.lua     routermanagement_server.lua  upnpmediaserver_server.lua
devicelist_server.lua             ftpserver_server.lua         locale_server.lua              parentalcontrol_server.lua  router_server.lua            vlantagging_server.lua
diagnostics_server.lua            guest_lan                    macfilter_server.lua           qos_server.lua              routerupnp_server.lua        wan
dynamicportforwarding_server.lua  guestnetworkauth_server.lua  networkconnections_server.lua  reliability_server.lua      smbserver_server.lua         wirelessap_marvell_server.lua
dynamicsession_server.lua         guestnetwork_server.lua      networktraffic_server.lua      routerleds_server.lua       storage_server.lua           wirelessap_server.lua
```
