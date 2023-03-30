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

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")


# 멜론 차트 버튼 클릭
#chartbtn = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
#chartbtn.click()
# 1위곡명 가져오기
#first = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').text
#print(first)
#time.sleep(3)
# 1위부터 20위까지 가져오기
#for i in range(1, 21):
#    titles = driver.find_element(By.XPATH,f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a').text
#    print(titles)
#    time.sleep(3)
# 스크롤 내리기
#driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
#driver.execute
# 실시간 급상승 가수 가져오기

# 곡의 장르 가져오기
#first = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').text
#print(first)
#time.sleep(3)
#time.sleep(1)
#chartbtn1 = driver.find_element(By.XPATH,'//*[@id="lst50"]/td[7]/div/div/div/a')
#chartbtn1.click()
#time.sleep(2)
#second = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').text
#print(second)
#time.sleep(3)

# 좋아하는 가수의 곡명 10개

# 순위, 곡명, 가수명 가져오기
#address = driver.find_element(By.XPATH, '//*[@id="gnb"]/div[2]/div/ol/li[5]/a').text
#time.sleep(1)
#ActionChains(driver).move_to_element(address).perform()
#time.sleep(1)

#for i in range(1,11):
#    ranklist = driver.find


#chartbtn2 = driver.find_element(By.XPATH, '//*[@id="top_search"]')
#chartbtn2.click()
#ActionChains(driver).send_keys_to_element(chartbtn2, '헤이즈').perform()
#chartbtn3 = driver.find_element(By.XPATH, '//*[@id="gnb"]/fieldset/button[2]/span')
#chartbtn3.click()
#for i in range(1, 11):
#    songs = driver.find_element(By.XPATH,f'//*[@id="frm_searchArtist"]/div/table/tbody/tr[{i}]/td[3]/div/div/a[2]').text
#    print(songs)
#    time.sleep(3)




# csv 파일로 변환
#chartbtn4 = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
#chartbtn4.click()
#time.sleep(1)
#for i in range(1, 51):
#    list = driver.find_element(By.XPATH,f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a').text
#  time.sleep(3)

#import csv

#file = open('melon.csv', mode='w', newline='')
#writer = csv.writer(file)
#writer.writerow(['rank','title','singer'])
#    writer.writerow([rank, title, singer])
#file.close()

