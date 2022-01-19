from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import auth

import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
boarddb = client.MP # MP 이름의 DB에 접근
knudb = client.MP

def index(request):
    return render(request, 'mainpage/index2.html')

def tables(request):
    boards = {'boards': knudb.knuboard.find().sort("boardid", pymongo.DESCENDING)}
    return render(request, 'mainpage/tables.html', boards)

def forms(request):
    return render(request, 'mainpage/forms.html')

def register(request):
    if request.method == "GET":
        return render(request, 'mainpage/register.html')
    elif request.method == "POST":
        print("POST접근")
        username = request.POST.get('registerUsername')  # 딕셔너리형태
        email = request.POST.get('registerEmail')
        password = request.POST.get('registerPassword')
        res_data = {}

        print(username, "가입!\nPW: ", password, "\nemail: ", email, "\n")
        return render(request, 'mainpage/index2.html')


def login(request):

    return render(request, 'mainpage/login.html')

def charts(request):
    return render(request, 'mainpage/charts.html')

# def post(request):
#     if request.method == "POST":
#         count = db.board.count_documents({})
#         print("POST 발생! ", count)
#         author = request.POST['author']
#         title = request.POST['title']
#         content = request.POST['content']
#         doc = {'boardid': count+1, 'author': author, 'title': title, 'content': content, 'created_date': timezone.now(), 'modified_date': None}
#         db.board.insert_one(doc)
#         return HttpResponseRedirect(reverse('index'))
#     else:
#         return render(request, 'mainpage/post.html')
#
# def detail(request, boardid):
#     try:
#         doc = db.board.find_one({'boardid': boardid})
#         #doc = {'title': "TEST TITLE"}
#     except doc.DoesNotExist:
#         raise Http404("Does not exist!")
#     return render(request, 'mainpage/detail.html', {'board': doc})
#
# def edit(request):
#     return