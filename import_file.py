import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

field_first_name = browser.find_element_by_name("firstname")
field_first_name.send_keys("Юра")
field_last_name = browser.find_element_by_name("lastname")
field_last_name.send_keys("Иванов")
field_email = browser.find_element_by_name("email")
field_email.send_keys("aa@aa.ru")

current_dir = os.path.abspath(os.path.dirname("/Users/alex/enviroments/selenium_env/selenium_course/"))
file_path = os.path.join(current_dir, 'todo.txt')
element = browser.find_element_by_id("file")
element.send_keys(file_path)

button = browser.find_element_by_css_selector(".btn")
button.click()
