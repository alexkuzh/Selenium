from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

print(driver.find_element(By.LINK_TEXT, "California Real Estate").get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))
assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
print(driver.title)

if driver.find_element_by_xpath("//h2[contains(text(),'Send Us a Message')]").text == 'Send Us a Message':
    driver.find_element_by_xpath("//input[@id='g2-name']").send_keys('t1')
    driver.find_element_by_name("g2-email").send_keys('blablabla@gmail.com')
    driver.find_element_by_id("contact-form-comment-g2-message").send_keys('test!')
    driver.implicitly_wait(5)
    # print(driver.find_element_by_xpath("//button[@class='pushbutton-wide']").text)
    driver.find_element_by_class_name("pushbutton-wide").click()  # not click ?????
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//a[contains(text(),'go back')]").click()
    # driver.find_element_by_xpath("//img[@class='custom-logo']").click()

print("Button's type is", driver.find_element_by_xpath("//button[@class='pushbutton-wide']").get_attribute("type"))

driver.close()