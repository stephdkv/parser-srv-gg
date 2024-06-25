import time
from datetime import datetime
import os

import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("parser.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class Parser:

    def __init__(self):
        pass
    
    def parse(self):
        option = webdriver.FirefoxOptions()
        option.set_preference('dom.webdriver.enable', False)
        option.set_preference('dom.webnotifications.enable', False)
        option.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Firefox/89.0')
        option.add_argument('--headless')
        driver = webdriver.Firefox(options=option)
        driver.minimize_window()
        driver.get('https://srv-gg.ru/auth/realms/fseq/protocol/openid-connect/auth?client_id=account&redirect_uri=https%3A%2F%2Fsrv-gg.ru%2F&state=918e0255-4a96-4530-8723-8f3bd9b48776&response_mode=fragment&response_type=code&scope=openid&nonce=a3161c0b-71fa-487d-8d87-6df7316f4b97&code_challenge=hHngFKGvWEQ8CzumtyTTln9LTiElkkpnAvHENvPb8bE&code_challenge_method=S256')
        
        try:
            username_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'username'))
            )
            username_field.send_keys('eurolite8999@mail.ru')
            
            password_field = driver.find_element(By.ID, 'password')
            password_field.send_keys('Eurolite8999@mail.ru')
            driver.find_element(By.ID, 'kc-login').click()
            
            
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'link-primary'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'seq-select__value-container'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'react-select-6-listbox'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'd-inline-block'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'form-check-input'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'd-inline-block'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'seq-select-container'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'seq-select__menu'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'btn-seq-primary'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'informed'))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'btn-seq-primary'))
            ).click()
            btn_bron = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'btn-seq-primary'))
            ).is_enabled()
            btn_bron_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'btn-seq-primary'))
            )
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            screenshot_path = os.path.join('../images',f"screenshot_{current_time}.png")
            driver.execute_script("arguments[0].scrollIntoView();", btn_bron_element)  
            driver.save_screenshot(screenshot_path)

            calendar = driver.find_elements(By, 'react-datepicker__month')
            for week in calendar:
                days = week.find_elements(By, 'react-datepicker__week')
                for day in days:
                    day_item = day.find_element(By.XPATH, '//*[@tabindex="0"]').text
                    day.find_element(By.XPATH, '//*[@tabindex="0"]').click()
                    print(day_item)
             
            return btn_bron         
                    
                   
        finally:
            driver.close()

        #return btn_bron

if __name__ == "__main__":
    parser = Parser()
    parser.parse()
    
    while True:
        try:
            available = parser.parse()
            if available:
                logging.info("Запись есть")
                time.sleep(300)
            else:
                logging.info("На ближайщие даты записей нет")
                time.sleep(300)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            time.sleep(60)
