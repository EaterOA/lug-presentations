Preparation
===

* start gotty server

    # start a tmux session under gotty
    ./gotty -p 8080 tmux new -A -s gotty

    # on another terminal
    tmux new -A -s gotty

    # to control tmux
    ### split horizontal:   ^a "
    ### split vertical:     ^a %
    ### move between windows:   ^a ^(up-down-left-rght)
    ### resize current window:  ^a (up-down-left-rght)

* start python http.server

    python3 http.server 8000

* start ngrok

    ./ngrok http 8080

Confirm that all of the above work (load in browser)

Presentation
===

Preparation
---

sudo apt-get install nginx
sudo apt-get install postgresQL
sudo apt-get install varnish
sudo apt-get install python-pip python3-pip
sudo pip3 install Flask flask-sqlalchemy jinja2 werkzeug markupsafe itsdangerous
sudo pip install Flask flask-sqlalchemy jinja2 werkzeug markupsafe itsdangerous

Webapps
---

- A server is just a computer sitting somewhere
  - How you access these servers is via ssh or ftp
  - SSH allows you to control the server through a command line interface

- People deploy apps these days with both PaaS and servers
  - Using a server gives you full control and you can do much more

Nginx
===

- A webserver is just a server that responds to HTTP requests with webpages.
  When you go to a website and type in a URL, your browser is making an HTTP
  request to that server.
- A lot of websites have a domain name, which actually just maps to the IP
  address
- In our case, we don't have a domain, so we use the IP address directly

- We've preinstalled a lot of the necessary components for our webserver, so
  what we will teach you today is how to enable, use, and configure them.

    service nginx start

- Nginx is a program that reads HTTP requests and sends responses. The most
  basic thing it can do is just sending back HTML pages.

    # go to <ip> on browser

- Look at /etc/nginx/sites-available/default
- Configuration for your current website
- A lot of details, but one interesting one is `root /usr/share/nginx/html`

    cd /usr/share/nginx/html
    vim index.html
    # modify whatever
    # reload page
    
    vim somepage.html
    # load <ip>/somepage.html
