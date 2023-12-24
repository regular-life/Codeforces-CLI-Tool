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

import json
import getpass

# from utils.encrypt import *

# Function to save credentials
def save_credentials(username, password):
    credentials = {'username': username, 'password': password}
    with open('secrets/credentials.json', 'w') as file:
        json.dump(credentials, file)

# Function to load credentials
def load_credentials():
    try:
        with open('secrets/credentials.json', 'r') as file:
            credentials = json.load(file)
            username = credentials.get('username', '')
            password = credentials.get('password', '')
            return username, password
    except:
        username = input("Enter your Codeforces username: ")
        password = getpass.getpass("Enter your Codeforces password: ")
        save_credentials(username, password)
        return username, password

if __name__ == '__main__':
    username, password = load_credentials()
    print("Username: " + username)
    print("Password: " + password)