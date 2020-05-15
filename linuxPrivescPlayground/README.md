# Linux Privesc Playground

SSH creds are `user:password`

```
export IP=10.10.182.9
```

## Task 1
1. Get the easiest flag on THM (/root/flag.txt)
Running `linpeas` we find we can become root in almost any way possible..... We see that we can run `screen` as root, so with a simple `sudo screen` we can cat the flag in root's home:
```
root@privesc:/tmp# cat /root/flag.txt
Congratulations! You got the easiest flag on THM!
THM{3asy_f14g_1m40}
Now go priv esc some more!
```
