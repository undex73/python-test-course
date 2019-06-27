from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
first_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
first_name.send_keys("Василий")
second_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
second_name.send_keys("Пупкин")
email = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
email.send_keys("vasia@pupkin.vp")
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn").click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
