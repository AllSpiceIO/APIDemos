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
    newTeamName = teamMods['newTeamName']
    thisorg = None
    theseTeams = None
    newTeamOnServer = False
    oldTeamOnServer = False
    oldTeamname = teamMods['oldTeamName']
    teamID = 0
    try:
        thisorg = orgDict[orgname]
        theseTeams = thisorg.get_teams()
        for thisTeam in theseTeams:
            if thisTeam.name == oldTeamname:
                oldTeamOnServer = True
                teamID = thisTeam.id
            if thisTeam.name == newTeamName:
                newTeamOnServer = True
    except:
        allspice.log.error(f'error {orgname}.getTeams()')
        quit()

    # Check for errorsd
    if  (   oldTeamOnServer is False or 
            newTeamOnServer is True or
            teamID == 0 or
            newTeamName is None
    
    ):
        allspice.log.error(f'error {orgname}.getTeams(), oldTeamname = {oldTeamname} on server = {oldTeamOnServer}, newTeamname = {newTeamName} on server = {newTeamOnServer} ')
        quit()

    # setup https post parameters to modify team
    params = { 'name' : newTeamName }

    # Tell the server we want to modify the team with the new name
    try:
       
        response = allspice.hub.modify_team(teamID, params)
        allspice.log.info(f'Modifying organization = {orgname}, modifying team = {oldTeamname}, to {newTeamName}')
    except:
        allspice.log.error(f'error with allspice.hub.modifyTeam({teamID}), Modifying organization = {orgname}, modifying team = {oldTeamname}, to {newTeamName}')

allspice.log.info(f'{__file__} completed')