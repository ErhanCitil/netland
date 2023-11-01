Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess netland-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/netland/log/apache2/error.log"
        CustomLog "/srv/sites/netland/log/apache2/access.log" common

        WSGIProcessGroup netland-<target>

        Alias /media "/srv/sites/netland/media/"
        Alias /static "/srv/sites/netland/static/"

        WSGIScriptAlias / "/srv/sites/netland/src/netland/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-netland-<target>]
    user = <user>
    command = /srv/sites/netland/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/netland/src/netland/wsgi/wsgi_<target>.py
    home = /srv/sites/netland/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/netland/log/uwsgi_err.log
    stdout_logfile = /srv/sites/netland/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_netland_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/netland/log/nginx-access.log;
      error_log /srv/sites/netland/log/nginx-error.log;

      location /500.html {
        root /srv/sites/netland/src/netland/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/netland/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/netland/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_netland_<target>;
      }
    }
