# GetRepoBOM.py

## Summary
prints a BOM from a repo

Reads .prjpcb file, compiles list of schematics, 
    requests json/dict for each schematic
    parses schematic dict for component attributes
    prints component attributes 

example uses csv output


## Usage
From the command line, create two environmental variables
This example uses bash

```
export ALLSPICE_URL="https://hub.allspice.io"

export ALLSPICE_ACCESS_TOKEN="your-access-token"

```

To run:
```
python3 getRepoBOM.py > youroutfile.csv

```

If you need help, check out our tutorial on [how to create an AllSpice access token](https://allspice.document360.io/docs/how-to-create-an-allspice-authentication-application-access-token).
