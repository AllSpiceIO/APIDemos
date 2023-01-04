# Based on https://github.com/Langenfeld/py-gitea


import os
from gitea import *

import pprint

TOKEN = "90667459ce8f5e7c1546d2de04577712ce0abc0e"
URL = "https://allspice.dev"
gitea = Gitea(URL, TOKEN)

print("Gitea Version: " + gitea.get_version())
print("API-Token belongs to user: " + gitea.get_user().username)

# get organization names
organizations = gitea.get_orgs()

# process all organizations on site
organization = organizations[3]
# for organization in organizations:
if(1):   
    # debug
    print(organization.name)
    
    # get all repos
    OrganizationRepos = organization.get_repositories()

    teamlist = organization.get_teams()
    for team in teamlist:
        # print("teamname, " + team.name + ", units" + str(sorted(team.units)) )
        # teamMemberList = team.get_members()

        print(team.permission)
        # for unit in team.units:
        #     print(unit)

        print(team.units_map)
        print(team.units_map['repo.code'])
        for unitmap in team.units_map:
            print(team.units_map[unitmap])

        teamMemberList = team.get_members()
        for teamMember in teamMemberList:
            print("team: " + team.name + ", member: " + teamMember.email)
    
    # process all repositories in an organization
    # for repo in OrganizationRepos:
        
    #     # debug
    #     print(repo.get_full_name())

    #     # process all branches
    #     repoBranches = repo.get_branches()
    #     print("branchCount, " + str(len(repoBranches)))

    #     commitCount = 0
    #     # for branch in repoBranches:
    #     #     print("branchName, " + branch.__getattribute__("name"))
          
    #     #     #print("branch, " + branch )

    #     # count all commits
    #     repoCommits = repo.get_commits()

        


