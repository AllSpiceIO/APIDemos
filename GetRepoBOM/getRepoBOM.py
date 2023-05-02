# getRepoBOM.py

# This function will be replaced by built-in rate limiting
# https://github.com/AllSpiceIO/py-allspice/issues/6
import os
import json
from gitea import Gitea, Repository, Content

from time import sleep
import base64

# Will remove when rate limiting is added to py-allspice
# https://github.com/AllSpiceIO/py-allspice/issues/6


def delay_server():
    sleep(0.01)


# def get_repo_file()



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


# Get PcbPrj file from repo
org_name = "ProductDevelopmentFirm"
repo_name = "ArchimajorDemo"
project_file_name = "Archimajor.PrjPcb"
api_command = "contents"
api_url = f"/repos/{org_name}/{repo_name}/{api_command}/{project_file_name}"

# Set branch / ref
params = {"ref": "main"}

contents_response = allspice.requests_get(api_url, params)

file_content = base64.b64decode(contents_response["content"])
content_string = file_content.decode("utf-8") 
print(content_string)



# Example how to use dict
# for key in file_dict:
#     # print (f"{key}:{file_dict[key]}")

# Convert to JSON
# file_json = json.dumps(file_dict)
# print(file_json)
