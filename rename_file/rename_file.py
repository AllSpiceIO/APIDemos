# Get_shas.py

import os
from allspice import AllSpice

# ----------------------------
# Test basic server connectivity
try:
    URL = os.environ['ALLSPICE_URL']
except KeyError:
    print("Invalid URL. Run this command:")
    print("export ALLSPICE_URL=\"https://hub.allspice.io\"")

try:
    TOKEN = os.environ['ALLSPICE_ACCESS_TOKEN']
except KeyError:
    print("Token. Set environmental variables")
    print(">export ALLSPICE_ACCESS_TOKEN=\"YourAccessToken\"")

allspice = AllSpice(URL, TOKEN)

print("AllSpice Version: " + allspice.get_version())
print("API-Token belongs to user: " + allspice.get_user().username)

# test values
repo_owner = "AllSpiceUser"
repo_name = "TestAPIs"
new_file_path = "new_file_path.txt"  # include path and file name
old_file_path = "old_file_path.txt"  # include path and file name
branch_to_modify = "develop"


# fetch the sha from repo_owner, repo_name_ and old_file_path
param = {
    "ref": branch_to_modify
}
API_CONTENTS = """/repos/%s/%s/contents/%s"""  # repo_owner, repo_name, old_file_path
file_metadata = allspice.requests_get(
    API_CONTENTS % (repo_owner, repo_name, old_file_path), param)

# Compose the put reuqest to rename the file
API_RENAME = """/repos/%s/%s/contents/%s"""  # repo_owner, repo_name, new_path
# populate param var with sha, old_file_path, commit message, and branch
param = {
    "sha": file_metadata["sha"],
    "from_path": old_file_path,
    "message": "commit message",
    "branch": branch_to_modify
}

# send the request to rename the file
allspice.requests_put(API_RENAME % (
    repo_owner, repo_name, new_file_path), param)
