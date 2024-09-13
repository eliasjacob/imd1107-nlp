#!/bin/bash

# Define URLs
URL1="https://public.jacob.al/imd1107-nlp/binaries.zip"

# Define output file names
OUTPUT1="binaries.zip"

# Download files
echo "Downloading $URL1..."
wget -O $OUTPUT1 $URL1

# Unzip files into respective directories
echo "Unzipping $OUTPUT1"
unzip -o $OUTPUT1

# Clean up zip files
rm $OUTPUT1

echo "Download and extraction complete."