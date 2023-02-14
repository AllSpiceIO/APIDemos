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

delayserver()



allspice.infoheader("Test /version")
# test GET server version
versionResponse = ""
try:
    versionResponse = allspice.hub.get_version()
    delayserver()
except:
    allspice.log.error(f'failure to gitea.get_version()')
    quit()

allspice.log.info(f'/version, Allspice Version: {versionResponse}')




allspice.infoheader("Test /user")
# test GET /user, get the authenticated user
username = ""
try:
    delayserver()
    username = allspice.hub.get_user().username
    delayserver()
except:
    allspice.log.error(f'User authentication invalid {username}')
    quit()

allspice.log.info(f'/user, API-Token belongs to user: {username}')






allspice.infoheader("Test GET /repos/{owner}/{repo}")
# test GET     /repos/{owner}/{repo}                               Get a repository

serobj = None
userrepos = None
try:
    userobj = allspice.hub.get_user_by_username(username)
    delayserver()
    userrepos = userobj.get_repositories()
    delayserver()
except:
    allspice.log.error('error with user.get_user_object()')
    quit()

repoinfo = f'/users/{username}/repos, '
# loop through every json element and add to log string

# list the repo names
for repo in userrepos:
    repoinfo += f'{repo.name}, '
allspice.log.info(repoinfo)

allspice.infoheader("Test repo object dump")
repoinfo = "repo info dump"
thisrepo = userrepos[0] # arbitrary repo
for key in thisrepo.__dict__:
    thisthing = thisrepo.__dict__[key]
    repoinfo += f'{key} = {thisthing}, '
allspice.log.info(repoinfo)



## API list - if you need a python wrapper or an example from below, contact us at support@allspice with the requested API call 
# for up-to-date api information, visit https://hub.allspice.io/api/swagger

# POST    /repos/migrate                                      Migrate a remote git repository
# GET     /repos/search                                       Search for repositories
# GET     /repos/{owner}/{repo}                               Get a repository
# DELETE  /repos/{owner}/{repo}                               Delete a repository
# PATCH   /repos/{owner}/{repo} Edit a repository's properties. Only fields that are set will be changed.
# GET     /repos/{owner}/{repo}/allspice_generated/json/{filepath}    Get the json blob for a cad file if it exists, otherwise enqueue a new job and return a 503 status. Note: This is still experimental and not yet recommended for critical applications.
# GET     /repos/{owner}/{repo}/allspice_generated/svg/{filepath}     Get the svg blob for a cad file if it exists, otherwise enqueue a new job and return 503 status. Note: This is still experimental and not yet recommended for critical applications.
# GET     /repos/{owner}/{repo}/archive/{archive}             Get an archive of a repository
# GET     /repos/{owner}/{repo}/assignees                     Return all users that have write access and can be assigned to issues
# GET     /repos/{owner}/{repo}/branch_protections            List branch protections for a repository
# POST    /repos/{owner}/{repo}/branch_protections            Create a branch protections for a repository
# GET     /repos/{owner}/{repo}/branch_protections/{name}     Get a specific branch protection for the repository
# DELETE  /repos/{owner}/{repo}/branch_protections/{name}     Delete a specific branch protection for the repository
# PATCH   /repos/{owner}/{repo}/branch_protections/{name}     Edit a branch protections for a repository. Only fields that are set will be changed
# GET     /repos/{owner}/{repo}/branches                      List a repository's branches
# POST    /repos/{owner}/{repo}/branches                      Create a branch
# GET     /repos/{owner}/{repo}/branches/{branch}             Retrieve a specific branch from a repository, including its effective branch protection
# DELETE  /repos/{owner}/{repo}/branches/{branch}             Delete a specific branch from a repository
# GET     /repos/{owner}/{repo}/collaborators                 List a repository's collaborators
# GET     /repos/{owner}/{repo}/collaborators/{collaborator}  Check if a user is a collaborator of a repository
# PUT     /repos/{owner}/{repo}/collaborators/{collaborator}  Add a collaborator to a repository
# DELETE  /repos/{owner}/{repo}/collaborators/{collaborator}  Delete a collaborator from a repository
# GET     /repos/{owner}/{repo}/collaborators/{collaborator}/permission   Get repository permissions for a user
# GET     /repos/{owner}/{repo}/commits                       Get a list of all commits from a repository
# GET     /repos/{owner}/{repo}/commits/{ref}/status          Get a commit's combined status, by branch/tag/commit reference
# GET     /repos/{owner}/{repo}/commits/{ref}/statuses        Get a commit's statuses, by branch/tag/commit reference
# GET     /repos/{owner}/{repo}/contents                      Gets the metadata of all the entries of the root dir
# GET     /repos/{owner}/{repo}/contents/{filepath}           Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
# PUT     /repos/{owner}/{repo}/contents/{filepath}           Update a file in a repository
# POST    /repos/{owner}/{repo}/contents/{filepath}           Create a file in a repository
# DELETE  /repos/{owner}/{repo}/contents/{filepath}           Delete a file in a repository
# POST    /repos/{owner}/{repo}/diffpatch                     Apply diff patch to repository
# GET     /repos/{owner}/{repo}/editorconfig/{filepath}       Get the EditorConfig definitions of a file in a repository
# GET     /repos/{owner}/{repo}/forks                         List a repository's forks
# POST    /repos/{owner}/{repo}/forks                         Fork a repository
# GET     /repos/{owner}/{repo}/git/blobs/{sha}               Gets the blob of a repository.
# GET     /repos/{owner}/{repo}/git/commits/{sha}             Get a single commit from a repository
# GET     /repos/{owner}/{repo}/git/commits/{sha}.{diffType}  Get a commit's diff or patch
# GET     /repos/{owner}/{repo}/git/notes/{sha}               Get a note corresponding to a single commit from a repository
# GET     /repos/{owner}/{repo}/git/refs                      Get specified ref or filtered repository's refs
# GET     /repos/{owner}/{repo}/git/refs/{ref}                Get specified ref or filtered repository's refs
# GET     /repos/{owner}/{repo}/git/tags/{sha}                Gets the tag object of an annotated tag (not lightweight tags)
# GET     /repos/{owner}/{repo}/git/trees/{sha}               Gets the tree of a repository.
# GET     /repos/{owner}/{repo}/hooks                         List the hooks in a repository
# POST    /repos/{owner}/{repo}/hooks                         Create a hook
# GET     /repos/{owner}/{repo}/hooks/git                     List the Git hooks in a repository
# GET     /repos/{owner}/{repo}/hooks/git/{id}                Get a Git hook
# DELETE  /repos/{owner}/{repo}/hooks/git/{id}                Delete a Git hook in a repository
# PATCH   /repos/{owner}/{repo}/hooks/git/{id}                Edit a Git hook in a repository
# GET     /repos/{owner}/{repo}/hooks/{id}                    Get a hook
# DELETE  /repos/{owner}/{repo}/hooks/{id}                    Delete a hook in a repository
# PATCH   /repos/{owner}/{repo}/hooks/{id}                    Edit a hook in a repository
# POST    /repos/{owner}/{repo}/hooks/{id}/tests              Test a push webhook
# GET     /repos/{owner}/{repo}/issue_templates               Get available issue templates for a repository
# GET     /repos/{owner}/{repo}/keys                          List a repository's keys
# POST    /repos/{owner}/{repo}/keys                          Add a key to a repository
# GET     /repos/{owner}/{repo}/keys/{id}                     Get a repository's key by id
# DELETE  /repos/{owner}/{repo}/keys/{id}                     Delete a key from a repository
# GET     /repos/{owner}/{repo}/languages                     Get languages and number of bytes of code written
# GET     /repos/{owner}/{repo}/media/{filepath}              Get a file or it's LFS object from a repository
# POST    /repos/{owner}/{repo}/mirror-sync                   Sync a mirrored repository
# GET     /repos/{owner}/{repo}/pulls                         List a repo's pull requests
# POST    /repos/{owner}/{repo}/pulls                         Create a pull request
# GET     /repos/{owner}/{repo}/pulls/{index}                 Get a pull request
# PATCH   /repos/{owner}/{repo}/pulls/{index}                 Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.
# GET     /repos/{owner}/{repo}/pulls/{index}.{diffType}      Get a pull request diff or patch
# GET     /repos/{owner}/{repo}/pulls/{index}/commits         Get commits for a pull request
# GET     /repos/{owner}/{repo}/pulls/{index}/merge           Check if a pull request has been merged
# POST    /repos/{owner}/{repo}/pulls/{index}/merge           Merge a pull request
# DELETE  /repos/{owner}/{repo}/pulls/{index}/merge           Cancel the scheduled auto merge for the given pull request
# POST    /repos/{owner}/{repo}/pulls/{index}/requested_reviewers     create review requests for a pull request
# DELETE  /repos/{owner}/{repo}/pulls/{index}/requested_reviewers     cancel review requests for a pull request
# GET     /repos/{owner}/{repo}/pulls/{index}/reviews         List all reviews for a pull request
# POST    /repos/{owner}/{repo}/pulls/{index}/reviews         Create a review to an pull request
# GET     /repos/{owner}/{repo}/pulls/{index}/reviews/{id}    Get a specific review for a pull request
# POST    /repos/{owner}/{repo}/pulls/{index}/reviews/{id}    Submit a pending review to an pull request
# DELETE  /repos/{owner}/{repo}/pulls/{index}/reviews/{id}    Delete a specific review from a pull request
# GET     /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments       Get a specific review for a pull request
# POST    /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals     Dismiss a review for a pull request
# POST    /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals   Cancel to dismiss a review for a pull request
# POST    /repos/{owner}/{repo}/pulls/{index}/update                      Merge PR's baseBranch into headBranch
# GET     /repos/{owner}/{repo}/raw/{filepath}                Get a file from a repository
# GET     /repos/{owner}/{repo}/releases                      List a repo's releases
# POST    /repos/{owner}/{repo}/releases                      Create a release
# GET     /repos/{owner}/{repo}/releases/tags/{tag}           Get a release by tag name
# DELETE  /repos/{owner}/{repo}/releases/tags/{tag}           Delete a release by tag name
# GET     /repos/{owner}/{repo}/releases/{id}                 Get a release
# DELETE  /repos/{owner}/{repo}/releases/{id}                 Delete a release
# PATCH   /repos/{owner}/{repo}/releases/{id}                 Update a release
# GET     /repos/{owner}/{repo}/releases/{id}/assets          List release's attachments
# POST    /repos/{owner}/{repo}/releases/{id}/assets          Create a release attachment
# GET     /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}  Get a release attachment
# DELETE  /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}  Delete a release attachment
# PATCH   /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}  Edit a release attachment
# GET     /repos/{owner}/{repo}/reviewers                     Return all users that can be requested to review in this repo
# GET     /repos/{owner}/{repo}/signing-key.gpg               Get signing-key.gpg for given repository
# GET     /repos/{owner}/{repo}/stargazers                    List a repo's stargazers
# GET     /repos/{owner}/{repo}/statuses/{sha}                Get a commit's statuses
# POST    /repos/{owner}/{repo}/statuses/{sha}                Create a commit status
# GET     /repos/{owner}/{repo}/subscribers                   List a repo's watchers
# GET     /repos/{owner}/{repo}/subscription                  Check if the current user is watching a repo
# PUT     /repos/{owner}/{repo}/subscription                  Watch a repo
# DELETE  /repos/{owner}/{repo}/subscription                  Unwatch a repo
# GET     /repos/{owner}/{repo}/tags                          List a repository's tags
# POST    /repos/{owner}/{repo}/tags                          Create a new git tag in a repository
# GET     /repos/{owner}/{repo}/tags/{tag}                    Get the tag of a repository by tag name
# DELETE  /repos/{owner}/{repo}/tags/{tag}                    Delete a repository's tag by name
# GET     /repos/{owner}/{repo}/teams                         List a repository's teams
# GET     /repos/{owner}/{repo}/teams/{team}                  Check if a team is assigned to a repository
# PUT     /repos/{owner}/{repo}/teams/{team}                  Add a team to a repository
# DELETE  /repos/{owner}/{repo}/teams/{team}                  Delete a team from a repository
# GET     /repos/{owner}/{repo}/times                         List a repo's tracked times
# GET     /repos/{owner}/{repo}/times/{user}                  List a user's tracked times in a repo
# GET     /repos/{owner}/{repo}/topics                        Get list of topics that a repository has
# PUT     /repos/{owner}/{repo}/topics                        Replace list of topics for a repository
# PUT     /repos/{owner}/{repo}/topics/{topic}                Add a topic to a repository
# DELETE  /repos/{owner}/{repo}/topics/{topic}                Delete a topic from a repository
# POST    /repos/{owner}/{repo}/transfer                      Transfer a repo ownership
# POST    /repos/{owner}/{repo}/transfer/accept               Accept a repo transfer
# POST    /repos/{owner}/{repo}/transfer/reject               Reject a repo transfer
# POST    /repos/{owner}/{repo}/wiki/new                      Create a wiki page
# GET     /repos/{owner}/{repo}/wiki/page/{pageName}          Get a wiki page
# DELETE  /repos/{owner}/{repo}/wiki/page/{pageName}          Delete a wiki page
# PATCH   /repos/{owner}/{repo}/wiki/page/{pageName}          Edit a wiki page
# GET     /repos/{owner}/{repo}/wiki/pages                    Get all wiki pages
# GET     /repos/{owner}/{repo}/wiki/revisions/{pageName}     Get revisions of a wiki page
# POST    /repos/{template_owner}/{template_repo}/generate    Create a repository using a template
# GET     /repositories/{id}                                  Get a repository by id
# GET     /topics/search                                      search topics via keyword
# POST    /user/repos
