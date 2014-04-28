import re, os, inspect

from fabric.api import env, local, run, sudo
from fabric.context_managers import cd, lcd, prefix, settings
from fabric.contrib.console import confirm
from fabric.contrib.files import exists



def deploy_essential():
    sudo("yum -y update")
