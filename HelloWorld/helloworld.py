# HelloWorld.py

# If you're new to scripting, this is a great place to start.

# Hello World starts you out easy with some simple server requests.
# This will help you troubleshoot your connection and show you the basics of making an api request
#
# For more information read our README.md
import os
from gitea import *

try:
    URL = os.environ['ALLSPICE_URL']
except:
    print("Invalid URL. Run this command:")
    print("export ALLSPICE_URL=\"https://hub.allspice.io\"")

try:
    TOKEN = os.environ['ALLSPICE_ACCESS_TOKEN']
except:
    print("Token. Set environmental variables")
    print(">export ALLSPICE_ACCESS_TOKEN=\"YourAccessToken\"")

allspice = Gitea(URL, TOKEN)

print("AllSpice Version: " + allspice.get_version())
print("API-Token belongs to user: " + allspice.get_user().username)
