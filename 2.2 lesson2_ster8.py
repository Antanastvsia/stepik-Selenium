from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")
    
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")
    
    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_path = os.path.join(current_dir, "test_file.txt")

    with open(file_path, "w") as f:
        pass  
    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(file_path)
 
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    browser.quit()