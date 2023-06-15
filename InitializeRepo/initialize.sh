#!/bin/bash
set -euo pipefail

git pull

# Check if a directory argument is provided
if [ -z "$1" ]; then
  echo "Please provide a directory name as an argument."
  exit 1
fi

# Store the directory argument
directory="$1"

if ! git pull > /dev/null 2>&1; then
    echo "Not in a git repository, couldn't pull"
fi


suffixes=("schdoc" "prjpcb" "pcbdoc")  # Replace with your desired list of suffixes

path=$(git rev-parse --show-toplevel) 

reponame=$(basename "$path")

# Loop through each suffix
for suffix in "${suffixes[@]}"; do
    # Find all files with .foo extension (case-insensitive) and loop through them
    find "${directory}" -type f -iname "*.${suffix}" | while read -r file; do
    # Get the directory path and the base filename
        dir_path=$(dirname "$file")
        base_name=$(basename "$file")

        # Check if the base filename already contains the prefix
        if echo "$base_name" | grep -q "^${reponame}"; then
            echo "Skipping: ${dir_path}/${base_name} (Already modified)"
            continue
        fi

        
        # Prepend the prefix to the base filename
        new_name="${reponame}_${base_name}"
        
        # Rename the file
        mv "$file" "${dir_path}/${new_name}"
        
        echo "Modified: ${dir_path}/${base_name} -> ${dir_path}/${new_name}"
    done
done
