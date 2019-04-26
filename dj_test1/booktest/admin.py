# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bput_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender','hbook']
# Register your models here.

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
