from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept() 

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()