import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fist_name = browser.find_element_by_css_selector(".first_block > .form-group.first_class > input.first")
        fist_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector(".first_block > .form-group.second_class > input.second")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_css_selector(".first_block > .form-group.third_class > input.third")
        email.send_keys("aleshinalecsey@gmail.com")

        button = browser.find_element_by_xpath("//button[text()='Отправить']")
        button.click()

        time.sleep(5)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", "Поздравляем! Вы успешно зарегистировались!", "Error:Test fail")
    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fist_name = browser.find_element_by_css_selector(".first_block > .form-group.first_class > input.first")
        fist_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector(".first_block > .form-group.second_class > input.second")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_css_selector(".first_block > .form-group.third_class > input.third")
        email.send_keys("aleshinalecsey@gmail.com")

        button = browser.find_element_by_xpath("//button[text()='Отправить']")
        button.click()

        time.sleep(5)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", "Поздравляем! Вы успешно зарегистировались!", "Error:Test fail")

if __name__ == "__main__":
    unittest.main()
