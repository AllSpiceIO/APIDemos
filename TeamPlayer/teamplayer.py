# changeteamname.py
# changes an organization teamname


# loads values from json file and modifies teamname


# Load the allspice/gitea module
import os
import sys
sys.path.append('..')
from allspice_proto.allspice_proto import AllSpice_Proto
allspice = AllSpice_Proto()
if (allspice.start() is False):
    quit()


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
parser = argparse.ArgumentParser(prog = __file__, description='adds or modifies teams')
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
        teamsToMod['teamsToModify'] is None or
        teamsToMod['orgsToModify']  is None
    ):
    allspice.log.error(f'Can\'t parse filename {args.filename}', teamsToMod={teamsToMod})
    quit()

allspice.log.info(f'{__file__}, {allspice.URL} python script')

orgs = None
try:
    orgs = allspice.hub.get_orgs();
    
except: 
    allspice.log.error(f'failure on orgs = allspice.hub.get_orgs() - check permission')
    quit()

orgnames = []
orgDict = {}
DEBUG_GET_ORGS = False
if (DEBUG_GET_ORGS):
    allspice.log.info(f'orgs={orgs}')
for org in orgs:
    orgDict[org.name] = org
    orgnames.append(org.name)

for orgMod in teamsToMod['orgsToModify']:
    if orgMod not in orgnames:
        allspice.log.error(f'orgMod = {orgMod} not in organization list on server')
    
DEBUG_ORG_NAMES = False
if DEBUG_ORG_NAMES:
     allspice.log.info(f'orgs={orgs}')


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




for orgname in teamsToMod['orgsToModify']:

    # For each of the teamsToModify objects in the json file
    for teamMods in teamsToMod['teamsToModify']:
        
        # Log team dict object
        DEBUG_TEAMNAME = False
        if DEBUG_TEAMNAME:
            allspice.log.info(f'teamMods={teamMods}')
        
        # get organization's teams and check to see if oldTeamName is a team
       
        description  = teamMods['description']
        permission   = teamMods['permission']
        canCreateOrgRepo = teamMods['can_create_org_repo']
        includesAllRepos = teamMods['includes_all_repositories']
        units_map = teamMods['units_map']
        teamname = teamMods['name']
        thisorg = None
        teamOnServer = False
        thisTeam = None
        teamID = 0
        try:
            thisorg = orgDict[orgname]
            thisTeam = thisorg.get_team(teamname)



            if thisTeam == None:
                print("this")
                thisTeam = allspice.hub.create_team(    thisorg, 
                                                        teamname, 
                                                        teamMods['description'],
                                                        teamMods['permission'],
                                                        teamMods['can_create_org_repo'],
                                                        teamMods['includes_all_repositories'],
                                                        units, 
                                                        teamMods['units_map'])   

            else:

                # print("that")
                if thisTeam.id == 0:
                    allspice.log.error(f'TeamID is 0, teamname={teamname}')
                    quit()

                params = { 
                    'name'                      : teamname,
                    'description'               : teamMods['description'],
                    'permission'                : teamMods['permission'],
                    'can_create_org_repo'       : teamMods['can_create_org_repo'],
                    'includes_all_repositories' : teamMods['includes_all_repositories'],
                    'units'                     : units,
                    'units_map'                 : teamMods['units_map']    
                }

                foo = allspice.hub.modify_team(thisTeam.id, params)
                allspice.log.info(f'Modifying organization = {thisorg.name}, modifying team = {teamname}')
        except:
            allspice.log.error(f'error {orgname}.getTeams()')
            quit()

        
        # Add users to team
        for email in teamMods['emailList']:
            user = allspice.hub.get_user_by_email(email)
            DEBUG_EMAILS = False
            if DEBUG_EMAILS:
                allspice.log.info(f'Modifying organization: {thisorg.name}, team {teamname}, adding email={email}')
            
            if thisTeam is not None:
                thisTeam.add_user(user)


allspice.log.info(f'{__file__} completed')