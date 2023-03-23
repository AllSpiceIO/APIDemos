# addfiletorepo.py

import base64
import os
from gitea import *


def encode_base64_string(string_input:str):
    sample_string_bytes = string_input.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

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

#org = Organization.request(allspice, "ProductDevelopmentFirm")
repo = Repository.request(allspice, "ProductDevelopmentFirm", "AddfileViaAPIDemo")

file_content = "# A wonderful text example"
b64_str_content = encode_base64_string(file_content)

repo.create_file("documentation.md",b64_str_content)



