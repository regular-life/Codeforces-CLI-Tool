#!/bin/bash

# ANSI escape codes for colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # Reset color

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Function to print feedback message
print_feedback() {
    echo -e "${GREEN}$1 ✔${NC}"
}

# Check if Python3 is installed
if command -v python3 &> /dev/null
then
    print_feedback "Python3 found"
else
    # Display warning message in red
    echo -e "${RED}WARNING: Python3 could not be found. You need to download and install python3 first before being able to use this tool.${NC}"
    exit
fi

cd "$SCRIPT_DIR" > /dev/null
cd .. > /dev/null

VENV_USE=true
if [ ! -d ".env" ]; then
    VENV_USE=false
fi

activate_venv() {
    if [ "$VENV_USE" = true ]; then
        source .env/bin/activate
    fi
}

deactivate_venv() {
    if [ "$VENV_USE" = true ]; then
        deactivate
    fi
}

activate_venv
python3 options/GetAlarm.py
deactivate_venv