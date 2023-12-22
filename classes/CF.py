from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.credentials import *
from utils.encrypt import *
from utils.getQuestionID import *
from utils.compilerToCode import *


class CF:
    
    def __init__(self, driver):
        self.driver = driver
        
    def codeforcesLogin(self, username, password):
        self.driver.get("https://codeforces.com/enter")
        
        # Find the username and password fields and fill them in
        username_field = self.driver.find_element(By.NAME, "handleOrEmail")
        password_field = self.driver.find_element(By.NAME, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)
        
        # Wait till redirect
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://codeforces.com/")
        )
            
    def submit(self, username, password, questionID, compiler, pathToCode):
        # login
        self.codeforcesLogin(username, password)
        
        # navigate to submit page
        url = f"https://codeforces.com/problemset/submit"
        self.driver.get(url)
        
        # Wait till redirect
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://codeforces.com/problemset/submit")
        )
        
        # find and put in contest and question number to submit
        question_code = self.driver.find_element(By.NAME, "submittedProblemCode")
        question_code.send_keys(questionID)
        
        # Select the desired programming language
        language_selector = Select(self.driver.find_element(By.NAME, "programTypeId"))
        language_selector.select_by_value(compiler)
        
        # Upload file instead of pasting code
        upload_element = self.driver.find_element(By.NAME, "sourceFile") 
        # Replace By.NAME with By.ID if needed
        upload_element.send_keys(pathToCode)
        
        # Submit using the question id button
        question_code.send_keys(Keys.RETURN)
        
        # Wait for the URL to change, indicating successful submission
        WebDriverWait(self.driver, 30).until(
            EC.url_contains("/status")
        )
        
        self.driver.close()
        
        print(f"Mock submission for contest and question {questionID} from {pathToCode} completed.")