from selenium.webdriver.common.by import By
from configuration import *
from time import sleep


def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)
    
    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    
    chrome_browser.find_element(By.ID, "login-button").click()
    
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    
    chrome_browser.find_element(By.ID, "shopping_cart_container").click()
    
    chrome_browser.find_element(By.ID, "checkout").click()
    
    chrome_browser.find_element(By.ID, "first-name").send_keys("Evgen")
    
    chrome_browser.find_element(By.ID, "last-name").send_keys("Voronov")
    
    chrome_browser.find_element(By.ID, "postal-code").send_keys("601500")

    chrome_browser.find_element(By.ID, "continue").click()

    total_price = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")
    sleep(2)
    expected_total = "58.29"
    assert total == expected_total 
    print("Итоговая сумма равна $58.29")
