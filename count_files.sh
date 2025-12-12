#!/bin/bash

DIR="/etc"

if [ -d "$DIR" ]; then
    total_files=$(find "$DIR" -type f | wc -l)
    echo "Number of files in $DIR: $total_files"
else
    echo "Directory $DIR does not exist."
    exit 1
fi
