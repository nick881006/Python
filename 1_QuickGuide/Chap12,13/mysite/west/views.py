# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
from django.contrib.auth import *
from django import forms
from west.models import Character

class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 200)

def first_page(request):
    return HttpResponse("<p>西餐</p>")

def staff(request):
    staff_list = Character.objects.all()
#    staff_str  = map(str, staff_list)
#    context   = {'label': ' '.join(staff_str)}
#    return render(request, 'templay.html', context)
    return render(request, 'templay.html', {'staffs': staff_list})

def templay(request):
    context          = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)

def form(request):
    return render(request, 'form.html')

def investigate(request):
#    rlt = request.GET['staff']
#    return HttpResponse(rlt)
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted  = form.cleaned_data['name']
            new_record = Character(name = submitted)
            new_record.save()
    
    form = CharacterForm()
    ctx ={}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form']  = form
    return render(request, "investigate.html", ctx)

def user_login(request):
    '''
    login
    '''
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(username=username, password=password)
        if user is not None:
            print "Correct!"
            login(request, user)
            return HttpResponse("<h1>log in</h1>")
    ctx = {}
    ctx.update(csrf(request))
    return render(request, 'login.html',ctx)

def register(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            new_user = form.save() 
        return HttpResponse("<h1>welcome new user</h1>") 
    else:
        form = UserCreationForm()
        ctx = {'form': form}
        ctx.update(csrf(request))       
        return render(request, "register.html", ctx)