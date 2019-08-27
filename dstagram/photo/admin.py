from django.contrib import admin
#
# # Register your models here.

from .models import Photo

class PhotoOption(admin.ModelAdmin):
    list_display = ['id','owner','image','created','updated']
    list_filter=['created','updated']
    search_fields = ['description','created','owner__username']
    #onwer__username = owner라는 객체 안에 username 을 이용한다
    ordering = ['-id'] #데이터베이스에 영향을 주지 않음
    raw_id_fields = ['owner']

admin.site.register(Photo, PhotoOption)