import math
from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")

field = browser.find_element_by_id("answer")
field.send_keys(calc(x))
checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
checkbox.click()
radio = browser.find_element_by_css_selector(".check-input#robotsRule")
radio.click()
