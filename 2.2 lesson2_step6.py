from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
 
    time.sleep(30)
    browser.quit()