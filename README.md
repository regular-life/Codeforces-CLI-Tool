# Codeforces CLI Tool (cftool)

## Overview:

The Codeforces Tool (cftool) is a command-line utility designed to streamline various interactions with the Codeforces platform. Whether you want to submit code, check your recent submission status, view upcoming contests, or manage credentials, cftool provides a simple and efficient way to navigate Codeforces functionalities.
Please make sure to read the Getting Started section below.

## Table of Contents:

1. [Installation](#installation)
2. [Usage](#usage)
3. [Options](#options)
4. [File Structure](#file-structure)
5. [Getting Started](#getting-started)
6. [Future Targets](#future-targets)
7. [Technologies Used](#technologies-used)
8. [Acknowledgements](#acknowledgements)
9. [License](#license)

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
    Run the installation script to do the initial setup and installtion of dependencies:
    ```bash
    make install-venv-setup       # if you wish to use virtualenv (will be named .env) setup
    make install                  # if you do not wish to use virtualenv
    ```
  - Open another terminal and start working :) 

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
|-- .env                   # Virtual environment files (if you opt to use virtualenv)
|-- classes/               # Directory containing classes
|   |-- CF_Submit.py
|-- config/                # Configuration files
|   |-- config_interpreter.py
|   |-- config.yml
|-- options/               # Directory containing scripts for different options
|   |-- getBlogs.py
|   |-- getContests.py
|   |-- getMyContests.py
|   |-- getMyStats.py
|   |-- getSubmissionStatusDetails.py
|   |-- Submit.py
|   |-- help.txt           # Usage instructions
|-- scripts/               # Directory containing .sh scripts related to the project
|   |-- install.sh
|   |-- install-venv-setup.sh
|-- secrets/               # Directory for storing sensitive information
|   |-- credentials.json
|-- utils/                 # Directory containing utility scripts
|   |-- compilerToCode.py
|   |-- credentials.py
|   |-- encrypt.py
|   |-- getCompiler.py
|   |-- getQuestionID.py
|-- cftool                 # Main script (shell script)
|-- LICENSE                # GNU GPL License
|-- Makefile               # Makefile for installation
|-- README.md              # Readme of the project
|-- requirements.txt       # File containing the names and versions of all the packages involved. (TIP: you can just do "pip install requirements.txt"
```

## Getting Started:

- Ensure that you have the required packages installed and add the project directory to your `PATH` using the provided installation script.

- Please read and make necessary changes in `config/config.yml`. Additionally, check and define `YOUR_TERMINAL_RC_FILE` in `scripts/install.sh` and `scripts/install-venv-setup.sh`.

- Although `encrypt.py` is currently unused, it will be implemented soon. Or maybe some other encryption format (I need to search for something like this).

- This project has been developed and tested on Arch Linux. While efforts have been made to ensure compatibility with different operating systems, flawless performance on all platforms is not guaranteed.

- Run `cftool` with the desired options to interact with Codeforces effortlessly.

## Future Targets:

We are actively working on improving cftool. Future features may include:

- Problem recommender system.
- Support for additional online judges.
- Option for password reset.
- Encryption-Decryption of username and password.

## Technologies Used:

- Python
- Python VirtualEnv
- Bash
- Selenium for Web Scraping
- Requests library
- Pytz & tzlocal library
- YML for config
- OOPS applied where possible
- CodeForces API

## Acknowledgements:

I would like to thank the Codeforces platform and the developer community.

Feel free to contribute, report issues, or suggest new features. Happy coding!

## License:
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

When distributing this software, you must provide the source code and comply with the terms of the GPL license. If you make modifications to the code, document those changes.

For more details, please refer to the [full text of the GPL license](https://www.gnu.org/licenses/gpl-3.0.html).

---
