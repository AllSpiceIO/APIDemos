# getRepoBOM.py

# This function will be replaced by built-in rate limiting
# https://github.com/AllSpiceIO/py-allspice/issues/6
import os
import json
from gitea import Gitea

from time import sleep
import base64
import re

# Will remove when rate limiting is added to py-allspice
# https://github.com/AllSpiceIO/py-allspice/issues/6


def delay_server():
    sleep(0.01)


def get_repo_file(owner_name, repo_name, file_name, branch_name):
    api_command = "contents"
    api_url = f"/repos/{org_name}/{repo_name}/{api_command}/{file_name}"

    # Set branch / ref
    params = {"ref": f"{branch_name}"}

    contents_response = allspice.requests_get(api_url, params)

    file_content = base64.b64decode(contents_response["content"])
    content_string = file_content.decode("utf-8")
    return content_string


def get_sch_file_list_from_project_file(project_file_content: str) -> list:
    # Parse PcbPrj -> list of sch files
    pattern = re.compile(r"DocumentPath=(.*?SchDoc)\r\n")

    sch_list = []
    for match in pattern.finditer(project_file_content):
        sch_list.append(match.group(1))

    return sch_list

def get_sch_dict_from_repo(owner_name:str, repo_name:str, filename:str, branch_name:str)->dict:
    # Replace with your owner, repo, and filename
    # /repos/repo_owner/repo_name/allspice_generated/json/filename
    api_url = "/repos/AllSpiceUser/ArchimajorFork/allspice_generated/json/Mosfets.SchDoc"



    api_url = f"/repos/{owner_name}/{repo_name}/allspice_generated/json/{filename}"

    # Set branch / ref
    params = {"ref": f"{branch_name}"}

    file_dict = allspice.requests_get(api_url, params)
    return file_dict


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
branch_name = "main"

project_file_content = get_repo_file(org_name,
                                     repo_name,
                                     project_file_name,
                                     branch_name)

sch_file_list = get_sch_file_list_from_project_file(project_file_content)

### Print header row
print("org_name, repo_name, file_name, refdes, mfg_name, mpn")

## print component attributes
### for every schematic filename parsed from .PcbPrj
for file_name in sch_file_list:
    sch_dict = get_sch_dict_from_repo(org_name,
                    repo_name,
                    file_name,
                    "main")

    ### parse individual attributes
    for key in sch_dict:

        attribute_list = []

        try:
            attributes = sch_dict[key]["attributes"]
            attribute_list.append( attributes["Designator"]["text"] )
            attribute_list.append( attributes["MANUFACTURER"]["text"] )
            attribute_list.append( attributes["MANUFACTURER #"]["text"] )

        except KeyError:
            continue

        except TypeError:
            continue

        print(f"{org_name}, {repo_name}, {file_name}, " + ', '.join(attribute_list))
 