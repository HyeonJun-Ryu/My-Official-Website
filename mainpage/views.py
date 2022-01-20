from django.shortcuts import render
from django.contrib import auth
from argon2 import PasswordHasher

import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.MP # MP 이름의 DB에 접근


def index(request):
    return render(request, 'mainpage/index2.html')

def tables(request):
    boards = {'boards': db.knuboard.find().sort("boardid", pymongo.DESCENDING)}
    return render(request, 'mainpage/tables.html', boards)

def forms(request):
    return render(request, 'mainpage/forms.html')

def register(request):
    if request.method == "GET":
        return render(request, 'mainpage/register.html')
    elif request.method == "POST":
        username = request.POST.get('registerUsername')  # 딕셔너리형태
        email = request.POST.get('registerEmail')
        password = request.POST.get('registerPassword')
        repassword = request.POST.get('registerRePassword')
        res_data = {}
        if (password != repassword):
            print("비밀번호 불일치!!!")
            res_data['error'] = "비밀번호 불일치!!!!!!"
            return render(request, 'mainpage/register.html', res_data)
        doc = {'username': username, 'email': email, 'password': PasswordHasher().hash(password)}
        #PasswordHasher().verify(암호화된 비밀번호, 입력받은 비밀번호)
        db.user.insert_one(doc)
        print(username, "가입!\nPW: ", PasswordHasher().hash(password), "\nemail: ", email, "\n")
        return render(request, 'mainpage/index2.html')


def login(request):
    if request.method == "GET":
        return render(request, 'mainpage/login.html')
    elif request.method == "POST":
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        print(username, "\n",password)
        dict = db.user.find({'username': username})
        print(dict['password'])
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