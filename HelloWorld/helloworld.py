# HelloWorld.py

# If you're new to scripting, this is a great place to start. 

# Hello World starts you out easy with some simple server requests.
# This will help you troubleshoot your connection and show you the basics of making an api request


import logging
import os

# importing Py-gitea
# https://github.com/Langenfeld/py-gitea
from gitea import *


# Load URL and access token from environmental variables
try:
    URL = os.environ['ALLSPICE_URL']
    # URL = "https://allspice.dev"
except:
    logging.error(f'ALLSPICE_URL is None, run >export ALLSPICE_URL="yourURL"')
    quit()


try:
    TOKEN = os.environ['ALLSPICE_ACCESS_TOKEN']
except:
    loggin.error(f'ALLSPICE_ACCESS_TOKEN is None, run >export ALLSPICE_ACCESS_TOKEN="token", create token at {URL}/user/settings/applications')
    quit()


# create website object  
gitea = Gitea(URL, TOKEN)

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')


# --------------------------------------------------
# Start script

logging.info("Hello world test script")

logging.info(f'Gitea Version: {gitea.get_version()}')



username = gitea.get_user().username
logging.info(f'get_user().username={username}')
try:
    username = gitea.get_user().username
except:
    logging.error('User authentication invalid')
    quit()

logging.info(f'API-Token belongs to user: {username}')


# get all organization names
organizations = gitea.get_orgs()

