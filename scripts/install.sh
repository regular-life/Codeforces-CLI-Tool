#!/bin/bash

# ANSI escape codes for colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # Reset color

# Set the terminal rc file where the path will be added
YOUR_TERMINAL_RC_FILE=~/.bashrc

# Function to print feedback message
print_feedback() {
    echo -e "${GREEN}$1 ✔${NC}"
}

# Check if Python is installed
if command -v python &> /dev/null
then
    print_feedback "Python found"
else
    # Display warning message in red
    echo -e "${RED}WARNING: Python could not be found. You need to download and install python first before being able to use this tool.${NC}"
    exit
fi

# pip 23.3.2

# Install requirements.txt
pip install -r requirements.txt
# if successful, print feedback message
# check success
if [ $? -eq 0 ]; then
    print_feedback "requirements.txt installed"
else
    echo -e "${RED}WARNING: requirements.txt could not be installed. You need to install the requirements manually.${NC}"
fi

# Add the current working directory to the PATH environment variable
echo '# cftool path. added by install.sh' >> $YOUR_TERMINAL_RC_FILE
echo 'export PATH=$PATH:'$(pwd) >> $YOUR_TERMINAL_RC_FILE
print_feedback "PATH added to $YOUR_TERMINAL_RC_FILE"

# Give execute permission to the cftool script
chmod +x cftool && print_feedback "cftool script made executable" || echo -e "${RED}WARNING: cftool script could not be made executable. You need to give execute permission to the cftool script manually.${NC}"

# delete .env folder if exists
if [ -d ".env" ]; then
    rm -rf .env
fi
print_feedback ".env folder deleted"
