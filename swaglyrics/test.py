import subprocess
import sys
import os

cmd = 'pip install %s --upgrade swaglyrics'

print(os.geteuid())

if os.geteuid() != 0:
    subprocess.call(['sudo', 'python3', *sys.argv])


# sudo = False
#
# if sudo:
#     cmd = cmd % ''
#     run('sudo %s' % cmd, shell=True)
# else:
#     cmd = cmd % '--user'
#     run(cmd, shell=True)
