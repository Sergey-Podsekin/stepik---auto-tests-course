from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return abs(math.log(12 * math.sin(x)))


try:
    # Открыть страницу http://SunInJuly.github.io/execute_script.html.
    browser.get(link)

    # Считать значение для переменной x.
    num = int(browser.find_element_by_id("input_value").text)

    # Посчитать математическую функцию от x.
    x1 = calc(num)

    # Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0, 120);")

    # Ввести ответ в текстовое поле.
    browser.find_element_by_id("answer").send_keys(str(x1))

    # Выбрать checkbox "I'm the robot".
    browser.find_element_by_id("robotCheckbox").click()

    # Переключить radiobutton "Robots rule!".
    browser.find_element_by_id("robotsRule").click()

    # Нажать на кнопку "Submit".
    browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(10)
    browser.quit()
