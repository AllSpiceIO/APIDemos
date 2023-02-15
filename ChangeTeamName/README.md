# changeteamname.py
A script for changing teamnames in AllSpice Hub

## Notes
orgsToMod and teamList are manually populated, if script is useful, should convert to loading orgs and teams from a file


## Setup
Clone this repo

Clone the python wrapper for gitea into this repo/gitea : https://github.com/AllSpiceIO/py-gitea
example:
Teamplayer/gitea/readme.md
Teamplayer/gitea/gitea/gitea.py

Do not use https://github.com/Langenfeld/py-gitea as modifications and extentions have been madeeeeee


## Environmental variables
Generate access token if needed: 
https://hub.allspice.io/user/settings/applications


Set the access token from the commandline or your environment variables
Mac / Linux
`export ALLSPICE_ACCESS_TOKEN="<youraccesstoken>"`

Windows
`set ALLSPICE_ACCESS_TOKEN="youraccesstoken"`

Set the url. If you are a standard AllSpice user, your URL is https://hub.allspice.io
Mac/Linux
`export ALLSPICE_URL="https://hub.allspice.io"`

Windows
`set ALLSPICE_URL="https://hub.allspice.io"`


## Modify json file


## Run the script
`python3 changeteamname.py teamtoChangeExample.json`
