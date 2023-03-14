# repos.py

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
# allspice.hub.logEveryEndpoint(True)

delayserver()

from pygitea_mod.gitea.apiobject import Repository


# -----------------------------------------------------------------------------
allspice.infoheader("Test GET /version")
# test GET server version
versionResponse = ""
try:
    versionResponse = allspice.hub.get_version()
    delayserver()
except:
    allspice.log.error(f'failure to gitea.get_version()')
    quit()

allspice.log.info(f'/version, Allspice Version: {versionResponse}')


# -----------------------------------------------------------------------------
try:
    result = allspice.hub.getRepoJSON("AllSpiceUser", "ArchimajorFork", "Mosfets.SchDoc")
    allspice.log.info(f"JSON obj size:{len(result)}")
    print(result)

except:
    allspice.log.error("Failure to getRepoJSON")
    quit()


