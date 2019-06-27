import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(int(x)+int(y))

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(calc(x))

button = browser.find_element_by_css_selector(".btn")
button.click()
