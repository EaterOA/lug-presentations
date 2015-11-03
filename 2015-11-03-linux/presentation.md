Preparation
===

* set up LAN
* start gotty server
* start python http.server

Confirm that all of the above works

Presentation
===

Daily life: open up libreoffice writer and stea:
Package management: open up software manager, install gparted
Distros: open up gparted, show the 3 different distros, shared home (wiped chromeos and installed linux; can't do that w/ windows nor mac)
Desktop environment: switch to KDE

Demo
---

1. Start off with basics
 - Explain what a filesystem is and how terminal is navigated
 - pwd
 - ls
 - mkdir test
 - cd test
 - pwd
 - echo "Hello, world!" > hello.txt
 - ls
 - ls -l hello.txt
 - cat hello.txt
 - You can do a lot more with scripting
 - for x in {a..m}; do touch "$x.txt"; done
 - for x in {a..m}; do touch "$x.gif"; done
 - ls *.txt
 - mkdir textfiles
 - mv *.txt textfiles
2. Custom scripts
 - Go through process of creating a random password generator
 - cat /dev/urandom | tr -cd 'a-z' | head -c 16; echo
 - Shell gives you access to all languages and tools
 - Show custom monitor.py script
 - Show sspuush script
 - Show getip script
3. Utilities
 - Shell has a lot of cute utilities
 - date
 - TZ="Japan" date
 - cal, cal -3
 - factor 8432717483
4. SSH
 - ssh into seasnet
 - Use seasnet to compile something
 - scp it back
 - X forward: ssh lug -XC2 -c blowfish-cbc
5. Torrenting
 - ssh nano
 - deluged && deluge-console
 - add https://www.archlinux.org/releng/releases/2015.11.01/torrent/
6. Running services
 - These slides are actually being served from my laptop right now
 - The live TTY too
 - (if running bind9: and DNS server)
7. Networking
 - nc -l 8000
 - On another window, telnet localhost 8000
 - Serve a file: nc -l 8000 < monitor.py
 - On another window, nc localhost 8000 > received.py
 - Talk to external http server: telnet linux.ucla.edu 80, GET / HTTP/1.1
