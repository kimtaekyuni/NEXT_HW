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

# 네이버 영화 랭크 1~20위 뽑기 
#for i in range(1,11):
#    movie_ranking1 = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i+1}]/td[2]/div/a').text
#    print(movie_ranking1)
#    time.sleep(0.5)
#for i in range(1,11):
#    movie_ranking2 = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i+12}]/td[2]/div/a').text
#    print(movie_ranking2)
#    time.sleep(0.5)

# 각 영화 클릭 -> 개요, 감독, 평점 

#for i in range(1,22):
    #if i == 8:
        #chartbtn = driver.find_element(By.XPATH, '//*[@id="old_content"]/table/tbody/tr[9]/td[2]/div/a')
        #chartbtn.click()
        #movie_outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
        #print(movie_outline)
        #time.sleep(0.5)
        #movie_director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
        #print(movie_director)
        #time.sleep(0.5)
        #movie_star = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[4]/div[2]/div[2]/div[1]/div/div/em').text
        #print(movie_star)
        #chartbtn_return = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
        #chartbtn_return.click()

    #elif i == 11:
        # chartbtn_return.click()

    #else:
    #chartbtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i+1}]/td[2]/div/a')
    #chartbtn.click()
    #movie_outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
    #print(movie_outline)
    #time.sleep(0.5)
    #movie_director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    #print(movie_director)
    #time.sleep(0.5)
    #movie_star = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
    #print(movie_star)
    #chartbtn_return = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
    #chartbtn_return.click()

#for i in range(1,8):
#     chartbtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i+1}]/td[2]/div/a')
#     chartbtn.click()
#     movie_outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
#     print(movie_outline)
#     time.sleep(0.5)
#     movie_director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#     print(movie_director)
#     time.sleep(0.5)
#     movie_star = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
#     print(movie_star)
#     chartbtn_return = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#     chartbtn_return.click()
#
#chartbtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{9}]/td[2]/div/a')
#chartbtn.click()
#movie_outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
#print(movie_outline)
#time.sleep(0.5)
#movie_director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#print(movie_director)
#time.sleep(0.5)
#movie_star = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[4]/div[2]/div[2]/div[1]/div/div/em').text
#print(movie_star)
#chartbtn_return = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#chartbtn_return.click()
# 
#for i in range(9,11):
#    chartbtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i+1}]/td[2]/div/a')
#    chartbtn.click()
#    movie_outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
#    print(movie_outline)
#    time.sleep(0.5)
#    movie_director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#    print(movie_director)
#    time.sleep(0.5)
#    movie_star = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
#    print(movie_star)
#    chartbtn_return = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#    chartbtn_return.click()
#
#for i in range(12,22):
#    chartbtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i+1}]/td[2]/div/a')
#    chartbtn.click()
#    movie_outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
#    print(movie_outline)
#    time.sleep(0.5)
#    movie_director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#    print(movie_director)
#    time.sleep(0.5)
#    movie_star = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
#    print(movie_star)
#    chartbtn_return = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#    chartbtn_return.click()

#본인 좋아하는 영화 검색 
#chartbtn_searchblank = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
#chartbtn_searchblank.click()
#ActionChains(driver).send_keys_to_element(chartbtn_searchblank, '미니언즈').perform()
#chartbtn_search = driver.find_element(By.XPATH, '//*[@id="jSearchArea"]/div/button')
#chartbtn_search.click()
#chartbtn_minions = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li[1]/dl/dt/a/strong')
#chartbtn_minions.click()
#minions_title = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
#print(minions_title)
#time.sleep(0.5)
#minions_director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#print(minions_director)
#time.sleep(0.5)
#
#for i in range(1,3):
#    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
#    driver.execute
#
#
#minions_stars = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
#print(minions_stars)
#time.sleep(0.5)
#minions_review = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text
#print(minions_review)
#time.sleep(0.5)

#csv 파일로 만들기 
import csv

container_movie_outline = []
container_movie_director = []
container_movie_star = []

file = open('navermovie.csv', mode='w', newline='', encoding="utf-8")
writer = csv.writer(file)
writer.writerow(['outline','director','star'])

for i in range(1,8):
    chartbtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i+1}]/td[2]/div/a')
    chartbtn.click()
    movie_outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
    #container_movie_outline.append(movie_outline)
    #print(movie_outline)
    time.sleep(0.5)
    movie_director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    #container_movie_director.append(movie_director)
    #print(movie_director)
    time.sleep(0.5)
    movie_star = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
    #container_movie_star.append(movie_star)
    #print(movie_star)
    chartbtn_return = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
    chartbtn_return.click()    
    writer.writerow([movie_outline,movie_director,movie_star])
   
   
file.close()














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

