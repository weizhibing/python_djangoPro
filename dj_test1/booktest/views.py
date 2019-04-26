# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo

from django.template import loader,RequestContext



# Create your views here.
def index(request):
    #return HttpResponse('laotie,meimaobing')
    return render(request,'booktest/index.html',
                  {'content':'hello word'})
def index2(request):
    return HttpResponse('hello python')

def show_books(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/show_books.html',
                  {'books':books})

def detail(request,bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all
    return render(request,'booktest/detail.html',
                  {'book':book,'heros':heros})