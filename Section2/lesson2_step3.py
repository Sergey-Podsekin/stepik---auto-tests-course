from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"


try:
    browser.get(link)
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    x = num1 + num2
    print(x)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x))
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()
