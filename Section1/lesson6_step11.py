from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем поля с аттрибутом required
    required_fields = browser.find_elements_by_xpath("//*[@required]")

    # Проверяем, что количество обязательных полей равно 3
    assert len(required_fields) == 3, "Неверное количество обязательных полей"

    # Вводим данные в каждое обязательное поле
    for element in required_fields:
        element.send_keys('data')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
