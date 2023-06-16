# initialize.sh

# Initializes directory

Prepends project filenames with repo name. All *.prjpcb, *.schdoc, *.pcbdoc.

For example telemetry.prjpcb in repo "rocket" would change to "rocket_telemetry.prjpcb"

## Prerequisites

Make sure you have the following prerequisites installed:

- Bash shell (usually pre-installed on Unix-like systems) or git for windows
- Git (if the script uses Git commands)

## Instructions

1. Open a terminal or command prompt.

2. Make the script executable if it isn't already by running the following command:
    ```
    chmod +x initialize.sh
    ```

3a. To run the script without adding it to the path, use the full path to the script. 

In this example the source script is here:
``` 
 ~/Documents/git-demos/APIDemos/InitializeRepo/initialize.sh . 
```

Change directory to your git directory. In this example this is our target git directory:

``` 
 cd ~/Documents/git-demos/ArchimajorDemo
```

Here is an example of the script being run on this ArchimajorDemo repo:
``` 
danie@floorputer MINGW64 ~/Documents/git-demos/ArchimajorDemo (demo_feature)
$ ~/Documents/git-demos/APIDemos/InitializeRepo/initialize.sh .
Already up to date.
Modified: ./Archimajor.SchDoc -> ./ArchimajorDemo_Archimajor.SchDoc
Modified: ./Connectors.SchDoc -> ./ArchimajorDemo_Connectors.SchDoc
Modified: ./EndStops.SchDoc -> ./ArchimajorDemo_EndStops.SchDoc
Modified: ./Fans.SchDoc -> ./ArchimajorDemo_Fans.SchDoc
Modified: ./Microcontroller.SchDoc -> ./ArchimajorDemo_Microcontroller.SchDoc
Modified: ./Mosfets.SchDoc -> ./ArchimajorDemo_Mosfets.SchDoc
Modified: ./Mosfets_alt.SchDoc -> ./ArchimajorDemo_Mosfets_alt.SchDoc
Modified: ./Motors.SchDoc -> ./ArchimajorDemo_Motors.SchDoc
Modified: ./Power.SchDoc -> ./ArchimajorDemo_Power.SchDoc
Modified: ./Thermistors.SchDoc -> ./ArchimajorDemo_Thermistors.SchDoc
Modified: ./Thermocouples.SchDoc -> ./ArchimajorDemo_Thermocouples.SchDoc
Modified: ./USB.SchDoc -> ./ArchimajorDemo_USB.SchDoc
Modified: ./Archimajor.PrjPcb -> ./ArchimajorDemo_Archimajor.PrjPcb
Modified: ./Archimajor.PcbDoc -> ./ArchimajorDemo_Archimajor.PcbDoc
```


3b. If you would like to add the initialize script directory, then you need to add the command to your path.
``` 
export PATH=$PATH:"[path to directory]"
```

Example path:
``` 
export PATH=$PATH:"C:\Users\danie\Documents\git-demos\APIDemos\InitializeRepo"
```

4. The script can be run by passing it any directory, including ".", the current dir.
```
./initialize.sh git_directory
```
Replace "git_directory" with your git project directory.

5. The script will perform the defined modifications on the specified files based on the defined suffixes. The modified files will be renamed with the repository name as a prefix.

6. The script will display messages indicating the modifications made to the files.

7. Once the script finishes, check the desired directory to see the modified files.

## Customization

You can customize the script by modifying the variables and logic within the script file:

- `suffixes`: Update this variable to contain the desired list of file suffixes you want to modify.


- Script logic: You can modify the script logic, such as the file modification operations, guard clauses, or additional functionality to suit your specific requirements.

Feel free to modify and adapt the script to meet your specific needs.
