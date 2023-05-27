# get_repo_json.py

# This function will be replaced by built-in rate limiting
# https://github.com/AllSpiceIO/py-allspice/issues/6
import os
import json
from gitea import Gitea, Organization, Commit
from time import sleep

# Will remove when rate limiting is added to py-allspice
# https://github.com/AllSpiceIO/py-allspice/issues/6

class Object(object):
    pass

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

this_org = Organization.request(allspice, "ProductDevelopmentFirm")

repo_list = this_org.get_repositories()


for repo in repo_list:

    branch_list = repo.get_branches()
    i=0
    for branch in branch_list:
        params = Object()
        try:
            params.sha = branch.name
            file_list = repo.get_git_content(params)
            for obj in file_list:
                print(obj.name)
            # print(f"{repo.name}/{branch.name}-> {file_list.name}")
        except TypeError:
            # empty branch
            pass




# # Replace with your owner, repo, and filename
# # /repos/repo_owner/repo_name/allspice_generated/json/filename
# file_url = "/repos/AllSpiceUser/ArchimajorFork/allspice_generated/json/Mosfets.SchDoc"

# # Set branch / ref
# params = {"ref": "main"}

# file_dict = allspice.requests_get(file_url, params)

# # Example how to use dict
# # for key in file_dict:
# #     # print (f"{key}:{file_dict[key]}")

# # Convert to JSON
# file_json = json.dumps(file_dict, indent=4)
# print(file_json)
