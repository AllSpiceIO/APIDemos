# Based on https://github.com/Langenfeld/py-gitea



import os
# from gitea import *

# Importing locally from /gitea/gitea/, not the installed py-gitea api
from gitea.gitea import *

# helper class, different than gitea.teams, should merge
from src.team import Team

# Load URL and access token from environmental variables
try:
    URL = os.environ['ALLSPICE_URL']
    # URL = "https://allspice.dev"
except:
    print('ALLSPICE_URL is None, run >export ALLSPICE_URL="https://allspice.dev"')
    quit()


try:
    TOKEN = os.environ['ALLSPICE_ACCESS_TOKEN']
except:
    print (f'ALLSPICE_ACCESS_TOKEN is None, run >export ALLSPICE_ACCESS_TOKEN="token", create token at {URL}/user/settings/applications')
    quit()


# create website object  
gitea = Gitea(URL, TOKEN)

# -----------------------------------------------------
# Setup

# Create list of organizations to modify
orgsToMod = ["UtilityTesting", "ExampleOrganization"]


# Create teams
readWrite = "write"
canCreateOrgRepo = True
includesAllRepos = True
teamList = []
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

print("TeamPlayer python script")
print("Gitea Version: " + gitea.get_version())
print("API-Token belongs to user: " + gitea.get_user().username)


# get all organization names
organizations = gitea.get_orgs()

# process all organizations on site
for organization in organizations:

    if organization.name in orgsToMod:
        print(f'Modifying organization, {organization.name}')

        for team in teamList:
            units_map = team.units_map
            teamToMod = organization.get_team(team.name)
            print(f'Modifying organization: {organization.name}, adding team: {team.name}')
            if (teamToMod == None):
                teamToMod = gitea.create_team(organization, team.name, team.description, team.readWrite, team.canCreateOrgRepo, team.includesAllRepos, units, units_map)            

            # Add users to team
            for email in team.memberEmails:
                user = gitea.get_user_by_email(email)
                if teamToMod is not None:
                    teamToMod.add_user(user)

