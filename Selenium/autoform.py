from selenium import webdriver
#submit subscription from automatically

chrome_driver_path = "/Users/liqingli/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element_by_name("fName")
fName.send_keys("li")
lName = driver.find_element_by_name("lName")
lName.send_keys("li")
email = driver.find_element_by_name("email")
email.send_keys("test@test.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()