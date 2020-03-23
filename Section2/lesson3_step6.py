from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    print(x)
    return abs(math.log(12 * math.sin(x)))


try:
    browser.get(link)
    browser.find_element_by_css_selector('[type="submit"]').click()
    new_tab = browser.window_handles[1]
    old_tab = browser.window_handles[0]
    browser.switch_to.window(new_tab)

    x = int(browser.find_element_by_id("input_value").text)
    print(x)
    answer = str(calc(x))
    print(answer)
    browser.find_element_by_id("answer").send_keys(answer)

    submit_button = browser.find_element_by_css_selector('button')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
