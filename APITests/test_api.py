import sys
sys.path.append('..')
from allspice.allspice import AllSpice
allspice = AllSpice()
## allspice = None
class TestApi(object):

  
    def test_alwaysPass(self):
        assert True

    def test_allspiceNotNone(self):
        assert allspice is not None
        
    def test_allspice_start(self):
        assert allspice.start()

    def test_version(self):
        versionResponse = ""
        try:
            versionResponse = allspice.hub.get_version()
        except:
            allspice.log.error(f'failure to gitea.get_version()')
            assert False

        allspice.log.info(f'Allspice Version: {versionResponse}')
        assert True


    def test_user(self):
        username = ""
        try:
            username = allspice.hub.get_user().username
        except:
            allspice.log.error(f'failure to gitea.get_user()')
            assert False

        allspice.log.info(f'Allspice user: {username}')
        assert True
       
