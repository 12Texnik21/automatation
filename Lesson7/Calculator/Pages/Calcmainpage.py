from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Lesson7.constant import Calculator_URL
from selenium import webdriver 

class CalcMain:
    

    def __init__(self, browser : webdriver.Chrome):
        self.browser = browser
        self.browser.get(Calculator_URL)
    
    def insert_time(self):
        
        delay_input = self.browser.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(45)

    def clicking_buttons(self):
        
        self.browser.find_element(By.XPATH, "//span[text() = '7']").click()

        self.browser.find_element(By.XPATH, "//span[text() = '+']").click()

        self.browser.find_element(By.XPATH, "//span[text() = '8']").click()

        self.browser.find_element(By.XPATH, "//span[text() = '=']").click()

    def wait_buttons_gettext(self):
        
        WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"),"15" ))
        return self.browser.find_element(By.CLASS_NAME, "screen").text