from selenium import webdriver
import os
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))


try:
    browser.get(link)
    browser.find_element_by_css_selector('[name="firstname"]').send_keys('Sergey')
    browser.find_element_by_css_selector('[name="lastname"]').send_keys('Podsekin')
    browser.find_element_by_css_selector('[name="email"]').send_keys('sergey@py.com')
    submit = browser.find_element_by_id('file')
    file_path = os.path.join(current_dir, 'file.txt')
    submit.send_keys(file_path)
    browser.find_element_by_css_selector('button').click()

finally:
    time.sleep(10)
    browser.quit()
