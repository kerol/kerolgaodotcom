About
=====

Deploy Django projects on ECS.
Nginx + uWSGI + Supervisor.

Configuration
~~~~~~~~~~~~~

Nginx:

-    rename nginx.conf to kerolgao.com.conf
-    copy to /etc/nginx/conf.d/kerolgao.com.conf

uWSGI:

do nothing.

Supervisor:

-    edit supervisor.conf
-    rename kerolgao.com.ini
-    copy to /etc/supervisord.d/kerolgao.com.ini

Notes
~~~~~

commands(centos 7):

-    systemctl start nginx
-    systemctl start supervisord


