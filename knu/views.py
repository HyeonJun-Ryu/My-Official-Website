from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.MP # MP 이름의 DB에 접근


def index(request):
    boards = {'boards': db.knuboard.find()}
    return render(request, 'knu/index.html', boards)
