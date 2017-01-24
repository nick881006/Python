#coding=utf-8
from django.http import HttpResponse
from django.contrib.auth import *

def first_page(request):
    return HttpResponse("<p>Hello World</p>")

def user_logout(request):
    '''
    logout
    URL: /users/logout
    '''
    logout(request)
    return HttpResponse("<h1>log out</h1>")