import time
import pickle

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Parser:

    def __init__(self):
        pass
    
    def parse(self):
        option = webdriver.FirefoxOptions()
        option.set_preference('dom.webdriver.enable', False)
        option.set_preference('dom.webnotifications.enable', False)
        option.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Firefox/89.0')
        driver = webdriver.Firefox(options=option)
        driver.get('https://srv-gg.ru/auth/realms/fseq/protocol/openid-connect/auth?client_id=account&redirect_uri=https%3A%2F%2Fsrv-gg.ru%2F&state=918e0255-4a96-4530-8723-8f3bd9b48776&response_mode=fragment&response_type=code&scope=openid&nonce=a3161c0b-71fa-487d-8d87-6df7316f4b97&code_challenge=hHngFKGvWEQ8CzumtyTTln9LTiElkkpnAvHENvPb8bE&code_challenge_method=S256')
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'username')
            ))
        username_field.send_keys('eurolite8999@mail.ru')
        password_field = driver.find_element(By.ID , 'password')
        password_field.send_keys('Eurolite8999@mail.ru')
        driver.find_element(By.ID , 'kc-login').click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'link-primary')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'seq-select__value-container')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'react-select-6-listbox')
        )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'd-inline-block')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'form-check-input')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'd-inline-block')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'seq-select-container')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'seq-select__menu')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'btn-seq-primary')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'informed')
            )).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'btn-seq-primary')
            )).click()
        btn_bron = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'btn-seq-primary')
            )).is_enabled()
        if btn_bron == False:
            return print("На ближайщие даты записей нет")
        else:
            return print(f"Запись есть")
if __name__ == "__main__":
    parser = Parser()
    parser.parse()