from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
from tqdm import tqdm


options = webdriver.ChromeOptions()
title = 'All I Want for Christmas Is You'
artist = 'Mariah Carey'
full = artist + ' - ' + title
daily = []
dateT = []
dailyUS = []
dailyUK = []
us = 'us/ny/new-york-city/KLGA'
uk = 'gb/london/EGLC'


# 리스트 가져오기
list_url = 'https://kworb.net/ww/archive/'
html = urlopen(list_url).read()
soup = BeautifulSoup(html, "lxml")
addresses = soup.find_all('a')

dates = []

for address in addresses:
    if len(address.text) >= 8:
        each = address.text[:8]
        dates.append(each)
    else:
        continue
 


# 매일 순위 추가하기
def addRank(date):
    daily_url = f'{list_url}{date}.html'
    temp = []
    temp.append(str(date))
    
    # url open
    with urlopen(daily_url) as u:
            daily_soup = BeautifulSoup(u, "lxml")
            daily_table = daily_soup.find('table', {'class' : 'sortable'})
            
            try:
                daily_tr = daily_table.select('tr')
                artist_title = []
                rank = []
                rank2 = []
                
                # 아티스트 목록, US 순위, UK 순위
                for idx, tr in enumerate(daily_tr):                   
                    if idx >0:
                        artist_title.append(tr.select_one('td:nth-of-type(3)').text)
                        if len(tr.select_one('td:nth-of-type(9)').text) > 3:
                            rank.append(tr.select_one('td[style="border-left:1px solid black;"]').text)
                            rank2.append((tr.select_one('td[style="border-left:1px solid black;"]')).next_sibling.text)
                        else:
                            rank.append(tr.select_one('td:nth-of-type(9)').text)
                            rank2.append(tr.select_one('td:nth-of-type(9)').next_sibling.text)


                #데이터 추가
                if full in artist_title:
                    temp.append(str(artist_title.index(full) + 1))
                    temp.append(str(rank[artist_title.index(full)]))
                    temp.append(str(rank2[artist_title.index(full)]))

                else:
                    temp.extend(['400', '400', '400'])
                            
            except:
                temp.extend(['err', 'err', 'err'])
    
    daily.append(temp)
    
for date in tqdm(dates):
    addRank(date)

print(daily)


# 기온 날짜 리스트
for year in range(2011, 2022):
    if year == 2011:
        for month in range(2, 13):
            date = str(year) + '-' + str(month)
            dateT.append(date)
            
    elif year == 2021:
        dateT.append('2021' + '-' + '1')
        
    else:
        for month in range(1, 13):
            date = str(year) + '-' + str(month)
            dateT.append(date)


# 날씨 페이지 접속
def render_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('C:\projects\chromedriver', chrome_options=options)
    driver.get(url)
    time.sleep(5)
    r = driver.page_source
    driver.quit()
    return r


# 화씨-섭씨 변환 함수
def trans(f):
    c = (float(f) - 32) * 5 / 9
    return str(round(c, 2))


# 날씨 데이터 저장
def addClimate(country):
    
    for d in dateT:

        url = f'https://www.wunderground.com/history/monthly/{country}/date/{d}'

        # 5초 기다리는 함수 및 불러내기   
        r = render_page(url)

        soup = BeautifulSoup(r, "lxml")
        container = soup.select_one('lib-city-history-observation')
        check = container.select_one('tbody')
        table = check.select('table')[1]
        td = table.select('td:nth-of-type(2)')
        
        temp = []

        # 데이터 저장
        try:
            for i, data in enumerate(td):

                if d == '2011' + '-' + '2':
                    if i > 18:
                        temp.append(trans(data.text))

                elif i > 0:
                    temp.append(trans(data.text))


        except:
            temp.append('err')

        # 미국 날씨
        if country == us:
            dailyUS.append(temp)

        # 영국 날씨    
        else:
            dailyUK.append(temp)
            
        print(country + d + 'is done!')

for country in [us, uk]:
    addClimate(country)

# 확인
print(dailyUS)
print(dailyUK)


# 기온 정렬 함수
def open(T):
    temp = []
    for i in T:
        for j in i:
            temp.append(str(i))
            
    T, temp = temp, T
    
    return T


# 정보 합치기
for n in range(len(daily)):
    daily[n].insert(3, open(dailyUS)[n])
    daily[n].append(open(dailyUK)[n])


# CSV 파일 생성
with open('mariah_xmas.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['date','WDRank','USRank', 'USTemp', 'UKRank', 'UKTemp'])

    writer.writerows(daily)
