#!/bin/bash

# Add the current working directory to the PATH environment variable
echo 'export PATH=$PATH:'$(pwd) >> ~/.zshrc

# Give execute permission to the cftool script
chmod +x cftool
