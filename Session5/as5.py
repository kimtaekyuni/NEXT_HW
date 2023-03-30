from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "C:/Users/tgkim/OneDrive/바탕 화면/NEXT 자료/NEXT_HW/Session5/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (네이버 영화 랭킹) 
driver.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")

import pandas as pd
from bs4 import BeautifulSoup
import requests as req

input_box = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
input_box.send_keys('미니언즈')
input_box.send_keys(Keys.ENTER)
time.sleep(1)

chartbtn = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li[1]/dl/dt/a')
chartbtn.click()

url = driver.current_url

res =req.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.select('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')
title_cleaned = [e.text.strip() for e in title]
director = soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a')
director_cleaned = [a.text.strip() for a in title]

print(title_cleaned)
print(director_cleaned)




