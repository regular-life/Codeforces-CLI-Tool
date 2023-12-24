"""
Copyright (C) 2023 yash

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import ruamel.yaml

CONFIG_FILE_PATH = 'config/config.yml'

yaml_str="""\
file_named_by_question_ID: true
# for question 1900A, the file name is 1900A.cpp or some other compiler

# if you want to use the question ID as the file name, set this to true
# otherwise, set this as false

# default: true

headless_browser: false
# whether you want to see the browser or not

# if you want to use headless browser, set this to true. this will be faster, but you won't be able to see the browser and what's going on there. tought if there is an issue which only appears on the screen, and not reflected on terminl
# otherwise, set this as false

# default: false (for testing); set this as true later
"""

# Read the config file
def read_config():
    try:
        with open(CONFIG_FILE_PATH, 'r') as file:
            config = ruamel.yaml.YAML().load(file)
        return config
    except FileNotFoundError:
        # Create the config file if it doesn't exist
        print("file did not exist before :0 , it has been created now")
        with open(CONFIG_FILE_PATH, 'w') as file:
            ruamel.yaml.YAML().dump(yaml_str, file)
        return read_config()

# Update the config
def update_config(st_file_naming, st_browser_visibility):
    config = read_config()
    config["file_named_by_question_ID"] = st_file_naming
    config["headless_browser"] = st_browser_visibility
    with open(CONFIG_FILE_PATH, 'w') as file:
        ruamel.yaml.YAML().dump(config, file)

if __name__ == "__main__":
    # Example usage
    config = read_config()
    print("Current config:\n", config)
    
    print("Do you want to make changes in the config? (yes/no): ", end="")
    user_input = input().lower()
    if not user_input.__contains__("y"):
        print("No changes made.")
        exit()
    
    st_file_naming = config["file_named_by_question_ID"]
    st_browser_visibility = config["headless_browser"]

    # Prompt the user to update the config
    user_input = input("Do you want to use the question ID as the file name? (yes/no): ").lower()
    if user_input.__contains__("y"):
        if not st_file_naming:
            update_config(True, st_browser_visibility)
            print("Config updated.")
        else:
            print("Config already set to true.")
    else:
        if st_file_naming:
            update_config(False, st_browser_visibility)
            print("Config updated.")
        else:
            print("Config already set to false.")
        
    st_file_naming = config["file_named_by_question_ID"]
    st_browser_visibility = config["headless_browser"]
        
    user_input = input("Do you want to the browser to be visible? (yes/no): ").lower()
    if user_input.__contains__("y"):
        if not st_browser_visibility:
            update_config(st_file_naming, True)
            print("Config updated.")
        else:
            print("Config already set to true.")
    else:
        if st_browser_visibility:
            update_config(st_file_naming, False)
            print("Config updated.")
        else:
            print("Config already set to false.")