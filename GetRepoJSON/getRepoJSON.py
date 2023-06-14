# get_repo_json.py

import os
import json
from allspice import AllSpice, Repository

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

allspice = AllSpice(URL, TOKEN)

repo: Repository = Repository.request(allspice, "AllSpiceUser", "ArchimajorFork")

# Replace with the path to the file from the root of the repo
file_path = "Mosfets.SchDoc"

# If you want the JSON for a specific commit or branch, get it from the repo object:
ref = repo.get_branch("main")

# You can also directly use a sha hash
ref = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6"

# Or a branch name
ref = "main"

file_dict = repo.get_generated_json(file_path, ref)

# Example how to use dict
# for key in file_dict:
#     # print (f"{key}:{file_dict[key]}")

# Convert to JSON
file_json = json.dumps(file_dict)
print(file_json)
