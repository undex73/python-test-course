import math
from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector(".btn")
button.click()
confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text

field = browser.find_element_by_id("answer")
field.send_keys(calc(x))

button = browser.find_element_by_css_selector(".btn")
button.click()
