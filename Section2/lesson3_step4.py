from selenium import webdriver
import time
import math


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return abs(math.log(12 * math.sin(x)))


try:
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser.get(link)

    # Нажать на кнопку
    first_button = browser.find_element_by_css_selector('button')
    first_button.click()

    # Принять confirm
    alert = browser.switch_to.alert
    alert.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = int(browser.find_element_by_id('input_value').text)
    answer = str(calc(x))
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer)

    submit_button = browser.find_element_by_css_selector('button')
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()
