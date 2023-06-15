# initialize.sh

# Initializes director

Prepends project filenames with repo name. All *.prjpcb, *.schdoc, *.pcbdoc.

For example telemetry.prjpcb in repo "rocket" would change to "rocket_telemetry.prj.pcb"

## Prerequisites

Make sure you have the following prerequisites installed:

- Bash shell (usually pre-installed on Unix-like systems)
- Git (if the script uses Git commands)

## Instructions

1. Open a terminal or command prompt.

2. Navigate to the repo directory.

3. Make the script executable if it isn't already by running the following command:
    ```bash
    chmod +x initialize.sh
    ```

4. Execute the script by running the following command:
    ```bash
    ./initialize.sh
    ```

5. The script will perform the defined modifications on the specified files based on the defined suffixes. The modified files will be renamed with the repository name as a prefix.

6. The script will display messages indicating the modifications made to the files.

7. Once the script finishes, check the desired directory to see the modified files.

## Customization

You can customize the script by modifying the variables and logic within the script file:

- `suffixes`: Update this variable to contain the desired list of file suffixes you want to modify.

- `path`: If the script uses Git commands, this variable is set to the repository's root path. If not using Git, you can remove this variable.

- Script logic: You can modify the script logic, such as the file modification operations, guard clauses, or additional functionality to suit your specific requirements.

Feel free to modify and adapt the script to meet your specific needs.
