import logging
import os

import sys
sys.path.append('..')
from pygitea_mod.gitea.gitea import Gitea


# importing Py-gitea
# https://github.com/Langenfeld/py-gitea
# from gitea.gitea import Gitea


class AllSpice_Proto(object):
    # units_map is the read/write permissions
    def __init__(self):
        self.foo = "foo"
        
        try:
            self.log = logging
            LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
            self.log.basicConfig(level=LOGLEVEL, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')
        except:
            print("fatal error setting up logging")

    
    def __str__(self) -> str:
        teamStr = f'no __str__ for allspice'
        return teamStr

    def baz(self):
        print("baz")
    
    def version(self):
        print("v0.5")

    def start(self):

        # Load URL and access token from environmental variables
        try:
            self.URL = os.environ['ALLSPICE_URL']
            # URL = "https://allspice.dev"
        except:
            self.log.error(f'ALLSPICE_URL is None, run >export ALLSPICE_URL="yourURL"')
            return False

        try:
            TOKEN = os.environ['ALLSPICE_ACCESS_TOKEN']
        except:
            self.log.error(f'ALLSPICE_ACCESS_TOKEN is None, run >export ALLSPICE_ACCESS_TOKEN="token", create token at {self.URL}/user/settings/applications')
            self.log.error(f'ALLSPICE_ACCESS_TOKEN is None, follow instructions to generate token: https://allspice.document360.io/docs/how-to-create-an-allspice-authentication-application-access-token')
            return False


        # create website object  
        allspice = None
        # URL = "https://hub.allspice.io"
        try:
            self.hub = Gitea(self.URL, TOKEN)
        except:
            self.log.error(f'Failure on gitea = Gitea(URL, TOKEN), i.e gitea = Gitea({self.URL}, **hidden**), {self.hub}')

        return True

    foo="bar"
    log = None
    hub = None
    ULR = ""



