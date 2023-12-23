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