from fabric.api import *
from fabric.contrib import files

env.hosts = ["127.0.0.1"]
env.user = "ec2-user"
env.key_filename = "/home/ubuntu/prince-betaout.pem"

def osbasics():
	sudo("yum install -y yum-plugin-fastestmirror.noarch")
	sudo("yum -y update")
	sudo("yum install -y java mod_ssl nmap nano links svn mlocate make cmake glib glib2 libpng libjpeg libtiff ghostscript freetype ImageMagick ImageMagick-perl telnet libevent libmemcached libmemcached-devel memcached nscd ntpd")
	sudo("rm -rf /etc/localtime")
	sudo("ln -sf /usr/share/zoneinfo/GMT /etc/localtime")
	sudo("chkconfig nscd on")
	sudo("chkconfig ntpd on")
	sudo("service nscd start")
	sudo("service ntpd start")

def configure():
	osbasics()

