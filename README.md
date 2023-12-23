# Codeforces Tool (cftool)

**Overview:**

The Codeforces Tool (cftool) is a command-line utility designed to streamline various interactions with the Codeforces platform. Whether you want to submit code, check your recent submission status, view upcoming contests, or manage credentials, cftool provides a simple and efficient way to navigate Codeforces functionalities.

**Table of Contents:**

1. [Installation](#installation)
2. [Usage](#usage)
3. [Options](#options)
4. [File Structure](#file-structure)
5. [Getting Started](#getting-started)
6. [Future Targets](#future-targets)
7. [Technologies Used](#technologies-used)
8. [Acknowledgements](#acknowledgements)

**1. Installation:**

To install cftool and its dependencies, use the provided installation script:

```bash
make install
```

This script not only installs the required packages but also adds the project directory to your PATH for easy access.

**2. Usage:**

Run cftool with various options to perform specific tasks:

```bash
cftool [--submit | --status | --contests | --my-stats | --my-contests | --credentials | --config | --blogs | --help]
```

**3. Options:**

- **--submit:** Run cftool for submitting your code.
- **--status:** Display the most recent submission status and details.
- **--contests:** Display upcoming contests on CodeForces along with the countdown.
- **--my-stats:** Display statistics such as your rating, the number of problems you've solved, and a comparison of problems solved versus rating for your ID.
- **--my-contests:** View information related to the five most recent contests and your performance in these contests.
- **--credentials:** Manage cftool credentials.
- **--config:** View and make changes to the configuration settings for cftool.
- **--blogs:** View the most recent blogs from Codeforces.
- **--help:** Display this help message.

**4. File Structure:**

- **.env:** Virtual environment files.
- **classes:** CF.py.
- **config:** config_interpreter.py, config.yml.
- **options:** getBlogs.py, getContests.py, getMyContests.py, getMyStats.py.
- **secrets:** credentials.json.
- **utils:** compilerToCode.py, credentials.py, encrypt.py, getCompiler.py, getQuestionID.py, getSubmissionStatusDetails.py.
- **cftool:** Main script (shell script).
- **help.txt:** Usage instructions.
- **install.sh:** Installation script.
- **Makefile:** Makefile for installation.

**5. Getting Started:**

Ensure you have the required packages installed and add the project directory to your PATH using the provided installation script. Run cftool with the desired options to interact with Codeforces effortlessly.

**6. Future Targets:**

We are actively working on improving cftool. Future features may include:

- Enhanced contest analytics.
- Integrated code debugging tools.
- Support for additional online judges.
- User-specific customization options.

**7. Technologies Used:**

- Python
- Bash
- Selenium
- Makefile
- Bash
- Requests library
- Pytz library
- Git for version control

**8. Acknowledgements:**

Special thanks to the Codeforces platform and the developer community for their continuous support.

Feel free to contribute, report issues, or suggest new features. Happy coding!
