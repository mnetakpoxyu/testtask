from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

def change_google_password(email, old_password, new_password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://accounts.google.com/signin/v2/identifier')

    driver.find_element(By.ID, 'identifierId').send_keys(email)
    driver.find_element(By.ID, 'identifierNext').click()
    time.sleep(2)

    driver.find_element(By.NAME, 'password').send_keys(old_password)
    driver.find_element(By.ID, 'passwordNext').click()
    time.sleep(5)

    driver.get('https://myaccount.google.com/security')
    time.sleep(5)

    driver.find_element(By.XPATH, '//a[contains(text(),"Password")]').click()
    time.sleep(2)
    
    driver.find_element(By.NAME, 'password').send_keys(new_password)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    
    time.sleep(5)
    driver.quit()

def update_google_profile(email, password, new_first_name, new_last_name):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://accounts.google.com/signin/v2/identifier')

    driver.find_element(By.ID, 'identifierId').send_keys(email)
    driver.find_element(By.ID, 'identifierNext').click()
    time.sleep(2)

    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.ID, 'passwordNext').click()
    time.sleep(5)

    driver.get('https://myaccount.google.com/personal-info')
    time.sleep(5)

    driver.find_element(By.XPATH, '//span[text()="Name"]').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'firstName').clear()
    driver.find_element(By.NAME, 'firstName').send_keys(new_first_name)
    driver.find_element(By.NAME, 'lastName').clear()
    driver.find_element(By.NAME, 'lastName').send_keys(new_last_name)
    driver.find_element(By.XPATH, '//button[text()="Save"]').click()

    time.sleep(5)
    driver.quit()

def save_data(email, password, first_name, last_name, birth_date, backup_email):
    with open('user_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, password, first_name, last_name, birth_date, backup_email])

def main():
    email = 'your-email@gmail.com'
    old_password = 'oldpassword'
    new_password = 'newpassword'
    new_first_name = 'NewFirstName'
    new_last_name = 'NewLastName'
    birth_date = '01/01/1990'
    backup_email = 'backup-email@gmail.com'

    change_google_password(email, old_password, new_password)
    update_google_profile(email, new_password, new_first_name, new_last_name)
    save_data(email, new_password, new_first_name, new_last_name, birth_date, backup_email)

if __name__ == "__main__":
    main()
