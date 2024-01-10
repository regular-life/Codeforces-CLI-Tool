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

# Check if virtualenv is installed
if command -v virtualenv &> /dev/null
then
    print_feedback "virtualenv found"
else
    # Display warning message in red
    echo -e "${RED}WARNING: Python virtualenv could not be found. You need to download and install virtualenv first before being able to use this tool.${NC}"
    exit
fi

# Make virtualenv named .env and install modules from requirements.txt
virtualenv .env && print_feedback "virtualenv created"
source .env/bin/activate && print_feedback "virtualenv activated"
pip install -r requirements.txt && print_feedback "requirements installed"

# Add the current working directory to the PATH environment variable
echo '# cftool path. added by install-venv-setup.sh' >> $YOUR_TERMINAL_RC_FILE
echo 'export PATH=$PATH:'$(pwd) >> $YOUR_TERMINAL_RC_FILE
print_feedback "PATH added to $YOUR_TERMINAL_RC_FILE"

# Give execute permission to the cftool script
chmod +x cftool && print_feedback "cftool script made executable" || echo -e "${RED}WARNING: cftool script could not be made executable. You need to give execute permission to the cftool script manually.${NC}"
