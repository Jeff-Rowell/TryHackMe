# CTF 100

## Stage 1

### Flag 1
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 3333
***************************
*   100 Flags challenge   *
***************************
Welcome to the THM point grabbing challenge!
The task is simple, find the flag and get the point
It can be hard or easy, IDK
To start the challenge, I need your address. So that I can send it to you.
> 10.8.21.42
Well done! Please take your first flag
flag 1: you_got_a_message
5 open ports is now opened for you! Hint: 4 digits and start with 3
Good luck!
```

### Flag 2
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 3343
Flag 2 challenge
Crack the following code
Guvf_vf_prnfre_pvcure
> This_is_ceaser_cipher

Good job!
flag 2: qt8pm59jh5r49uqdwfw2
Just some numbering: 8989
```

### Flag 3
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 3353
Flag 3 challenge
Crack the following code
Kxydrob_mokcob_mszrob
> Another_ceaser_cipher

Good job!
flag 3: 5wdtc7jzk33qjauh5gxm
Just some numbering: 7431
```

### Flag 4
Vignere cipher with `where` as the key:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 3363
Flag 4 challenge
Crack the following code
where is the key
Ez_me_jnvrk_sb_fslv_afij
> Is_in_front_of_your_eyes

Good job!
flag 4: sm8jvu8jxu7dz6s7qmsp
Just some numbering: 5667
```

### Flag 5
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 3373
Flag 5 challenge
Crack the following code
-- --- .-. Ook . / -.-. --- -.. . / -Ook . . .--. / -Ook --- --- .--.
> MORSE CODE BEEP BOOP

Good job!
flag 5: 2p3363hrava9fbq296ca
Just some numbering: 9332
```

### Flag 6
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 3383
Flag 6 challenge
Crack the following code
59 6f 75 20 67 65 74 20 68 65 78 2d 65 64
> You get hex-ed

Good job!
flag 6: skuj9359mqdm6sv8d8z6
Just some numbering: 3331
```

### Flag 7
Using the ports from the previous responses:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 9999
***************************
*   Port knocking input   *
***************************
Hi user, please enter the port sequence
The format is (can be more than 4): PORT PORT PORT PORT
> 8989 7431 5667 9332 3331
Something happen
Good luck!
```

Nmap scan again to see if more ports opened. From the hint we know the range is in `4000-5000`:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nmap -p4000-5000 -Pn -T5 $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-13 14:14 MDT
Nmap scan report for 10.10.127.16
Host is up (0.16s latency).
Not shown: 1000 filtered ports
PORT     STATE SERVICE
4000/tcp open  remoteanything

Nmap done: 1 IP address (1 host up) scanned in 31.44 seconds
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 4000
Congratulation! You have captured all the flag
Please go home, nothing to see here
Type 'exit' and leave this place

Seriously? Nothing to see here!
GET LOST!

Please I beg you, LEAVE!

Oh my fking god, take it, JUST TAKE IT
flag 7: zmht7gg3q3ft7cmc942n
Please leave, thank you

PORT PORT PORT PORT PORT
```

### Flag 8
Nmap scan again to see if more openned up:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nmap -p4000-5000 -Pn -T5 $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-13 14:16 MDT
Nmap scan report for 10.10.127.16
Host is up (0.16s latency).
Not shown: 995 filtered ports
PORT     STATE SERVICE
4000/tcp open  remoteanything
4001/tcp open  newoak
4002/tcp open  mlchat-proxy
4003/tcp open  pxc-splr-ft
4004/tcp open  pxc-roid
4005/tcp open  pxc-pin

Nmap done: 1 IP address (1 host up) scanned in 9.56 seconds
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 4001
Flag 8 challenge
Crack the following code
QSBjb21tb24gYmFzZQ==
> A common base

Good job!
flag 8: dmm32qvfkfwm6yjnw46k
Same old stuff: 10113
```

### Flag 9
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 4002
Flag 9 challenge
Crack the following code
KRUGS4ZANFZSAYJAONWWC3DMMVZCAYTBONSQ====
> This is a smaller base

Good job!
flag 9: fuf8mx74nph26f69mr97
Same old stuff: 10415
```

### Flag 10
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 4003
Flag 10 challenge
Crack the following code
4UFrmghikrDhdg9avkV9avpg4uHQmhvUf7GgRoCo
> Look like a brother to base64

Good job!
flag 10: hud9bm8yc37md5b7t7mn
Same old stuff: 21033
```

### Flag 11
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 4004
Flag 11 challenge
Crack the following code
9lG&`+@/pn8P(%7BOPpi@ru:&
> More ASCII character

Good job!
flag 11: 4xm43r2wajrsrbm4775d
Same old stuff: 35555
```

### Flag 12
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 4005
Flag 12 challenge
Crack the following code
Erzg,W]@7RqSkb9jPD<:vz3B
> More and More ASCII

Good job!
flag 12: qtfvbd7gbvyg9gww5jwj
Same old stuff: 25637
```

### Flag 13
Now put the ports backwards into the service on `9999`:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 9999
***************************
*   Port knocking input   *
***************************
Hi user, please enter the port sequence
The format is (can be more than 4): PORT PORT PORT PORT
> 25637 35555 21033 10415 10113
Something happen
Good luck!
```

Nmap scan again the port range `6000-6999` from the hint:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nmap -p6000-6999 -Pn -T5 $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-13 14:48 MDT
Nmap scan report for 10.10.127.16
Host is up (0.16s latency).
Not shown: 999 filtered ports
PORT     STATE SERVICE
6000/tcp open  X11

Nmap done: 1 IP address (1 host up) scanned in 50.35 seconds
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 6000
Congratulation on getting this far
You are a worthy challenger
5 more gates are opened for you
Take this as your reward
flag 13: aehg24vwn5yyc8jz4tv5
```

### Flag 14
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 6010
Flag 14 challenge
Crack the following code
pi pi pi pi pi pi pi pi pi pi pika pipi pi pipi pi pi pi pipi pi pi pi pi pi pi pi pipi pi pi pi pi pi pi pi pi pi pi pichu pichu pichu pichu ka chu pipi pipi pipi pi pi pi pi pi pi pi pi pi pi pikachu pipi pi pi pi pi pi pikachu pi pi pikachu ka ka ka ka ka ka ka ka ka ka pikachu pi pi pikachu pi pi pi pi pi pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu pichu pichu pi pi pikachu pipi pipi ka ka ka ka ka ka ka ka ka ka ka ka pikachu pi pi pi pi pi pi pi pi pi pi pikachu pichu pichu pikachu pipi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu pichu pikachu pipi pipi pi pikachu pi pi pi pi pi pikachu ka ka ka ka ka ka ka ka ka pikachu pichu pi pi pi pi pikachu pichu pikachu pipi pipi ka pikachu pichu pi pikachu pichu pikachu pipi ka pikachu pipi ka ka ka pikachu pichu pikachu ka ka pikachu pipi pi pi pi pi pi pi pi pi pikachu ka ka pikachu pichu pi pi pi pi pi pi pikachu ka ka ka ka ka ka pikachu pichu pikachu pipi pipi ka ka pikachu ka pikachu ka ka ka ka pikachu pichu pi pi pikachu pipi pi pi pikachu pi pi pikachu ka pikachu
> Pikachu is a type of electric pokemon

Good job!
flag 14: k2phhw85emq3v4njj5g6
You know the drill: 31031
```

### Flag 15
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 6020
Flag 15 challenge
Crack the following code
000000000000000000000000000000110010000010000000000010000000000000000000000010000000000000000000000000000000011011011011001111010010010000000000000000000000000000000000000000000100010000000000000100000100000000000000000000000000000000100011011000000100010010001001001001001001001001001001100000000000000000000000000000000100011011100010010001001001001001100000100000000000000000100011011100010000000000000000000000000000000000000000100011100010000100000000000000000000000100000000000000000100001001001001001001001001001001001001001100010001001100000000000000000000000100
> This is not a binary

Good job!
flag 15: qtfvbd7gbvyg9gww5jwj
You know the drill: 50010
```

### Flag 16
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 6030
Flag 16 challenge
Crack the following code
111111111100100010101011101011111110101111111111011011011011000001101001001000101001011111111111001010111001010000000000000000000000001010011011110010100100100000000000000000000000000000000010101111111111111001010000000000000000000000000000000001010011011001010010010111111111111111001010000000000001010000001010001010000001010
> Fork and spoon

Good job!
flag 16: ckjug6sj88xuajfku72h
You know the drill: 7968
```

### Flag 17
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 6040
Flag 17 challenge
Crack the following code
----------]<-<---<-------<---------->>>>+[<<<------------,<-,-----------------,+++++++++++++++++,-------------,-,++++++++++++++,>>--,<<----------,+++++++++,>>,<<++++,----------------,>---------------,--------,<++++,>+++,<-------,>+++,--------,
> Reverse of brainfuck

Good job!
flag 17: x4xhrqx3ywzyx2jmgc5j
You know the drill: 20010
```

### Flag 18
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 6050
Flag 18 challenge
Crack the following code
eeeeeeeeeepaeaeeeaeeeeeeeaeeeeeeeeeeccccisaaaeeeejaeeeeeeeeeeeeeeeeejiijejcceejaaiiiiiiiijiiijeejiiiiiijccjaaeeeeeeeeeeeeeeejiiiiiiiiiiiijiiijccjaaiiijeeeeeeeeeeeeeeeejiiiiiiiiiiiiiiiiijeeeeeeeejeeeeejiiiiiiiijeeeeeeeeeeeeeeejiiiiiiiiiiiiiiiiiijeeeeeeeej
> Just like the brainfuck

Good job!
flag 18: kr2t9qcgt4ht9h6j5ydp
You know the drill: 6100
```

### Port to stage 2
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 9999
***************************
*   Port knocking input   *
***************************
Hi user, please enter the port sequence
The format is (can be more than 4): PORT PORT PORT PORT
> 31031 50010 7968 20010 6100
Save this sequence, you need it for stage 2
That's all for the challenge
Thank you for your participation
```

```
31031 50010 7968 20010 6100
```



## Stage 2

### Flag 19
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 9999
***************************
*   Port knocking input   *
***************************
Hi user, please enter the port sequence
The format is (can be more than 4): PORT PORT PORT PORT
> 31031 50010 7968 20010 6100
Something happen
Good luck!
```

Quick nmap scan to see what is open:
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nmap -Pn -T5 $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-13 15:25 MDT
Nmap scan report for 10.10.151.243
Host is up (0.16s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE
1111/tcp open  lmsocialserver
9999/tcp open  abyss

Nmap done: 1 IP address (1 host up) scanned in 31.44 seconds
```

Looking at the port `1111/tcp` turns out to be an HTTP server, and on the webpage we are given a bunch of text with `alert!` over and over.

Using a notepad editor we can replace `alert!` with nothing and find the flag

```
j4dnbdewgwgy5r7kjtnd
```

### Flag 20

`/robots.txt` shows a couple of hidden directories, on containing flag 20:

```
Disallow:
/
/This_is_easy
/flag_20_2re645f4n2ex85g3b2fw
```

### Flag 21
From running `gobuster` we found a directory named `/hidden`, and viewing the source we can see flag 21:

```html
<p>Not bad, you found the hidden directory</p>
<!--Always check the comment-->
<!--flag 21: 5tjdmdawe35dsacmunqa-->
```

### Flag 22

From running `gobuster` we found the `/capture` endpoint:

```html
<p>Not bad, you found another flag</p>
<p>flag22: 35x7axg8xd7n4geyxp2t</p>
UHJvY2VlZCB3aXRoIHRoZSBuZXh0IGNoYWx<style></style>QMFZXG53POJSDUIDUNBSV6ZLOMQ======
```

Making note of the bases and how they are divided. We know that base32 is all caps, but the first part of the string looks like it could be base64.

### Flag 23
Once more, gobuster found a `/godzilla` directory which has flag 23:

```
Another one, you are smart ^^

flag23: 5vttxb43qpsh9ctbfzrd
eW91IGFyZSB0b28gc21hcnQsIGRvbid0IHlvdSB0aGluay4=
```

Looking at the source code of the page shows something interesting, it looks like there is another hidden base string, and it is divided in an interesting way:

```html
<p>Another one, you are smart ^^</p>
<p>flag23: 5vttxb43qpsh9ctbfzrd</p>
eW91IGFyZSB0b28gc21hcnQsIGRvbid0IHlvdSB0aGluay4=<br><br><br><br><br>
<font color="white">KVZWK4TOMFWWKORAM5QW2ZLPOZSXEID<style></style>sZW5nZTogODc2OSwgOTQ1MywgNjEyMywgOTkxMy4=</font>

<script language="JavaScript">
  window.onload = function() {
    document.addEventListener("contextmenu", function(e){
      e.preventDefault();
    }, false);
    document.addEventListener("keydown", function(e) {
    //document.onkeydown = function(e) {
      // "I" key
      if (e.ctrlKey && e.shiftKey && e.keyCode == 73) {
        disabledEvent(e);
      }
      // "J" key
      if (e.ctrlKey && e.shiftKey && e.keyCode == 74) {
        disabledEvent(e);
      }
      // "S" key + macOS
      if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
        disabledEvent(e);
      }
      // "U" key
      if (e.ctrlKey && e.keyCode == 85) {
        disabledEvent(e);
      }
      // "F12" key
      if (event.keyCode == 123 || event.keyCode == 18) {
        disabledEvent(e);
      }
    }, false);
    function disabledEvent(e){
      if (e.stopPropagation){
        e.stopPropagation();
      } else if (window.event){
        window.event.cancelBubble = true;
      }
      e.preventDefault();
      return false;
    }
  };
</script>
```

Decoding the base strings individually gives the following info:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ echo 'eW91IGFyZSB0b28gc21hcnQsIGRvbid0IHlvdSB0aGluay4=' | base64 -d
you are too smart, don't you think.
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ echo 'UHJvY2VlZCB3aXRoIHRoZSBuZXh0IGNoYWxsZW5nZTogODc2OSwgOTQ1MywgNjEyMywgOTkxMy4=' | base64 -d
Proceed with the next challenge: 8769, 9453, 6123, 9913.
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ echo 'KVZWK4TOMFWWKORAM5QW2ZLPOZSXEIDQMFZXG53POJSDUIDUNBSV6ZLOMQ======' | base32 -d
Username: gameover password: the_end
```

So now we have the port sequnce to give to the server on `9999/tcp`:

```
8769 9453 6123 9913
```

### Flag 24
Give the port sequence to port `9999/tcp`:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 9999
***************************
*   Port knocking input   *
***************************
Hi user, please enter the port sequence
The format is (can be more than 4): PORT PORT PORT PORT
> 8769 9453 6123 9913
Something happen
Good luck!
```


Run another quick nmap scan:
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nmap -Pn -T5 $IP
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-13 16:20 MDT
Nmap scan report for 10.10.151.243
Host is up (0.16s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE
110/tcp  open  pop3
1111/tcp open  lmsocialserver
9999/tcp open  abyss

Nmap done: 1 IP address (1 host up) scanned in 10.07 second
```

Now we see that POP3 port is open. And we also have the credentials to the POP3 mail server:
```
Username: gameover password: the_end
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 110
+OK Dovecot (Ubuntu) ready.
USER gameover
+OK
PASS the_end
+OK Logged in.
list
+OK 4 messages:
1 1010
2 7189
3 875
4 877
```

Now we can read mail messages:

```bash
RETR 1
+OK 1010 octets
Return-Path: <gameover@ctf100.com>
X-Original-To: gameover@ctfmain
Delivered-To: gameover@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id 601A1828E8
	for <gameover@ctfmain>; Mon,  7 Oct 2019 12:33:52 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user gameover)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:33:52 -0000
Message-ID: <1063a6d5ad70050be0771dbfe93280a7.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:33:52 -0000
Subject: You found me
From: gameover@ctf100.com
To: gameover@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

Congratulation on finding this port, This is a pop3

Take this flag as a token of celebration.

flag 24: phzppg952hsxaarspjfs

>From now on, thing will getting weirder and weirder. Good luck ^^
```


### Flag 25
Reading the next email gives another esoteric language:

```bash
RETR 2
+OK 7189 octets
Return-Path: <gameover@ctf100.com>
X-Original-To: gameover@ctfmain
Delivered-To: gameover@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id 4EB57828E8
	for <gameover@ctfmain>; Mon,  7 Oct 2019 12:41:22 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user gameover)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:41:22 -0000
Message-ID: <92b46b2d9318f438d18857a060dbdef5.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:41:22 -0000
Subject: A beautiful tree
From: gameover@ctf100.com
To: gameover@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... ...! ...? .... ...? .... .... .... ...? .... ....
...... .... .... .... .... ...? .... .... .... .... .... .... .... .... ....
...... .... .... .... .... .... ...? .... .... .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... ...? .... ...?
...... ...? .... ...? .... ...! ...! ...? ...! .... ...? .... ...? .... ...?
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... ...! .... .... ...? ...! ...! ...! ...! ...! ...! ...! ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... ...! .... ...? .... ...? .... .... .... .... ....
.....! .... .... ...? .... ...? ...! ...! ...! ...! ...! .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... ...! .... ...? .... ...? .... ...! .... .... ...? .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... ...! .... ...? .... ...! .... .... ...? .... .... ...! ....
...... .... .... .... .... .... ...! .... ...! ...! ...! ...! ...! ...! ...!
.....! ...! .... .... ...? .... .... .... .... ...! .... ...! ...! ...! ....
.....? .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... ...! .... ...! ...! ...! ...! ...! ...! ...! .... .... ...?
...... .... ...! .... ...? .... .... .... .... .... .... .... .... .... ....
...... .... .... ...! .... ...? .... ...! .... .... ...? .... ...? ...! ...!
.....! .... ...! ...! ...! ...! ...! .... ...? .... ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! .... ...! .... ...? ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... ...! ....
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ....
...... ...? ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! .... .... ...? ...! ...! ...!
.....! ...! ...! ...! .... ...! ...! ...! .... ...? .... ...? .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... ...! .... ....
.....? .... ...? .... .... .... .... .... .... .... .... .... .... .... ....
.....! .... ...? .... ...? .... ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! .... .... ...? .... ...? .... .... .... ....
...... .... .... .... .... .... ...! .... ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ....
...... .... .... .... .... .... .... .... .... .... .... .... ...! .... ...?
...... ...? .... ...! .... .... ...? .... ...? ...! ...! ...! .... ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! .... .... .... ...! .... .... ....
...... .... .... .... .... .... .... .... ...! .... ...! ...! ...! ...! ...!
.....! ...! .... ...? .... ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! .... ...? .... ...! .... .... ...? .... ...? ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! .... .... .... .... .... .... .... .... ....
...... .... .... .... ...! .... ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ....
...... .... .... .... .... .... .... .... .... .... .... .... ...! .... ...?
...... ...? .... ...! .... .... ...? ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! .... .... .... .... .... .... .... ...! .... .... ....
...... .... .... .... .... .... .... .... ...! .... ...? .... ...! .... ....
.....? .... ...? .... .... .... .... .... .... .... .... .... .... .... ....
...... .... ...! .... .... .... .... .... .... .... .... .... .... .... ...!
...... ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! .... .... .... .... .... .... .... ...! .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... ...! ....
...... .... ...! .... ...? .... ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! .... ...! .... .... ...? ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! .... .... .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... ...! .... ...? .... .... .... ...! .... .... ...?
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! .... ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... ...! .... ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ....
.....! ...! ...! ...! ...! ...! ...! ...! ...! .... ...! ...! ...! ...! ...!
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... .... .... .... ....
...... .... .... .... .... .... .... .... .... .... .... ...! .... ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...! ...!
.....! ...! ...! .... ...! ...! ...! ...! ...! ...! ...! ....
```

This esoteric language is Ook, but it is slightly compromised. There are some extra dots that need to be removed, and each sequence of `...` needs to be replaced with `Ook`. The corrected text should look like:

```
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook. Ook? Ook. Ook. Ook. Ook? Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook?
Ook. Ook? Ook. Ook? Ook. Ook! Ook! Ook? Ook! Ook. Ook? Ook. Ook? Ook. Ook?
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook! Ook. Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook? Ook. Ook. Ook. Ook. Ook.
Ook! Ook. Ook. Ook? Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook! Ook. Ook? Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook. Ook! Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook.
Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook?
Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook! Ook!
Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook! Ook. Ook? Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook.
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook? Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook. Ook! Ook! Ook! Ook. Ook? Ook. Ook? Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook.
Ook? Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook! Ook. Ook? Ook. Ook? Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook? Ook. Ook? Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook?
Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook! Ook! Ook! Ook. Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook! Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook. Ook? Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook?
Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook! Ook. Ook.
Ook? Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook!
Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook.
Ook. Ook. Ook! Ook. Ook? Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook! Ook. Ook. Ook? Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook! Ook. Ook. Ook?
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook! Ook! Ook! Ook! Ook!
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
Ook! Ook! Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
```

Decoding teh corrected text gives us the flag:

```
Oak is a beautiful tree. Don't you think? flag 25: nsknvw33cx4kfzhdbveb
```

### Flag 26
Reading the third mail message gives us:

```bash
RETR 3
+OK 875 octets
Return-Path: <gameover@ctf100.com>
X-Original-To: gameover@ctfmain
Delivered-To: gameover@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id 2148B828E8
	for <gameover@ctfmain>; Mon,  7 Oct 2019 12:42:35 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user gameover)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:42:35 -0000
Message-ID: <a93592815814af66d50fa39e415beee0.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:42:35 -0000
Subject: This is not over yet (264315)
From: gameover@ctf100.com
To: gameover@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

flag26: zf7b75uung8afcyfj3t2

sareunea awmkaakw
```

It seems as if we are given the flag, but it is scrambled. From the hint we know the letters are aranged in the sequence 264315, and they need to be rearranged to read 123456.

```
z   f   7   b   7   5  |  u   u   n   g   8   a  | f   c   y   f   j   3   t   2
---------------------------------------------------------------------------------
2   6   4   3   1   5  |  2   6   4   3   1   5  | 2   6   4   3   1   5   2   1
```

Rearranging the letters gives the flag:

```
7zb75f8ugnaujffy3c2t
```

### Flag 27
Looking at the fourth email message we get the following:

```bash
RETR 4
+OK 877 octets
Return-Path: <wakawaka@ctf100.com>
X-Original-To: gameover@ctfmain
Delivered-To: gameover@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id D7E8E828EA
	for <gameover@ctfmain>; Mon,  7 Oct 2019 12:47:40 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user wakawaka)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:47:40 -0000
Message-ID: <3f6ad0edfd6b027c506da5fe1ee02a59.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:47:40 -0000
Subject: The sheep jump over two fences
From: wakawaka@ctf100.com
To: gameover@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

GONGTFA WNYEE SCKVTVVWNXSODIH LGTETSVNI VWJZNPZQWB
```

From the hint and reading the Subject of the email, we get the inclination that this is a rail fence cipher, with a key of 2 (hence `The sheep jump over two fences`).

Throwing the ciphertext into a railfence cipher decrpytor and using key 2 gives the flag:
```
goodnight flag twentyseven is cvkwvjtzvnvpwznqxwsb
```

We also make note of a hiddne username `wakawaka`, but we don't have the password....

### Flag 28
Here we can use `hydra` to brute force the password of the `wakawaka` user's POP3 account. The hint tells us that the password shows up between lines 4500 and 5500 of `rockyou.txt`, so we can extract those lines into a new wordlist to shorten our attack attempts:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ sed -n 4500,5500p /usr/share/wordlists/rockyou.txt > pass.txt
```

Now, the hydra command we can run is:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ hydra -t 64 -l wakawaka -P pass.txt pop3://$IP
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-06-13 17:03:14
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 1001 login tries (l:1/p:1001), ~16 tries per task
[DATA] attacking pop3://10.10.151.243:110/
[STATUS] 320.00 tries/min, 320 tries in 00:01h, 681 to do in 00:03h, 64 active
[STATUS] 256.00 tries/min, 512 tries in 00:02h, 489 to do in 00:02h, 64 active
[110][pop3] host: 10.10.151.243   login: wakawaka   password: damnit
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-06-13 17:06:12
```

Now we can log into POP3 with the `wakawaka` user and read more messages:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 110
+OK Dovecot (Ubuntu) ready.
USER wakawaka
+OK
PASS damnit
+OK Logged in.
list
+OK 6 messages:
1 953
2 1039
3 895
4 959
5 23450
6 867
```

Reading the first message gives us a clean flag:

```bash
RETR 1
+OK 953 octets
Return-Path: <wakawaka@ctf100.com>
X-Original-To: wakawaka@ctfmain
Delivered-To: wakawaka@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id 64A18828EA
	for <wakawaka@ctfmain>; Mon,  7 Oct 2019 12:48:37 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user wakawaka)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:48:37 -0000
Message-ID: <28398944887e2d66a8b8b192c98a1c01.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:48:37 -0000
Subject: More stuff
From: wakawaka@ctf100.com
To: wakawaka@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

Great, you reached the abyss. If you stare into the abyss, the abyss is
staring back at you

flag 28: 3yy9e7wwe2b8fy65sgxb

The flag is clean
```


### Flag 29
Reading the second message gives us:

```bash
RETR 2
+OK 1039 octets
Return-Path: <wakawaka@ctf100.com>
X-Original-To: wakawaka@ctfmain
Delivered-To: wakawaka@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id F2F40828EA
	for <wakawaka@ctfmain>; Mon,  7 Oct 2019 12:49:22 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user wakawaka)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:49:22 -0000
Message-ID: <37f93f2ba240bf97e89f41f47ca6bc68.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:49:22 -0000
Subject: 3310
From: wakawaka@ctf100.com
To: wakawaka@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

333 555 2 4 0 8 9 33 66 8 999 66 444 66 33 0 444 7777 0 9 7777 7 2 6 9 777
9999 44 66 222 44 777 9 777 99 33 88 5 44 0 66 33 99 8 0 7 666 777 8 0 444
7777 0 8 44 777 33 33 0 666 66 33 0 8 44 777 33 33 0 8 44 777 33 33 0 9999
33 777 666
```

The contents of the email message refer to keys pressed on the old `Nokia 3310` cellphone. We can use a tap-decoder to reveal the plain-text message:

```
FLAG TWENTY NINE IS WSPAMWRZHNCHRWRXEUJH NEXT PORT IS THREE ONE THREE THREE ZERO
```

Making note that the next port is `31330`.

### Flag 30

Reading the next mail message gives:

```bash
RETR 3
+OK 895 octets
Return-Path: <wakawaka@ctf100.com>
X-Original-To: wakawaka@ctfmain
Delivered-To: wakawaka@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id 321B0828EA
	for <wakawaka@ctfmain>; Mon,  7 Oct 2019 12:49:51 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user wakawaka)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:49:51 -0000
Message-ID: <42932e91cc912e70d6fe82a44d8ff1ba.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:49:51 -0000
Subject: You are using it right now
From: wakawaka@ctf100.com
To: wakawaka@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

g;sh yjotyu od gu[dwtig[dcinueslwyk/ Mrcy [pty od gobr pmr momr doc xrtp
```

Looking at the Subject line `You are using it right now` and the hint, we can assume that this cipher text is using the keyshift cipher. We can decode this to get the flag:

```
flag thirty is fypsqrufpsxubywakqtj. Next port is five one nine six zero
```

Making note the next port is `51960`.


### Flag 31

The next message is:

```bash
RETR 4
+OK 959 octets
Return-Path: <wakawaka@ctf100.com>
X-Original-To: wakawaka@ctfmain
Delivered-To: wakawaka@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id 3F91C828EA
	for <wakawaka@ctfmain>; Mon,  7 Oct 2019 12:50:26 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user wakawaka)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:50:26 -0000
Message-ID: <ee6dd2c7add823fe796bb173f66b1e56.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:50:26 -0000
Subject: Serial number
From: wakawaka@ctf100.com
To: wakawaka@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

xinik-samak-lomof-fisuf-pomyf-hytif-fosyk-kymyf-fetok-tytal-puvek-metul-byval-nasal-bynad-vymog-vunul-motyd-bosyk-zasol-gomyk-nosed-betef-casif-cisyx
```

From the hint and the Subject line, we can recognize that this is encoded using Bubble Babble. There is a python module that we can use to decode the text:

```python
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ python3
Python 3.7.7 (default, May 23 2020, 22:42:17)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from bubblepy import BubbleBabble
>>> bb = BubbleBabble()
>>> bb.decode('xinik-samak-lomof-fisuf-pomyf-hytif-fosyk-kymyf-fetok-tytal-puvek-metul-byval-nasal-bynad-vymog-vunul-motyd-bosyk-zasol-gomyk-nosed-betef-casif-cisyx')
b'flag 31: 5u3rfa3vm6zzh7pzyqpe. Next port is 61111'
>>>
```

The next port is `61111`.

### Flag 32


Reading the next message gives us output of another esoteric lang, this time it is JSFuck. The text was too large to post here, but it decodes to be:

```
alert("Flag 32 is 3j9c8utp2ag6bwbrkmkn. Next port is 10101")
```

The next port is `10101`.

### Flag 33

Reading the last message in `wakawaka`'s mailbox, we get the following text that appears to be an ASCII shift:

```bash
RETR 6
+OK 867 octets
Return-Path: <wakawaka@ctf100.com>
X-Original-To: wakawaka@ctfmain
Delivered-To: wakawaka@ctfmain
Received: from [192.168.247.144] (localhost [127.0.0.1])
	by ctfmain.localdomain (Postfix) with ESMTP id 426F5828EA
	for <wakawaka@ctfmain>; Mon,  7 Oct 2019 12:51:46 +0000 (UTC)
Received: from 192.168.247.129
        (SquirrelMail authenticated user wakawaka)
        by 192.168.247.144 with HTTP;
        Mon, 7 Oct 2019 12:51:46 -0000
Message-ID: <cf4d8ccfaab21a4da45d85a4c1ce3d3b.squirrel@192.168.247.144>
Date: Mon, 7 Oct 2019 12:51:46 -0000
Subject: Definately an ASCII
From: wakawaka@ctf100.com
To: wakawaka@ctfmain
User-Agent: SquirrelMail/1.4.22
MIME-Version: 1.0
Content-Type: text/plain;charset=iso-8859-1
Content-Transfer-Encoding: 8bit
X-Priority: 3 (Normal)
Importance: Normal

Hnci"55"ku"6y6x7di9r|i|chxwx9ht0"Pgzv"rqtv"ku"54434
```

We can use an online decoder to test all possible shifts and find the flag:

```
Flag 33 is 4w4v5bg7pzgzafvuv7fr. Next port is 32212
```

The next port is `32212`.

### Port to stage 3

Using the ports in the order they were given:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 9999
***************************
*   Port knocking input   *
***************************
Hi user, please enter the port sequence
The format is (can be more than 4): PORT PORT PORT PORT
> 31330 51960 61111 10101 32212
Save this sequence, you need it for stage 3
That's all for the challenge
Thank you for your participation
```

```
31330 51960 61111 10101 32212
```

## Stage 3

### Flag 34
```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nmap -Pn $IP -T5
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-13 18:17 MDT
Nmap scan report for 10.10.170.124
Host is up (0.16s latency).
Not shown: 999 filtered ports
PORT     STATE SERVICE
9999/tcp open  abyss

Nmap done: 1 IP address (1 host up) scanned in 19.82 seconds
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nc $IP 9999
***************************
*   Port knocking input   *
***************************
Hi user, please enter the port sequence
The format is (can be more than 4): PORT PORT PORT PORT
> 31330 51960 61111 10101 32212
Something happen
Good luck!
```

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ nmap -Pn $IP -T5
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-13 18:19 MDT
Nmap scan report for 10.10.170.124
Host is up (0.16s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE
80/tcp   open  http
9999/tcp open  abyss

Nmap done: 1 IP address (1 host up) scanned in 10.00 seconds
```

Looking at the source of the `/index.html` page running on port `80/tcp` we notice the following HTML block with the flag:

```html
<p>
    By default, Ubuntu does not allow access through the web browser to
    <em>any</em> file apart of those located in <tt>/var/www</tt>,
    <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html" rel="nofollow">public_html</a>
    directories (when enabled) and <tt>/usr/share</tt> (for web
    applications). You know that the flag 34 is 8thx2yafbrsj9252xycr If your site is using a web document root
    located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
    document root directory in <tt>/etc/apache2/apache2.conf</tt>.
</p>
```

### Flag 35

Running `gobuster` we find a `/webadmin` directory that contains flag 35:

```html
<p>Good job on busting this directory</p>
<p>Enjoy the free flag</p>
<p>flag 35: emu387km6a67qf537rwb</p>
<!-- There are something down here -->
```

### Flag 36
Using the `directory-list-2.3-medium.txt` wordlist, we found the `/feardead` endpoint that holds flag 36:

```html
<p>Always use multiple wordlists</p>
<p>Do not fear dead, it just a part of process. Just enjoy your life>/p>
<p>flag 36: xdvnb27v6qsv27tdj8f6</p>
<!-- Something is buried inside this directory, can you dig it up? -->
```

### Flag 37
Continuing to enumerate we find a `/hidden` directory after running `gobuster` against the `/webadmin` endpoint. Under `/webadmin/hidden` we find flag 37:

```html
<p>Always perform a recursive search</p>
<p>Easy huh?</p>
<p>flag 37: y9rwqgrvy2eds3h4caeb</p>
<p>-----------------------------</p>
<p>End of the line, none shall cross this border</p>
```


### Flag 38
Further enumerating the `/webadmin/hidden/` directory with the `directory-list-2.3-medium.txt` wordlists, we found another endpoint `/virtualserver`. Looking at the page's source we find the flag:

```html
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
<hr>
<address>Apache/2.4.29 (Ubuntu) Server at CaptureTheFlag.com Port 80</address>
</body></html>
<!-- flag 38: 4f57pmqe56ct9zthg84n -->
```

### Flag 39
Running `gobuster` with the `big.txt` wordlist, we found flag 39 on the `/keepalive` endpoint:

```html
<p>Good work here! You found another directory</p>
<p>Living is great, don't ya think?</p>
<p>flag 39: mkrk2s4jykdv5h6jz9by</p>
<!-- Solve this DH and reveal another flag -->
<!-- g: 123
     p: 557
     a: 12
     b: 32
-->
```

### Flag 40
Running `gobuster` on the `/keepalive` endpoint found another directory `/547`:

```
<p>Just a simple key-exchange<p>
<p>Good job there</p>
<p> Submit 40 and get the flag<p>
<form action="" method="POST">
<input type="hidden" name="val" value="0"/>
<input type="submit" name="submit"/>
</form>
```

Inspecting the button element and changing the value from `0` to `40` then submitting gives us the flag:

```html
<p>Just a simple key-exchange<p>
<p>Good job there</p>
<p> Submit 40 and get the flag<p>
<form action="" method="POST">
<input type="hidden" name="val" value="40"/>
<input type="submit" name="submit"/>
</form>
flag 40: 2en98pkv2w6caw4dbpg6
```

### Flag 41
Looking at the hint for this task we see it mentions virtual hosts. We saw that for flag 38 there was a hostname `capturetheflag.com` when accessing the `/webadmin/hidden/virtualserver` endpoint. Adding the value `capturetheflag.com` into our `/etc/hosts` file with the server's associated IP, and then going to `http://capturetheflag.com` gives us flag 41:

```html
<p>Finally, you found my secret server</p>
<p>Take it, you are well deserve</p>
<p>flag 41: r8r6b623zg6teg8h59gh</p>
```

### Flag 42
The hint for this task tells us there is a hidden robot. Looking at `/.robots.txt` on the `http://capturetheflag.com` website gets us flag 42:

```html
disallow:*

/
/This
/is
/BS
/flag42_66kvh828uy5jmzz6bpw4
```

### Flag 43
Running `gobuster` on the `http://capturetheflag.com` site, we found a `/wireless` endpoint with some base encoded data:

```
How good is your bases?
Zz2/%kdB.6[uX+$MhX6F6u.:43WRTO^Vc!b:.p/5mQ"`/Btbs`mZ14bBKO5|@EUcX)2//fyiUQft#a9eiUxISodBi82O8vajJ}W/r;:u13nOg,PUJgyD!pj#v8+[WCfdQ=fGL*d5UNg7Km]PVGKFx=?tTG~M?]8L@|ig?*^X]5i/GZPVul5.i;=*o3%qFQrUFMx2`tM{cO`_hZsa6/_,n#]@RG3V|6shgaab!(pzIH24OOHSA,qI&weupL`I>NrO6]Oc/f{Y43lHCNxV4|AzGrg{s4t"){y5c"86E2w"7jJH$BWlOh4Ah.zjT?^yKym:]z!8Cy=Og!fe!(aMSzR3jjCZ"Z),ijcSq%?ki[,aqtcFp9*Rn3N*:O8Wm?PJL
```

Using [CyberChef](https://gchq.github.io/) we can build a recipe that decodes this. The sequence is:

```
base91 -> base85 -> base64 -> base58 -> base32 -> hex
```

Decoding we get the flag:

```
flag43: tshpxazvl2yc9rh0nv07
```

### Flag 44
Running `gobuster` on the `http://capturetheflag.com` site, we found a `/shark` endpoint that contains the following:

```html
<p>The text has been encoded by base64 for N times</p>
<p>Did you said how many time? IDK</p>
<p>Either manual or auto decode, both work</p>
<a href="b64.txt">Download now (Not a malware)</a>
```

Downloading the file it looks like recursively base64 encoded data, so we can write a simple pytohn script to decode for us:

```python
#!/usr/local/bin/python3

import base64


with open('b64.txt', 'r') as handle:
    data = handle.read()

while 1:
    try:
        data = base64.b64decode(data)
    except:
        print('Found the flag!')
        print(data.decode('utf-8'))
        break
```

Running the script gets us the flag:

```bash
jeffrowell@kali:~/Documents/TryHackMe/CTF 100$ ./script.py
Found the flag!
flag 44: ygm2my89uqzirzj0nojw
```

### Flag 45
Given that the previous two endpoints were `/wireless` and `/shark`, I thought the next might be `/wirelessshark` as a play on WireShark. Accessing `http://capturetheflag.com/wirelessshark` we see the following:

```html
<p>Spoofing,spoofing,spooky</p>
<p>flag 45: amlq1gpoq776am3t9lz0</p>
<a href=wire.pcap></a>
```

We also have a link to a PCAP file, we download it and find the port knocking sequence for our next stage:

![knock_knock](https://user-images.githubusercontent.com/32188816/84582763-6f829e00-adad-11ea-9451-ed6f0b34f17f.png)


### Flag 46
Enumerating the `/fardead` endpoint we find that there is also an `/ftp` directory. Looking at the source shows:

```html
<p>Can you solve this?</p>
<p>flag 46: äº”é›¶ä¸ƒä¹ä¸‰ä¸ƒå…«äº”å…«ä¸ƒä¸€äºŒäºŒé›¶å››å…«ä¹é›¶å…­å…«</p>
<a href=what.png></a>
```

In the challenge hint, the flag is encoded using Chinese numbering, and decoding Google gives us text that is the numbers spelled out as the flag:

```
Five zero seven nine three seven eight five eight seven one two two zero four eight nine zero six eight
```

```
50793785871220489068
```


### The login credential for next challenge
Downloading the `what.png` image from flag 46 we can reverse the image and scale it horizontally in GIMP to get the FTP creds:

![creds](https://user-images.githubusercontent.com/32188816/84582844-99889000-adae-11ea-80df-1cf59041703d.png)

```
secure:stego
```

### Port to stage 4

![knock_knock](https://user-images.githubusercontent.com/32188816/84582763-6f829e00-adad-11ea-9451-ed6f0b34f17f.png)

```
7777 8888 6666 5555 9999
```
