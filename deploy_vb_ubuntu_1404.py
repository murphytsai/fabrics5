import re, os, inspect

from fabric.api import env, local, run, sudo
from fabric.context_managers import cd, lcd, prefix, settings
from fabric.contrib.console import confirm
from fabric.contrib.files import exists



def deploy_os():
    sudo("apt-get update")
    sudo("mkdir -p /media/cdrom;mount /dev/cdrom /media/cdrom")
    sudo("apt-get install -y dkms build-essential linux-headers-generic linux-headers-$(uname -r)")
    sudo("/media/cdrom/VBoxLinuxAdditions.run")
