from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.MP # MP 이름의 DB에 접근


def index(request):
    boards = {'boards': db.knuboard.find().sort("boardid", pymongo.DESCENDING)}
    #count = db.knuboard.count_documents({})
    #doc = {'boardid': count+1, 'title': "TITLE TEST", 'knuurl': "https://www.naver.com", 'knuauthor': "홍길동", 'knudate': None, 'author': "KNUBOT", 'date': timezone.now()}
    #db.knuboard.insert_one(doc)
    return render(request, 'knu/index.html', boards)


#knuboard DB
#boardid, title, knuurl, knuauthor, knudate, author, date