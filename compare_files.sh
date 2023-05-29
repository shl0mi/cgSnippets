#!/bin/bash

# The directories
dir1="/path/to/folder1"
dir2="/path/to/folder2"

# Prefix for files in the second directory
prefix="translated_"

# Header for the output
printf "%-20s %10s %10s\n" "File" "Original Lines" "Translated Lines"

# Loop over all files in the first directory
for file in "$dir1"/*; do
    # Get the base filename without the directory
    base=$(basename "$file")

    # Corresponding file in the second directory
    file2="$dir2/$prefix$base"

    # Check if this file exists
    if [ -e "$file2" ]; then
        # Count the non-empty lines in each file
        count1=$(grep -cvP '^\s*$' "$file")
        count2=$(grep -cvP '^\s*$' "$file2")

        # Print the result with fixed width for each column
        printf "%-20s %10s %10s\n" "$base" "$count1" "$count2"
    fi
done
