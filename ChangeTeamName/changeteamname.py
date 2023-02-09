# changeteamname.py
# changes an organization teamname


# loads values from json file and modifies teamname


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


import argparse
parser = argparse.ArgumentParser(prog = __file__, description='Changes name of team')
# parser.parse_args()
parser.add_argument('filename')
args = parser.parse_args()

# Log filename
DEBUG_FILENAME = False
if DEBUG_FILENAME:
    allspice.log.info(f'args.filename={args.filename}')


import json
teamsToMod=None
with open(args.filename, 'r') as file:    
    
    # Parse input file into an array of teams
    # example : teamToChangeExample.Json 
    teamsToMod = json.load(file)
    
    # Log teams object
    DEBUG_JSON_LOAD = False
    if DEBUG_JSON_LOAD:
        allspice.log.info(f'teamsToMod={teamsToMod}')

# Vaguely check for json parsing failure
if (    teamsToMod                  is None or
        teamsToMod['teamsToModify'] is None
    ):
    allspice.log.error(f'Can\'t parse filename {args.filename}', teamsToMod={teamsToMod})
    quit()



# canCreateOrgRepo = True
# readWrite = "write"
# teamList.append( Team("ChupChups", 
#                         "update description",
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
#                             "repo.releases": "read",
#                             "repo.wiki": "write"
#                         }, 
#                         ["daniel@allspice.io", "daniel+mikachanical@allspice.io"]))

# # permission units, associated with units_map
# units=(
#             "repo.code",
#             "repo.issues",
#             "repo.ext_issues",
#             "repo.wiki",
#             "repo.pulls",
#             "repo.releases",
#             "repo.ext_wiki",
#     )


# # --------------------------------------------------
# # Start script

# DEBUG_EMAILS   = False
# DEBUG_ORG_LIST = False
# DEBUG_ORG      = False
# DEBUG_TEAMS    = True


allspice.log.info(f'{__file__}, {allspice.URL} python script')

orgs = allspice.hub.get_orgs();
orgnames = []
orgDict = {}
DEBUG_GET_ORGS = False
if (DEBUG_GET_ORGS):
    allspice.log.info(f'orgs={orgs}')
for org in orgs:
    orgDict[org.name] = org
    orgnames.append(org.name)
    
DEBUG_ORG_NAMES = False
if DEBUG_ORG_NAMES:
     allspice.log.info(f'orgs={orgs}')




# For each of the teamsToModify objects in the json file
for teamMods in teamsToMod['teamsToModify']:
    
    # Log team dict object
    DEBUG_TEAMNAME = False
    if DEBUG_TEAMNAME:
        allspice.log.info(f'teamMods={teamMods}')

    # verify org from file is in list of orgs from server
    orgname = teamMods['organization']
    if orgname not in orgnames:
        allspice.log.error(f'org does not exist = {orgname}')
        quit()
    
    # get organization's teams and check to see if oldTeamName is a team
    thisorg = None
    theseTeams = None
    teamOnServer = False
    oldTeamname = teamMods['oldTeamName']
    try:
        thisorg = orgDict[orgname]
        theseTeams = thisorg.get_teams()
        for thisTeam in theseTeams:
            print(f'-------->{thisorg.name}.{thisTeam.name}')
            if thisTeam.name is oldTeamname :
                teamOnServer = True
                break;
    except:
        allspice.log.error(f'error {orgname}.getTeams()')
        quit()

    if teamOnServer is False:
        allspice.log.error(f'error {orgname}.getTeams(), teamname = {oldTeamname} not on server')
        
    
    
    #print(orgs)

    # Check for current team
    # allspice.hub.get



# # get all organization names
# organizations = allspice.hub.get_orgs()
# if DEBUG_ORG_LIST:
#     allspice.log.info(f'organization list')
#     for organization in organizations:
#         allspice.log.info(f'organization = {organization.name}')

# # process all organizations on site
# for organization in organizations:

#     if organization.name in orgsToMod:
#         if DEBUG_ORG:
#             allspice.log.info(f'Modifying organization = {organization.name}')

#         teamnames = [] 
#         for team in teamList:
#             teamnames.append(team.name)

#         allspice.log.info(f'teamnames={teamnames}')
#         orgteams = organization.get_teams()
        
#         DEBUG_ORG_TEAMS = True
#         for team in orgteams:
#             if DEBUG_ORG_TEAMS:
#                 allspice.log.info(f'org = {organization.name}, Team = {team.name}, Id = {team.id}')

#         for team in teamList:
#             units_map = team.units_map
#             teamToMod = organization.get_team(team.name)
            
#             # If the team doesn't exist create_team
#             # else: modify team
#             if (teamToMod == None):
#                 teamToMod = allspice.hub.create_team(   organization, 
#                                                         team.name, 
#                                                         team.description,
#                                                         team.readWrite,
#                                                         team.canCreateOrgRepo,
#                                                         team.includesAllRepos, 
#                                                         units, 
#                                                         units_map)            
#                 if (DEBUG_TEAMS):
#                     allspice.log.info(f'Modifying organization = {organization.name}, creating team = {team.name}')
#             else:
                    
#                 params = { 
#                     'description' : team.description,
#                     'name'        : team.name,
#                 }

#                 foo = allspice.hub.modify_team(teamToMod.id, params)
#                 allspice.log.info(f'Modifying organization = {organization.name}, modifying team = {team.name}')


#             # Add users to team
#             for email in team.memberEmails:
#                 user = allspice.hub.get_user_by_email(email)
#                 if DEBUG_EMAILS:
#                     allspice.log.info(f'Modifying organization: {organization.name}, team {team.name}, adding email={email}')
                
#                 if teamToMod is not None:
#                     teamToMod.add_user(user)

