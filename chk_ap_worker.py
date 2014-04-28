from fabric.api import run
from fabric.colors import red, green

def chk_ap_worker_logs():
    a=run('tail /var/log/analyzeplatform/celery.log')
    print (red(a))
