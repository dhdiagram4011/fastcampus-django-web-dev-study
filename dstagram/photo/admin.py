from django.contrib import admin
#
# # Register your models here.

from .models import Photo

class PhotoOption(admin.ModelAdmin):
    list_display = ['id','owner','image','created','updated']

admin.site.register(Photo, PhotoOption)
