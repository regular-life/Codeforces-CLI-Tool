#!/bin/bash

# ANSI escape codes for colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # Reset color

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

# Add the current working directory to the PATH environment variable
# Adjust for different shells
if [ -n "$BASH_VERSION" ]; then
    echo '# cftool path. added by install.sh' >> ~/.zshrc
    echo 'export PATH=$PATH:'$(pwd) >> ~/.zshrc
    print_feedback "PATH added to .zshrc"
elif [ -n "$ZSH_VERSION" ]; then
    echo '# cftool path. added by install.sh' >> ~/.zshrc
    echo 'export PATH=$PATH:'$(pwd) >> ~/.zshrc
    print_feedback "PATH added to .zshrc"
else
    echo "Unsupported shell. Please add the following line to your shell configuration file manually:"
    echo "export PATH=\$PATH:$(pwd)"
fi

# Give execute permission to the cftool script
chmod +x cftool
