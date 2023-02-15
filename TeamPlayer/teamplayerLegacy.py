# teamplayer.py

# script to demonstrate organization / team / member / permissions

# Load the allspice/gitea module
import os
import sys
sys.path.append('..')
from allspice_proto.allspice_proto import AllSpice_Proto
allspice = AllSpice_Proto()
allspice.start()


# helper class, different than gitea.teams, should merge
from allspice_proto.src.team import Team

# Create list of organizations to modify
orgsToMod = ["UtilityTesting"]


# Create teams
readWrite = "write"
canCreateOrgRepo = True
includesAllRepos = True
teamList = []
# teamList.append( Team("Owners",
#                         "Owners of the org",
#                         readWrite,
#                         canCreateOrgRepo,
#                         includesAllRepos,
#                         {
#                             "repo.code": "write",
#                             "repo.ext_issues": "write",
#                             "repo.ext_wiki": "write",
#                             "repo.issues": "write",
#                             "repo.projects": "write",
#                             "repo.pulls": "write",
#                             "repo.releases": "write",
#                             "repo.wiki": "write"
#                         }, 
#                         ["daniel@allspice.io", "daniel+test2@allspice.io"]))

# canCreateOrgRepo = False
# readWrite = "read"
# teamList.append( Team("Plumbers", 
#                         "Can read and participate in design reviews",
#                         readWrite,
#                         canCreateOrgRepo,
#                         includesAllRepos,
#                         {
#                             "repo.code": "read",
#                             "repo.ext_issues": "none",
#                             "repo.ext_wiki": "none",
#                             "repo.issues": "read",
#                             "repo.projects": "read",
#                             "repo.pulls": "read",
#                             "repo.releases": "read",
#                             "repo.wiki": "read"
#                         }, 
#                         ["daniel+revareviewa@allspice.io", "daniel+mikachanical@allspice.io"]))

canCreateOrgRepo = True
readWrite = "write"
teamList.append( Team("ChupChups", 
                        "update description",
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
                            "repo.releases": "read",
                            "repo.wiki": "write"
                        }, 
                        ["daniel@allspice.io", "daniel+mikachanical@allspice.io"]))

# permission units, associated with units_map
units=(
            "repo.code",
            "repo.issues",
            "repo.ext_issues",
            "repo.wiki",
            "repo.pulls",
            "repo.releases",
            "repo.ext_wiki",
    )


# --------------------------------------------------
# Start script

DEBUG_EMAILS   = False
DEBUG_ORG_LIST = False
DEBUG_ORG      = False
DEBUG_TEAMS    = True


# hub = allspice.hub
allspice.log.info(f'TeamPlayer python script')



# get all organization names
organizations = allspice.hub.get_orgs()
if DEBUG_ORG_LIST:
    allspice.log.info(f'organization list')
    for organization in organizations:
        allspice.log.info(f'organization = {organization.name}')

# process all organizations on site
for organization in organizations:

    if organization.name in orgsToMod:
        if DEBUG_ORG:
            allspice.log.info(f'Modifying organization = {organization.name}')

        teamnames = [] 
        for team in teamList:
            teamnames.append(team.name)

        allspice.log.info(f'teamnames={teamnames}')
        orgteams = organization.get_teams()
        
        DEBUG_ORG_TEAMS = True
        for team in orgteams:
            if DEBUG_ORG_TEAMS:
                allspice.log.info(f'org = {organization.name}, Team = {team.name}, Id = {team.id}')

        for team in teamList:
            units_map = team.units_map
            teamToMod = organization.get_team(team.name)
            
            # If the team doesn't exist create_team
            # else: modify team
            if (teamToMod == None):
                teamToMod = allspice.hub.create_team(   organization, 
                                                        team.name, 
                                                        team.description,
                                                        team.readWrite,
                                                        team.canCreateOrgRepo,
                                                        team.includesAllRepos, 
                                                        units, 
                                                        units_map)            
                if (DEBUG_TEAMS):
                    allspice.log.info(f'Modifying organization = {organization.name}, creating team = {team.name}')
            else:
                    
                params = { 
                    'description' : team.description,
                    'name'        : team.name,
                }

                foo = allspice.hub.modify_team(teamToMod.id, params)
                allspice.log.info(f'Modifying organization = {organization.name}, modifying team = {team.name}')


            # Add users to team
            for email in team.memberEmails:
                user = allspice.hub.get_user_by_email(email)
                if DEBUG_EMAILS:
                    allspice.log.info(f'Modifying organization: {organization.name}, team {team.name}, adding email={email}')
                
                if teamToMod is not None:
                    teamToMod.add_user(user)

