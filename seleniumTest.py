from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("localhost:8000")

heightBox = driver.find_element_by_name('height')
weightBox = driver.find_element_by_name('weight')
submitButton = driver.find_element_by_xpath('//button[@id="submit_button"]')

time.sleep(1)

heightBox.send_keys("""6'2\"""")
weightBox.send_keys("""178""")
submitButton.click()

time.sleep(2)
response = json.loads(driver.execute_script('return JSON.stringify(window.my_response);'))
assert(response['bmi'] == 27.88)
assert(response['classification'] == "Normal Weight")

time.sleep(1)
heightBox.send_keys("""11'0\"""")
weightBox.send_keys("""5000""")
submitButton.click()
response = json.loads(driver.execute_script('return JSON.stringify(window.my_response);'))
assert(response['returnError'] == "Looks like your inputs were invalid!")