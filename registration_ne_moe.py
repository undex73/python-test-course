from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
input1.send_keys("Ivan")
input2 = browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
input2.send_keys("Petrov")
input3 = browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
input3.send_keys("fake@fake.fake")

button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()
