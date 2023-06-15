#!/bin/bash

git pull > /dev/null

suffixes=("schdoc" "prjpcb" "pcbdoc")  # Replace with your desired list of suffixes

path=$(git rev-parse --show-toplevel) 

reponame=$(basename "$path")

# Loop through each suffix
for suffix in "${suffixes[@]}"; do
    # Find all files with .foo extension (case-insensitive) and loop through them
    find "." -type f -iname "*.${suffix}" | while read -r file; do
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
