import requests
import urllib.request
from bs4 import BeautifulSoup
import time
from time import sleep
import re
from datetime import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.MP # MP 이름의 DB에 접근

id = "knubot1"
pw = "knubot1"


sindex = 3674



index = int(sindex)
url = "https://computer.knu.ac.kr/06_sub/02_sub.html?no=" + str(sindex) + "&bbs_cmd=view&page=1&key=&keyfield=&category=&bbs_code=Site_BBS_25"


def clean_text(text):
    pattern = '<[^>]*>'
    text = re.sub(pattern=pattern, repl='', string=text)
    text.replace("\n", "")
    text.replace(" ", "")
    text.replace("\n", "")
    #print("태그 제거 : " , text , "\n")
    return text

def getinfo(html):
    bs_html = BeautifulSoup(html.content, "html.parser")

    title = bs_html.find("div", {"class": "kboard-title"})
    #print(title.text)

    # content = bs_html.find("div", {"class": "content-view"})
    # string = str(content)
    # string = clean_text(string)
    # content = string
    # #print(string)

    date = bs_html.find("div", {"class": "detail-attr detail-date"})
    string = str(date.text)
    string = string[5:]
    date = string
    date = date.replace("\n", "")
    #print(date)

    author = bs_html.find("div", {"class": "detail-attr detail-writer"})
    author = bs_html.find("div", {"class": "detail-value"})
    author = clean_text(str(author))
    #print(author)



    # if(bs_html.find("div", {"class": "kboard-attach"}) != None):
    #     fileList = bs_html.find_all("div", {"class": "kboard-attach"})
    #     fileS = ''
    #     for file in fileList:
    #         fileS = fileS + '\n' + file.text
    #
    #     #print(fileS)


    title = clean_text(title.text)
    title = title.strip()
    #print(title)
    dict = {'title': title, 'date': date, 'author': author}
    return dict

    print(date)
    #print(content)


while(1):
    sindex = str(index)
    url = "https://computer.knu.ac.kr/06_sub/02_sub.html?no=" + sindex + "&bbs_cmd=view&page=1&key=&keyfield=&category=&bbs_code=Site_BBS_25"
    test = urllib.request.urlopen(url)
    html = requests.get(url)
    if (test.status == 200):
        print("URL 접근!", datetime.now())
        print("index: ", index)
        dict = getinfo(html)

        if (dict['title'] == ""):
            index += 1
            sindex = str(index)
            url = "https://computer.knu.ac.kr/06_sub/02_sub.html?no=" + sindex + "&bbs_cmd=view&page=1&key=&keyfield=&category=&bbs_code=Site_BBS_25"
            test = urllib.request.urlopen(url)
            html = requests.get(url)
            dict = getinfo(html)
            if (dict['title'] == ""):
                index -= 1
                print("Failed, 대기..")
                sleep(600)
                print("업데이트 재개!!!")
            else:
                count = db.knuboard.count_documents({})
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                # print(current_time)
                doc = {'boardid': index, 'title': dict['title'], 'knuurl': url, 'knuauthor': dict['author'],
                       'knudate': dict['date'], 'author': "KNUBOT", 'date': current_time}
                # print(dict['date'])
                try:
                    db.knuboard.insert_one(doc)
                except:
                    print("중복된 데이터 삽입 오류")
                index += 1

        else:
            count = db.knuboard.count_documents({})
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            #print(current_time)
            doc = {'boardid': index, 'title': dict['title'], 'knuurl': url, 'knuauthor': dict['author'], 'knudate': dict['date'], 'author': "KNUBOT", 'date': current_time}
            #print(dict['date'])
            try:
                db.knuboard.insert_one(doc)
            except:
                print("중복된 데이터 삽입 오류")
            index += 1

    else:
        print("잘못된 데이터 전달")
        break








