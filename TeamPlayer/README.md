# TeamPlayer
A script for manipulating teams in AllSpice / Gitea

Proof of concept script to add teams with specific permissions to organizations

## Notes
orgsToMod and teamList are manually populated, if script is useful, should convert to loading orgs and teams from a file

Pseudocode:
```
for organization in orgsToMod:
    for team in TeamList:
        newTeam = organization.add_team()
        for email in team.memberEmails:
            user = gitea.get_user_by_email(email)
            newTeam.add_user(user)
```


Script will add all teams+teammembers from teamList to all organizations from orgsToMod
If a team does not exist it is created. If a team already exists, it will be modified.

## Setup
Clone this repo API_DEMOS

Teamplayer requires a modified version of py-gitea and is located in the API_DEMOS/pygitea_mod folder
    This folder should clone automatically
    These modifications are temporary. We are trying to get the changes upstreamed and remove our modified pygitea, but for now, this gives access to unsupported functions



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


## Edit your json file


## Run the script
`python3 teamplayer.py UpdateOrgTeamsExample.json`


