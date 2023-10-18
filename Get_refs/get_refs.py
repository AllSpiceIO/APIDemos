# Get_refs.py

import os
from allspice import AllSpice, Repository

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

repo_owner = "ExampleOrganization"
repo_name = "RepoName"

test_repo = Repository.request(allspice, repo_owner, repo_name)

API_REFS = """/repos/%s/%s/git/refs"""  # <sha>``
print (f"{repo_owner} - {test_repo.name}")
commits = allspice.requests_get(API_REFS % (repo_owner, test_repo.name))
for commit in commits:
    print(commit["ref"] + " " + commit["object"]["sha"])




