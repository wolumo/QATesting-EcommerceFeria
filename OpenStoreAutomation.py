import os
from selenium import webdriver #Import to create a instance of an especific navigator 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r"C:\SeleniumDrivers" #Configurin on the path of the system.
driver = webdriver.Chrome() #Creating an Intance of Chrome.

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("http://smartcell-ecommerce-website.s3-website-us-east-1.amazonaws.com/")
driver.implicitly_wait(30)


myElement=  driver.find_element(By.XPATH, "//button[contains(@class, 'rounded-xl')]")


myElement.click()

#####################################################


