# Codeforces Tool (cftool)

## Overview:

The Codeforces Tool (cftool) is a command-line utility designed to streamline various interactions with the Codeforces platform. Whether you want to submit code, check your recent submission status, view upcoming contests, or manage credentials, cftool provides a simple and efficient way to navigate Codeforces functionalities.

## Table of Contents:

1. [Installation](#installation)
2. [Usage](#usage)
3. [Options](#options)
4. [File Structure](#file-structure)
5. [Getting Started](#getting-started)
6. [Future Targets](#future-targets)
7. [Technologies Used](#technologies-used)
8. [Acknowledgements](#acknowledgements)

## Installation:

  - **Download the Project:**
    Clone the repository to your local machine using the following command:
    ```bash
    git clone https://github.com/regular-life/cftool
    ```
    **OR**
    Download the .zip file from [cftool GitHub Repository](https://github.com/regular-life/cftool).

  - **Navigate to Project Directory:**
    Open a terminal and navigate to `cftool` directory.

  - **Run Installation Script:**
    Run the installation script to set up the virtual environment and install dependencies:
    ```bash
    make install
    ```
  
  - **Add Project to PATH:**
    This script also adds the project directory to your PATH for easy access.
    If there is an issue with this make suitable changes in `install.sh` and do `make install` again.

## Usage:

You can run cftool with various options to perform specific tasks:

```bash
cftool [--submit | --status | --contests | --my-stats | --my-contests | --credentials | --config | --blogs | --help]
```

## Options:

- **--submit:** Run cftool for submitting your code.
- **--status:** Display the most recent submission status and details.
- **--contests:** Display upcoming contests on CodeForces along with the countdown.
- **--my-stats:** Display statistics such as your rating, the number of problems you've solved, and a comparison of problems solved versus rating for your ID.
- **--my-contests:** View information related to the five most recent contests and your performance in these contests.
- **--credentials:** Manage cftool credentials.
- **--config:** View and make changes to the configuration settings for cftool.
- **--blogs:** View the most recent blogs from Codeforces.
- **--help:** Display this help message.

## File Structure:
```
project-root/
|-- .env                   # Virtual environment files
|-- classes/               # Directory containing classes
|   |-- CF.py
|-- config/                # Configuration files
|   |-- config_interpreter.py
|   |-- config.yml
|-- options/               # Directory containing scripts for different options
|   |-- getBlogs.py
|   |-- getContests.py
|   |-- getMyContests.py
|   |-- getMyStats.py
|   |-- Submit.py
|-- secrets/               # Directory for storing sensitive information
|   |-- credentials.json
|-- utils/                 # Directory containing utility scripts
|   |-- compilerToCode.py
|   |-- credentials.py
|   |-- encrypt.py
|   |-- getCompiler.py
|   |-- getQuestionID.py
|   |-- getSubmissionStatusDetails.py
|-- cftool                 # Main script (shell script)
|-- help.txt               # Usage instructions
|-- install.sh             # Installation script
|-- Makefile               # Makefile for installation
```

## Getting Started:

Ensure you have the required packages installed and add the project directory to your PATH using the provided installation script. Run cftool with the desired options to interact with Codeforces effortlessly.

## Future Targets:

We are actively working on improving cftool. Future features may include:

- Enhanced contest analytics.
- Integrated code debugging tools.
- Support for additional online judges.
- User-specific customization options.

## Technologies Used:

- Python
- Python VirtualEnv
- Bash
- Selenium for Web Scraping
- Requests library
- Pytz library
- YML for config
- OOPS applied where possible

## Acknowledgements:

Special thanks to [Sanyam Garg](https://github.com/SanyamGarg12) for suggesting more features that can be added and the ideation of the project.
I would also like to thank the Codeforces platform and the developer community.

Feel free to contribute, report issues, or suggest new features. Happy coding!

---