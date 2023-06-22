import os
from selenium import webdriver #Import to create a instance of an especific navigator 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

os.environ['PATH'] +=r"C:\SeleniumDrivers"
driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches' , ['enable-loggin'])

driver = webdriver.Chrome(options=options)


driver.get("http://smartcell-ecommerce-website.s3-website-us-east-1.amazonaws.com/")
driver.implicitly_wait(30)

## To find elements that are equal
#storeElements = driver.find_elements(By.CSS_SELECTOR, "li.text-\\[16px\\].mx-3.hover\\:cursor-pointer.hover\\:text-slate-400")


#for storeElement in storeElements:
 # if storeElement.text == 'Tienda': 
  #  storeElement.click()
   # break


usericon = driver.find_element(By.CSS_SELECTOR , "img[alt='usuario']")
usericon.click()


loginElement = driver.find_element(By.CSS_SELECTOR , 'span.text-\\[12px\\].sm\\:text-\\[15px\\].hover\\:cursor-pointer.hover\\:text-slate-400')
loginElement.click()

registerElement = driver.find_element(By.CSS_SELECTOR, "span.flex.justify-center.mb-\\[2rem\\].hover\\:cursor-pointer")
registerElement.click()

username = driver.find_element(By.NAME , "username")
email = driver.find_element(By.NAME , "email" )
password = driver.find_element(By.NAME, "password")
name = driver.find_element(By.NAME, "name")
lastName = driver.find_element(By.NAME, "lastname")


username.send_keys("wolumo")
email.send_keys("wistonjosequintanaosorio@hotmail.com")
password.send_keys("wolumito")
name.send_keys("Wiston Jose")
lastName.send_keys("Quintana Osorio")

nextElements = driver.find_elements(By.CSS_SELECTOR , "button.font-semibold.rounded-full.bg-blue-500.px-\\[2rem\\].py-2")
for NextElement in nextElements:
    if NextElement.text == "Siguiente":
        NextElement.click()

#######################################################################################################################################