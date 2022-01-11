from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.MP # MP 이름의 DB에 접근



def index(request):
    boards = {'boards': db.board.find()}
    return render(request, 'mainpage/index.html', boards)

def post(request):
    if request.method == "POST":
        print("POST 발생!")
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        doc = {'author': author, 'title': title, 'content': content, 'created_date': timezone.now(), 'modified_date': None}
        db.board.insert_one(doc)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'mainpage/post.html')

def detail(request, id):
    try:
        board = db.board.find({'boardid': id})
    except board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board})