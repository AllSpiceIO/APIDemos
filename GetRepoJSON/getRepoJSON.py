# get_repo_json.py

# This function will be replaced by built-in rate limiting
# https://github.com/AllSpiceIO/py-allspice/issues/6
import os
import json
from gitea import *
from time import sleep

# Will remove when rate limiting is added to py-allspice
# https://github.com/AllSpiceIO/py-allspice/issues/6
def delay_server():
    sleep(0.01)

try:
    URL = os.environ['ALLSPICE_URL']
except KeyError:
    print("Invalid URL. Run this command:")
    print("export ALLSPICE_URL=\"https://hub.allspice.io\"")
    quit()

try:
    TOKEN = os.environ['ALLSPICE_ACCESS_TOKEN']
except KeyError:
    print("Invalid token. Set environmental variables")
    print(">export ALLSPICE_ACCESS_TOKEN=\"YourAccessToken\"")
    quit()

allspice = Gitea(URL, TOKEN)
delay_server()

# Replace with your owner, repo, and filename
owner    = "AllSpiceUser"
reponame = "ArchimajorFork"
api_path = "allspice_generated/json/"
filename = "Mosfets.SchDoc"

# Build API URL
# /repos/repo_owner/repo_name/allspice_generated/json/filename
file_url = f"/repos/{owner}/{reponame}/{api_path}/{filename}"

# Set branch / ref
params = {"ref": "main"}

file_dict = allspice.requests_get(file_url, params)

# Convert to JSON
file_json = json.dumps(file_dict)
print(file_json)
