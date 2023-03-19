# get_repo_json.py
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
sch_url = "/repos/AllSpiceUser/ArchimajorFork/allspice_generated/json/Mosfets.SchDoc"
sch_dict = allspice.requests_get(sch_url)

# Example how to use dict
# for key in file_dict:
#     # print (f"{key}:{file_dict[key]}")


## Parsing example, generate CSV of components -------------------------------------
attribute_list = [
    "Designator",
    "MANUFACTURER",
    "MANUFACTURER #",
    "DISTRIBUTOR",
    "DISTRIBUTOR #",
    "PART",
    "PART DESCRIPTION",
    "TOLERANCE",
    "EE_SPEC",
    "Comment"
]

## Print csv header row
csv_header_row = ""
for attribute in attribute_list:
    csv_header_row += attribute + ", "
csv_header_row += "\n"    

csv_filename = "example_part_list.csv"
csv_file = open(csv_filename, "w")
csv_file.write(csv_header_row)

component_list = []
for key in sch_dict:
    
    if "type" not in sch_dict[key]:
        continue

    if sch_dict[key]["type"] != "Component":
        continue
    
    # print(f"{key}:{sch_dict[key]}")
    csv_record = ""
    for attribute in attribute_list:
        if attribute not in sch_dict[key]["attributes"]:
            csv_record += "NA, "
            continue

        csv_record += sch_dict[key]["attributes"][attribute]["text"] + ", "

    # To add variants:
    # variant_attributes_dict = sch_dict[key]["variant_attributes"]

    csv_record += "\n"    
    csv_file.write(csv_record)

print(f"Parts list written to {csv_filename}")
csv_file.close()


# Convert to JSON
import json
sch_json = json.dumps(sch_dict)

out_filename = "example_out.json"
file_out = open (out_filename, "w")
file_out.write(sch_json)
print(f"Design JSON written to {out_filename}")
