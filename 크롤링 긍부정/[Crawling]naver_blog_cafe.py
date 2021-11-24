from selenium import webdriver as wd        
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import datetime as dt
import urllib.parse             
import time


def extract_text(posts):
    tagout = re.compile('<.*?>')
    unicodeout = re.compile(r'"[\\u]%d{4,5}"')
    ps = []
    for p in posts:
        p = re.sub(tagout, "", str(p))
        p = re.sub(unicodeout, "", p)
        p = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", p)
        ps.append(p)
    return ps


def get_posts(url, startdate):
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    weekly_post = []
    weeklyfreq = 0
    posts = []

    tmp = soup.find_all("a", {'class' : "api_txt_lines total_tit _cross_trigger"})
    posts += extract_text(tmp)
    weeklyfreq += len(tmp)

    tmp = soup.find_all("div",  {'class' : "total_group"})
    posts += extract_text(tmp)
    weeklyfreq += len(tmp)

    while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height != last_height:
                html = driver.page_source
                soup = BeautifulSoup(html,'html.parser')
                
                tmp = soup.find_all("a", {'class' : "api_txt_lines total_tit _cross_trigger"})
                posts += extract_text(tmp)
                weeklyfreq += len(tmp)

                tmp = soup.find_all("div",  {'class' : "total_group"})
                posts += extract_text(tmp)
                weeklyfreq += len(tmp)
            else:                                   # 일별로 검색 후 끝까지 scroll 다 내림
                weekly_post.append([startdate, weeklyfreq, posts])
                break

            last_height = new_height
    
    return weekly_post


def createDF(contents, keyword, tag):
    import pandas as pd
    df = pd.DataFrame(contents, columns=['Date', 'Weekly Frequency', 'Tweets'])
    df.to_excel("NAVER_" + keyword + "_" + str(tag) + ".xlsx")


if __name__ == "__main__":

    driver = wd.Chrome("chromedriver.exe")
    keywords = ["코로나, 감정", "코로나, 기분", "코로나, 일상"]
    years = [2020, 2021]

    for keyword in keywords:
            for year in years:
                contents = []
                if year == 2020: limit = 13
                elif year == 2021: limit = 11
                for m in range(1, limit):
                    i = m
                    if len(str(m)) == 1: m = str(0) + str(m)
                    base = str(year) + str(m)
                    startdate = base + "01"
                    for d in ["07", "14", "21", "28"]:
                        middate = base + d
                        url = f"https://search.naver.com/search.naver?where=view&query={keyword}&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom{startdate}to{middate}%2Ca%3Aall&mode=normal&main_q=&st_coll=&topic_r_cat="
                        contents += get_posts(url, startdate)
                        startdate = middate
                        # print(i)
                        
                    if i == 6 or i == limit-1:
                        if i == 6: add = "_상반기"
                        elif i == limit-1: add = "_하반기"
                        tag = str(year) + "년" + add
                        createDF(contents, keyword, tag)
                        contents = []