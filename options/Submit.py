from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(script_dir, "..")
sys.path.append(project_dir)

from utils.credentials import *
from utils.encrypt import *
from utils.getQuestionID import *
from utils.getSubmissionStatusDetails import *
from utils.compilerToCode import *
from config.config_interpreter import *

from classes.CF import *

if __name__ == "__main__":
    
    if (read_config()["headless_browser"] == True):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode
        
        # Open Chrome browser in headless mode
        driver = webdriver.Chrome(options=chrome_options)
    else:
        # Open Chrome browser
        driver = webdriver.Chrome()
    
    # create object
    cf = CF(driver)
    
    # get file to submit
    filepath = input("Enter the file path: ")
    
    # get questionID and compiler   
    questionID, compiler = getQuestionID(filepath)
    
    # login info
    username, password = load_credentials()
    
    while username is None or password is None:
        username, password = load_credentials()
        
    # check if file name is valid
    if (read_config()["file_named_by_question_ID"] == False):
        questionID = input("Enter the question ID: ")
    
    # submit
    cf.submit(username, password, questionID, compiler, filepath)
    
    time.sleep(1)
    
    # get status
    print(getSubmissionStatusDetails(username))