from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text

    result = str(int(num1) + int(num2))

    dropdown = Select(browser.find_element(By.TAG_NAME, "select"))

    dropdown.select_by_value(result)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(30)
    browser.quit()