#!/bin/bash

# The directories
dir1="/path/to/folder1"
dir2="/path/to/folder2"

# Prefix for files in the second directory
prefix="translated_"

# Find the longest filename in dir1
max_length=0
for file in "$dir1"/*; do
    base=$(basename "$file")
    length=${#base}
    if (( length > max_length )); then
        max_length=$length
    fi
done

# Add 5 to max_length for some padding
((max_length+=5))

# Header for the output
printf "%-*s %10s %10s\n" "$max_length" "File" "Original Lines" "Translated Lines"

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
        printf "%-*s %10s %10s\n" "$max_length" "$base" "$count1" "$count2"
    fi
done
