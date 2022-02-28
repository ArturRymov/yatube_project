from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Страница со списком сообществ
def groups(request):
    return HttpResponse(f'Список сообществ')

# Страница со названием сообщества
def group_posts(request, slug):
    return HttpResponse(f'Сообщество с названием {slug}')


