# Based on https://github.com/Langenfeld/py-gitea


import os
from gitea import *

import pprint

TOKEN = "90667459ce8f5e7c1546d2de04577712ce0abc0e"
URL = "https://allspice.dev"
gitea = Gitea(URL, TOKEN)

print("Gitea Version: " + gitea.get_version())
print("API-Token belongs to user: " + gitea.get_user().username)

def getAllOrgTeams(organization):

    teamlist = organization.get_teams()
    for team in teamlist:
        teamLog  = organization.name + ", "
        teamLog += team.name + ", "
        teamLog += str(team.units_map) + ", "
        teamLog += "["

        teamMemberList = team.get_members()
        for teamMember in teamMemberList:
            teamLog += teamMember.email + ","
        
        # trim the final comma ","
        teamLog = teamLog.rstrip(teamLog[-1])
        teamLog += "]"
        print(teamLog)
    
    return


# get organization names
organizations = gitea.get_orgs()

# process all organizations on site
# organization = organizations[3]
for organization in organizations:
# if(1):   
   getAllOrgTeams(organization)



### reference
        # for unitmap in team.units_map:
        #     print(team.units_map[unitmap])  


