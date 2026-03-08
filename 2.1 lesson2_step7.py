from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    treasure_chest = browser.find_element(By.CSS_SELECTOR, "#treasure")

    x = treasure_chest.get_attribute("valuex")

    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(30)
    browser.quit()