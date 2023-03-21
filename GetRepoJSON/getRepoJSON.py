# get_repo_json.py

## This function will be replaced by built-in rate limiting
# https://github.com/AllSpiceIO/py-allspice/issues/6
from time import sleep
def delayserver():
    sleep(0.01)
    return

import os
from gitea import *

try:
    URL   = os.environ['ALLSPICE_URL']
except:
    print("Invalid URL. Run this command:")
    print("export ALLSPICE_URL=\"https://hub.allspice.io\"")

try:
    TOKEN = os.environ['ALLSPICE_ACCESS_TOKEN']
except:
    print("Token. Set environmental variables")
    print(">export ALLSPICE_ACCESS_TOKEN=\"YourAccessToken\"")

allspice = Gitea(URL, TOKEN)
delayserver()

# Replace with your owner, repo, and filename
# /repos/repo_owner/repo_name/allspice_generated/json/filename
file_url = "/repos/AllSpiceUser/ArchimajorFork/allspice_generated/json/Mosfets.SchDoc"
file_dict = allspice.requests_get(file_url)

# Example how to use dict
# for key in file_dict:
#     # print (f"{key}:{file_dict[key]}")

# Convert to JSON
import json
file_json = json.dumps(file_dict)
print(file_json)