#!/bin/bash

# Check if script was called with the required argument
if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory> <fraction>"
    exit 1
fi

directory=$1
fraction=$2
output_file="output.txt"

# Count total lines across all files in the directory
total_lines_in_dir=$(find $directory -type f -exec wc -l {} + | tail -n 1 | awk '{print $1}')

# Calculate target number of lines
target_lines=$(echo "$total_lines_in_dir*$fraction" | bc | awk '{print int($1+0.5)}')

# Initial count of lines
total_lines=0

# Remove the output file if it exists
rm -f $output_file

# Loop over all files in the specified directory
for file in $(find $directory -type f); do
    # Count lines in the current file
    current_lines=$(wc -l < "$file")
    
    # Check if total lines exceed the target count
    if (( total_lines + current_lines > target_lines )); then
        break
    fi

    # Concatenate current file to output file
    cat "$file" >> $output_file
    
    # Add a newline character to output file
    echo "" >> $output_file

    # Add the lines from the current file to the total
    total_lines=$((total_lines + current_lines))
done

echo "Operation finished. Total lines in $output_file: $total_lines"
