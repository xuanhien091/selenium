# -*- coding: utf-8 -*-

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time ,random 


# 変数設定

username = "" # twitter ID 

password = "" # twitter password 

tag = "筋トレ" #ハッシュタグ

num =   200 # いいね数


# docker内で起動するためのoptionを作成
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# option込でChromeを起動
driver = webdriver.Chrome(options=options)

login_url = "https://twitter.com/login"

# instagaramのサイトを開く

driver.get(login_url)

driver.implicitly_wait(15)

print(driver.current_url) #現在のURLを確認

print(driver.title + "にアクセス" ) #現在のページのタイトルを表示

driver.implicitly_wait(10)


time.sleep(5)


username = driver.find_element_by_xpath("//input[contains(@name, 'username_or_email')]")
password = driver.find_element_by_xpath("//input[contains(@name, 'password')]")


username.send_keys(username)
time.sleep(1)

password.send_keys(password)
password.send_keys(Keys.RETURN)

time.sleep(5)
driver.implicitly_wait(10)



driver.close()
