# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

def create(request):
    b = BookInfo()
    b.btitle = 'liuxinghudiejian'
    b.bpub_date = date(1990,1,1)
    b.save()
    #return HttpResponseRedirect('/index')
    return redirect('/index')


def delete(request,bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    #return HttpResponseRedirect('/index')
    return redirect('/index')