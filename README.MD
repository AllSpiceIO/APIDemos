# AllSpice API Demos

Welcome to AllSpice's api demos. These short programs should help you get started writing your own API interactions.

## Install py-allspice
To get started, download our python module py-allspice [https://pypi.org/project/py-allspice/]

```
pip install py-allspice
```

## Python usage:
```
from gitea import *

allspice = Gitea(URL, TOKEN)

print("AllSpice Version: " + allspice.get_version())
print("API-Token belongs to user: " + allspice.get_user().username)
```

You can read more about apis here: [https://allspice.document360.io/docs/using-the-allspice-api]

If you need to generate an access token, this will help you: [https://allspice.document360.io/docs/how-to-create-an-allspice-authentication-application-access-token]


## Demo folders
- [HelloWorld:](/HelloWorld/) A great place to start to see if everything is working fine
