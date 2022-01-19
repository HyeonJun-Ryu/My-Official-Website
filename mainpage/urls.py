from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('tables', views.tables, name='tables'),
    path('forms', views.forms, name='forms'),
    path('register', views.register, name='register'),
    path('charts', views.charts, name='charts'),
    # path('post', views.post, name='post'),
    # path('post/<int:boardid>/', views.detail, name='detail'),
]