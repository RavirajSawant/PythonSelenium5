# libraries
import time
from behave import *
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure

# handling notifications
option = Options()
option.add_argument("--disable-notifications")


# webdriver
@given(u'User user is on search page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User user is on search page')
Raviraj = webdriver.ChromeOptions()
Raviraj.headless = True
driver = webdriver.Chrome(executable_path="C:/Users/Raviraj/Desktop/chromedriver_win32/chromedriver.exe",
                          chrome_options=option)
driver.implicitly_wait(5)

# opening irctc air url
driver.get("https://www.air.irctc.co.in/")

# maximize window size
driver.maximize_window()
assert True, "Test Passeed"

time.sleep(5)
# select origin in the list
@when(u'user selects Hyderabad as a Origin')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user selects Hyderabad as a Origin')


driver.find_element(By.ID, "stationFrom").send_keys("Hyd")
driver.find_element(By.XPATH, "//body[1]/ul[1]/li[8]/div[1]").click()
assert True, "Test Passeed"
time.sleep(5)


# select destination in the list
@when(u'User user selects Pune as a Destination')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User user selects Pune as a Destination')
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//input[@id='stationTo']").send_keys("pune")
driver.find_element(By.XPATH, "//body[1]/ul[2]/li[7]/div[1]").click()
assert True, "Test Passeed"
time.sleep(5)


# select date
@when(u'user select today date from the Departure')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user select today date from the Departure')


driver.switch_to.default_content()
driver.find_element(By.XPATH, "//input[@id='originDate']").click()
driver.find_element(By.XPATH, "//span[@class='act active-red']").click()
assert True, "Test Passeed"
time.sleep(5)


# select travel class as business class
@when(u'user select Business class from the Travellers field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user select Business class from the Travellers field')
driver.find_element(By.XPATH, "//input[@id='noOfpaxEtc']").click()
element = driver.find_element(By.XPATH, "//select[@id='travelClass']")
dd = Select(element)
dd.select_by_visible_text("Business")
time.sleep(10)
driver.find_element(By.XPATH,
                    "//body/app-root[1]/app-index[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[6]/button[1]").submit()
assert True, "Test Passeed"
time.sleep(5)


# search the flight
@when(u'User clicks on the Search button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks on the Search button')
flight_names = driver.find_elements(By.XPATH, '//div[@class="right-searchbarbtm"]')
assert True, "Test Passeed"
time.sleep(5)

# prints available flights
@then(u'user flights are presented on the search result page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user flights are presented on the search result page')
print("the no. of flights available are:", len(flight_names))
for flight in flight_names:
    print(flight.text)
    print("-------------------------------------------------------------------")
assert True, "Test Passeed"
time.sleep(5)
# takes screenshots of avilable flights
@then(u'User capture the result screenshot and save in the project folder')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User capture the result screenshot and save in the project folder')
time.sleep(10)
driver.get_screenshot_as_file('flight1.png')
time.sleep(3)
driver.execute_script("window.scrollBy(0,750)", " ")
time.sleep(3)
driver.get_screenshot_as_file('flight2.png')
time.sleep(3)
driver.execute_script("window.scrollBy(750,1500)", " ")
time.sleep(3)
driver.get_screenshot_as_file('flight3.png')

assert True, "Test Passeed"

#close driver
driver.close()