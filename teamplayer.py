# Based on https://github.com/Langenfeld/py-gitea

# Use prepopulated team member and org lists to spoof file read and speed up development


import os
from gitea import *

from src.team import Team

import pprint

TOKEN = "90667459ce8f5e7c1546d2de04577712ce0abc0e"
URL = "https://allspice.dev"
gitea = Gitea(URL, TOKEN)

print("Gitea Version: " + gitea.get_version())
print("API-Token belongs to user: " + gitea.get_user().username)



def setOrgTeam(organization):
   
    return

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



# teamlist
orgsToMod = ["UtilityTesting"]
teamList = []
teamList.append( Team("teamFoo", 
                        {
                            "repo.code": "write",
                            "repo.ext_issues": "write",
                            "repo.ext_wiki": "write",
                            "repo.issues": "write",
                            "repo.projects": "write",
                            "repo.pulls": "write",
                            "repo.releases": "write",
                            "repo.wiki": "write"
                        },
                        ["email1@domain.com", "email2@domain.com"]))

teamList.append( Team("teamBar", 
                        {
                            "repo.code": "write",
                            "repo.ext_issues": "write",
                            "repo.ext_wiki": "write",
                            "repo.issues": "write",
                            "repo.projects": "write",
                            "repo.pulls": "write",
                            "repo.releases": "write",
                            "repo.wiki": "write"
                        },
                        ["email3@domain.com", "email4@domain.com", "email5@domain.com"]))



for team in teamList:
    print(team.__str__())

# get organization names
organizations = gitea.get_orgs()

# process all organizations on site
organization = organizations[3]
for organization in organizations:
# if(1):   
#    getAllOrgTeams(organization)
    print("foo")

    if organization.name in orgsToMod:
        print(f'modifyOrg, {organization.name}')
        #getAllOrgTeams(organization)
        # setOrgTeam(organization

        # for team in teamList:
        gitea.create_team(organization, "team31", "team12", "read", True, True)




### reference
        # for unitmap in team.units_map:
        #     print(team.units_map[unitmap])  


