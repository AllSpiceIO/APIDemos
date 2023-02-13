# user.py

# A demo script that demonstrates api calls /user

from time import sleep
def delayserver():
    sleep(0.01)
    return


import sys
sys.path.append('..')
from allspice_proto.allspice_proto import AllSpice_Proto
# from allspice.allspice import AllSpice
# allspice = AllSpice()
allspice = AllSpice_Proto()
# delayserver()
allspice.start()
allspice.hub.logEveryEndpoint(True)




# test GET server version
versionResponse = ""
try:
    delayserver()
    versionResponse = allspice.hub.get_version()
except:
    allspice.log.error(f'failure to gitea.get_version()')
    quit()

allspice.log.info(f'/version, Allspice Version: {versionResponse}')

# test GET /user, get the authenticated user
username = ""
try:
    delayserver()
    username = allspice.hub.get_user().username
except:
    allspice.log.error(f'User authentication invalid {username}')
    quit()

allspice.log.info(f'/user, API-Token belongs to user: {username}')

#test GET /users/{username}
# username is from previous example
user = None
try:
    user = allspice.hub.get_user_by_username(username)
except:
    allspice.log.error('error with get_user_by_username()')
    quit()

userinfo = f'/user/{username}, '
# loop through every json element and add to log string
for (key) in user:
    userinfo += f'{key}=%s, ' % user[key].__str__()
allspice.log.info(userinfo)

## Todo list - if you need 

## Applies to authenticated users
#test GET       /user/applications/oauth2 
#test POST      /user/applications/oauth2
#test GET       /user/applications/oauth2/{id}
#test DELETE    /user/applications/oauth2/{id}
#test PATCH     /user/applications/oauth2/{id}

#test GET /user/emails
#test POST /user/emails
#test DELETE /user/emails

#test GET /user/followers
#test GET /user/following
#test GET /user/following/{username}
#test PUT /user/following/{username}
#test DELETE /user/ffollowing{username}

#test GET /user/gpg_key_token
#test POST /user/gpg_key_verify
#test GET /user/user/gpg_keys
#test POST /user/gpg_keys
#test GET /user/gpg_keys/{id}
#test DELETE /user/gpg_keys/{id}

#test GET /user/keys List authenticated user's public keys
#test POST /user/keys create a public key
#test GET /user/keys/{id} get a public key
#test DELETE /user/keys/{id} delete a public key

#test GET /user/repos
#test POST /user/repos
#test GET /user/settings 
#test PATCH /user/settings
#test GET /user/starred
#test GET /user/starred/{owner}/{repo} whether the authenicated is starring the repo
#test PUT /user/starred/{owner}/{repo} star given repo
#test DELETE /userstarred/{owner}/{repo}
#test GET /user/stopwatches
#test GET /user/subscriptions
#test GET /user/teams
#test GET /user/times
#test GET /users/search


## Applies to {username}
#test GET /users/{username}/followers
#test GET /users/{username}/following
#test GET /users/{username}/following/{target} check if one iser is following another user
#test GET /users/{username}/gpg_keys
#test GET /users/{username}/heatmap
#test GET /users/{username}/repos
#test GET /users/{username}/starred
#test GET /users/{username}/subscription
#test GET /users/{username}/tokens
#test POST /users/{username}/tokens create an access token
#test DELETE users/{username}/tokens delete an access token


