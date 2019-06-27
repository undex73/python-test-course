import math
from selenium import webdriver

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text

field = browser.find_element_by_id("answer")
field.send_keys(calc(x))
checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()
radio = browser.find_element_by_css_selector(".form-check-input#robotsRule")
radio.click()

button = browser.find_element_by_css_selector(".btn")
button.click()
