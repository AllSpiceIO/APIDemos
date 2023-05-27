# get_repo_json.py

# This function will be replaced by built-in rate limiting
# https://github.com/AllSpiceIO/py-allspice/issues/6
import os
import json
from gitea import Gitea, Organization
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


def get_repo_branch_files(owner_name: str,
                          repo_name: str,
                          branch_name="main",
                          path=""):

    # Create Object to attach attributes to match api call
    params = Object()
    params.sha = branch_name
    params.path = path
    params.type = None

    file_list = repo.get_file_content(params)
 
    for obj in file_list:
        if (obj._type == "file"):
            print(f"{repo.name}/{branch.name} [{path}/{obj._name}]")
            pass
        elif (obj._type == "dir"):
            try:
                # recursively parse dirs
                get_repo_branch_files(
                    owner_name, repo_name, branch_name, obj._name)
            except AttributeError:
                pass
    return None


# TBD - replace with better example
print(__file__)
owner_name = "ProductDevelopmentFirm"

this_org = Organization.request(allspice, owner_name)

repo_list = this_org.get_repositories()

for repo in repo_list:

    branch_list = repo.get_branches()
    for branch in branch_list:

        try:
            foo = get_repo_branch_files(owner_name, repo.name, branch.name)

        except TypeError:
            # empty branch - not sure how to check this better
            pass


# for repo in repo_list:

#     branch_list = repo.get_branches()
#     for branch in branch_list:
#         params = Object()
#         try:
#             params.sha = branch.name
#             file_list = repo.get_git_content(params)
#             for obj in file_list:
#                 if(obj._type == "file"):
#                     print(f"{repo.name}/{branch.name} [{obj._name}]")
#         except TypeError:
#             # empty branch - not sure how to check this better
#             pass


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
