from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.implicitly_wait(2)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


def calc(x):
    a = (12 * math.sin(x))
    a = math.log(a)
    return str(a)


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

browser.find_element_by_id('book').click()
num = int(browser.find_element_by_id("input_value").text)
browser.find_element_by_id("answer").send_keys(calc(num))
browser.find_element_by_id("solve").click()
