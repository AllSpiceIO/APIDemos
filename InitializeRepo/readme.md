# initialize.sh

# Initializes director

Prepends project filenames with repo name. All *.prjpcb, *.schdoc, *.pcbdoc.

For example telemetry.prjpcb in repo "rocket" would change to "rocket_telemetry.prjpcb"

## Prerequisites

Make sure you have the following prerequisites installed:

- Bash shell (usually pre-installed on Unix-like systems) or git for windows
- Git (if the script uses Git commands)

## Instructions

1. Open a terminal or command prompt.

2. Make the script executable if it isn't already by running the following command:
    ```bash
    chmod +x initialize.sh
    ```

3. Make sure the script is either in your path, or add it to your path.
```
export PATH=$PATH:[path to directory]
```

4. Execute the script by running the following command:
    ```bash
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
