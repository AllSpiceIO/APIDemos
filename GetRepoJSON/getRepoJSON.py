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
# Generates header and index to json attributes
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

# Setup CSV writer
import csv
csv_filename = "example_part_list.csv"
csv_file = open(csv_filename, "w", newline='')
csv_writer = csv.writer(csv_file)

# Write CSV header row
csv_writer.writerow(attribute_list)

# Add each attribute to a list and then write the list to the CSV file
component_list = []
for key in sch_dict:

    # Check for wrong data type
    if "type" not in sch_dict[key]:
        continue

    # Check for component type
    if sch_dict[key]["type"] != "Component":
        continue
    
    # Add each attribute to the list
    csv_record_list = []
    for attribute in attribute_list:

        # check if attribute in record
        if attribute not in sch_dict[key]["attributes"]:
            csv_record_list.append("NA")
            continue

        # write csv record of all attributes
        csv_record_list.append(sch_dict[key]["attributes"][attribute]["text"])

    # To add variants:
    # variant_attributes_dict = sch_dict[key]["variant_attributes"]

    csv_writer.writerow(csv_record_list)   

print(f"Parts list written to {csv_filename}")
csv_file.close()


# Convert schematic dictionary to JSON -----------------------------
import json
sch_json = json.dumps(sch_dict, indent=4)

out_filename = "example_out.json"
file_out = open (out_filename, "w")
file_out.write(sch_json)
print(f"Design JSON written to {out_filename}")
