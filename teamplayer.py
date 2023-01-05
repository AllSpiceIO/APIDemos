# Based on https://github.com/Langenfeld/py-gitea

# Use prepopulated team member and org lists to spoof file read and speed up development


import os
# from gitea import *

# Importing locally from /gitea/gitea/, not the installed py-gitea api
from gitea.gitea import *

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


readWrite = "write"
canCreateOrgRepo = True
includesAllRepos = True

teamList.append( Team("Owners",
                        "Owners of the org",
                        readWrite,
                        canCreateOrgRepo,
                        includesAllRepos,
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
                        ["daniel@allspice.io", "daniel+test2@allspice.io"]))

canCreateOrgRepo = False
readWrite = "read"
teamList.append( Team("Collaborators", 
                        "Can read and participate in design reviews",
                        readWrite,
                        canCreateOrgRepo,
                        includesAllRepos,
                        {
                            "repo.code": "read",
                            "repo.ext_issues": "none",
                            "repo.ext_wiki": "none",
                            "repo.issues": "read",
                            "repo.projects": "read",
                            "repo.pulls": "read",
                            "repo.releases": "read",
                            "repo.wiki": "read"
                        }, 
                        ["daniel+revareviewa@allspice.io", "daniel+mikachanical@allspice.io"]))

canCreateOrgRepo = True
readWrite = "write"
teamList.append( Team("Contributors", 
                        "write acceess to team repos",
                        readWrite,
                        canCreateOrgRepo,
                        includesAllRepos,
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
                        ["daniel@allspice.io", "daniel+mikachanical@allspice.io"]))



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

        for team in teamList:
            units=(
                        "repo.code",
                        "repo.issues",
                        "repo.ext_issues",
                        "repo.wiki",
                        "repo.pulls",
                        "repo.releases",
                        "repo.ext_wiki",
                )
            units_map = team.units_map
            teamToMod = organization.get_team(team.name)
            print(f'team.readWrite, {team.readWrite}')
            if (teamToMod == None):
                teamToMod = gitea.create_team(organization, team.name, team.description, team.readWrite, team.canCreateOrgRepo, team.includesAllRepos, units, units_map)
                # teamToMod = gitea.create_team(organization, team.name, "teamdesc", "write", True, True, units, units_map)
                # teamToMod = gitea.create_team(organization, team.name, team.description, team.readWrite, True, True, units, units_map)
                # print(f'team.readWrite, {team.readWrite}')
                # teamToMod = gitea.create_team(organization, team.name, team.description, "write", True, True, units, units_map)
                

            # Add usernames to team
            for email in team.memberEmails:
                user = gitea.get_user_by_email(email)
                if teamToMod is not None:
                    teamToMod.add_user(user)



### reference
        # for unitmap in team.units_map:
        #     print(team.units_map[unitmap])  


