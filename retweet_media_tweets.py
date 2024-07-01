from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Path to Chrome Driver
chrome_driver_path = 'path_to_your_chromedriver'

# Login to New Twitter Account
twitter_username = 'your_username'
twitter_password = 'your_password'
mfa_code = input('Enter MFA code: ')

# Read Media Tweets
media_tweets_df = pd.read_csv('media_tweets.csv')

# WebDriver Settings
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://twitter.com/login')

# Twitter Login
time.sleep(3)
username_field = driver.find_element(By.NAME, 'session[username_or_email]')
password_field = driver.find_element(By.NAME, 'session[password]')
username_field.send_keys(twitter_username)
password_field.send_keys(twitter_password)
password_field.send_keys(Keys.RETURN)

# Imput MFA code
mfa_field = driver.find_element(By.NAME, 'challenge_response')
mfa_field.send_keys(mfa_code)
mfa_field.send_keys(Keys.RETURN)

# Post Media Tweets
for index, tweet in media_tweets_df.iterrows():
    tweet_box = driver.find_element(By.CSS_SELECTOR, 'div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
    tweet_box.send_keys(f"{tweet['datetime']} {tweet['text']}")

    for media_url in tweet['media']:
        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(media_url)

    driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']").click()
    time.sleep(5)

driver.quit()

#This software is released under the MIT License, see LICENSE.
