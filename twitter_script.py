from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import csv

def change_twitter_password(email, old_password, new_password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://twitter.com/login')

    driver.find_element(By.NAME, 'session[username_or_email]').send_keys(email)
    driver.find_element(By.NAME, 'session[password]').send_keys(old_password)
    driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]').click()
    time.sleep(5)

    driver.get('https://twitter.com/settings/security_and_access')
    time.sleep(5)
    
    driver.find_element(By.XPATH, '//a[text()="Password"]').click()
    time.sleep(2)

    driver.find_element(By.NAME, 'current_password').send_keys(old_password)
    driver.find_element(By.NAME, 'new_password').send_keys(new_password)
    driver.find_element(By.NAME, 'confirm_new_password').send_keys(new_password)
    driver.find_element(By.XPATH, '//div[@data-testid="SettingsSaveButton"]').click()
    
    time.sleep(5)
    driver.quit()

def post_random_tweet(email, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://twitter.com/login')

    driver.find_element(By.NAME, 'session[username_or_email]').send_keys(email)
    driver.find_element(By.NAME, 'session[password]').send_keys(password)
    driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]').click()
    time.sleep(5)

    tweet = "This is a random tweet #" + str(random.randint(1, 1000))
    driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]').send_keys(tweet)
    driver.find_element(By.XPATH, '//div[@data-testid="tweetButton"]').click()
    
    time.sleep(5)
    driver.quit()

def save_data(email, password, tweet_content):
    with open('twitter_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, password, tweet_content])

def main():
    email = 'your-email@gmail.com'
    old_password = 'oldpassword'
    new_password = 'newpassword'
    
    change_twitter_password(email, old_password, new_password)

    tweet_content = "This is a random tweet #" + str(random.randint(1, 1000))
    post_random_tweet(email, new_password)

    save_data(email, new_password, tweet_content)

if __name__ == "__main__":
    main()
