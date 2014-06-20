import re, os, inspect

from fabric.api import env, local, run, sudo
from fabric.context_managers import cd, lcd, prefix, settings
from fabric.contrib.console import confirm
from fabric.contrib.files import exists



def deploy_usandbox():
    sudo("yum -y update")
    sudo("yum -y install glibc.i686")
    sudo("yum -y install libstdc++")
    sudo("yum -y install libstdc++.i686")
    sudo("rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt")
    sudo("wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm")
    sudo("rpm -i rpmforge-release-0.5.3-1.el6.rf.*.rpm")
    sudo("rm *.rpm")
    sudo("yum -y install dkms")
    sudo("yum -y install kernel-devel kernel-headers")
    sudo("yum -y install postgresql postgresql-server.x86_64")
    sudo("yum -y install postgresql-devel")
    #sudo("service postgresql initdb")
    sudo("yum -y install bison gettext glib2 freetype fontconfig libpng libpng-devel libX11 libX11-devel glib2-devel libgdi* libexif glibc-devel urw-fonts java unzip gcc gcc-c++ automake autoconf libtool make bzip2 wget zip python-devel python-setuptools")
    sudo("easy_install pip")
    sudo("pip install psycopg2 pysphere celery redis simplejson pymongo requests")
    sudo("pushd . && cd /usr/local/src && wget http://download.mono-project.com/sources/mono/mono-2.10.8.tar.gz && popd")
    sudo("pushd . && cd /usr/local/src && tar zxvf mono-2.10.8.tar.gz && cd /usr/local/src/mono-2.10.8 && ./configure --prefix=/usr/local && make && make install && popd")

