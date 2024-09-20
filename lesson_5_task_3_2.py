from selenium import webdriver
from time import sleep

Chrome = webdriver.Chrome()

try:
    count = 0 

    Chrome.get("http://uitestingplayground.com/dynamicid")

    sleep(2)
    
    blue_button = Chrome.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    for _ in range(3):
        blue_button = Chrome.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)
except Exception as ex:
    print(ex)
finally:
    Chrome.quit()             