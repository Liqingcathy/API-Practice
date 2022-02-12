from selenium import webdriver

chrome_driver_path = "/Users/liqingli/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")

event = {}
for n in range(len(event_times)):
    event[n] = {
        "time": event_times[n].text,
        "name": event_name[n].text
    }
    
print(event)
driver.quit()

