from selenium import webdriver as wd        
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import datetime as dt
import urllib.parse             
import time


def extract_text(tweets):
    tagout = re.compile('<.*?>')
    unicodeout = re.compile(r'"[\\u]%d{4,5}"')
    tw = []
    for t in tweets:
        t = re.sub(tagout, "", str(t))
        t = re.sub(unicodeout, "", t)
        t = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", t)
        tw.append(t)
    return tw



def get_freq_only(keyword, startdate, middate, enddate):
    total_freq = []
    keyword_parse = urllib.parse.quote_plus(keyword)
    
    while startdate != enddate:        
        url = "https://twitter.com/search?q=" + keyword_parse + "%20since%3A" + str(startdate) + "%20until%3A" + str(middate) + "&src=typed_query&f=top"
        driver.get(url)
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        wordfreq = 0
        dailyfreq = {'Date' : startdate}
        tweets = soup.find_all("div", {'class' : "css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"})
        wordfreq += len(tweets)
        
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height != last_height:
                html = driver.page_source
                soup = BeautifulSoup(html,'html.parser')
                tweets = soup.find_all("div", {'class' : "css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"})
                wordfreq += len(tweets)

            else:                                   # 일별로 검색 후 끝까지 scroll 다 내림
                dailyfreq['Frequency'] = wordfreq
                total_freq.append(dailyfreq)        # 일별 단어 빈도수 기록
                
                startdate = middate
                middate += dt.timedelta(days=1)
                break

            last_height = new_height
    
    return total_freq



def search_twitter(keyword, startdate, middate, enddate):
    tweets_bag = []
    keyword_parse = urllib.parse.quote_plus(keyword)

    while startdate != enddate:         # interval : 1 day
        url = "https://twitter.com/search?q=" + keyword_parse + "%20since%3A" + str(startdate) + "%20until%3A" + str(middate) + "&src=typed_query&f=top"
        driver.get(url)
        time.sleep(5)
        
        latest = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-14lw9ot.r-gtdqiz.r-1gn8etr.r-1g40b8q > div:nth-child(2) > nav > div > div.css-1dbjc4n.r-1adg3ll.r-16y2uox.r-1wbh5a2.r-1pi2tsx.r-1udh08x > div > div:nth-child(2) > a")
        latest.click()
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        tw = []
        weeklyfreq = 0
        tweets = soup.find_all("div", {'class' : "css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"})
        tw += extract_text(tweets)
        weeklyfreq += len(tweets)

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height != last_height:
                html = driver.page_source
                soup = BeautifulSoup(html,'html.parser')
                
                tweets = soup.find_all("div", {'class' : "css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"})
                tw += extract_text(tweets)
                weeklyfreq += len(tweets)
            else:                                   # 일별로 검색 후 끝까지 scroll 다 내림
                tweets_bag.append([startdate, weeklyfreq, tw])
                startdate = middate
                middate += dt.timedelta(days=7)
                break

            last_height = new_height
    
    return tweets_bag



def createDF(total_freq, tweets_bag, keyword, tag):
    import pandas as pd
    if total_freq:
        df1 = pd.DataFrame(total_freq)
        df1.to_excel("Total_Freq_" + keyword + "_" + str(tag) + ".xlsx")

    if tweets_bag:
        df2 = pd.DataFrame(tweets_bag, columns=['Date', 'Weekly Frequency', 'Tweets'])
        df2.to_excel("Tweets_" + keyword + "_" + str(tag) + ".xlsx")



if __name__ == "__main__":

    keywords = ['코로나, 감정', '코로나, 기분', '코로나, 일상']
    years = [2020, 2021]
    driver = wd.Chrome("chromedriver.exe")
    yearly_freq = []
    tweets_bag = []

    for keyword in keywords:
        for year in years:
            if year == 2020: limit = 13
            elif year == 2021: limit = 11
            for i in range(1, limit):      # 1~12 month per year
                startdate = dt.date(year=year,month=i,day=1)
                middate = dt.date(year=year,month=i,day=7)
                enddate = dt.date(year=year,month=i,day=28)
                tweets_bag += search_twitter(keyword, startdate, middate, enddate)

                if i == 6 or i == limit-1:
                    if i == 6: add = "_상반기"
                    elif i == limit-1: add = "_하반기"
                    tag = str(year) + "년" + add
                    createDF(yearly_freq, tweets_bag, keyword, tag)
                    tweets_bag = []

        # yearly_freq = get_freq_only(keyword, startdate, middate, enddate)
        