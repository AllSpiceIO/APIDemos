# HelloWorld.py

# If you're new to scripting, this is a great place to start. 

# Hello World starts you out easy with some simple server requests.
# This will help you troubleshoot your connection and show you the basics of making an api request

import sys
sys.path.append('..')
from allspice.allspice import AllSpice
allspice = AllSpice()
allspice.start()

versionResponse = ""
try:
    versionResponse = allspice.hub.get_version()
except:
    allspice.log.error(f'failure to gitea.get_version()')
    quit()

allspice.log.info(f'Allspice Version: {versionResponse}')

username = ""
try:
    username = allspice.hub.get_user().username
except:
    allspice.log.error('User authentication invalid')
    quit()

allspice.log.info(f'API-Token belongs to user: {username}')


