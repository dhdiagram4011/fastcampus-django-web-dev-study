from django.contrib import admin

# Register your models here.

from .models import *
class CategoryOption(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Category, CategoryOption)

class ProductOption(admin.ModelAdmin):
    list_display = ['id','category','name','price','stock','available_display','available_order','created','updated']
    raw_id_fields = ['category']
    list_editable = ['price','stock','available_display','available_order']

admin.site.register(Product,ProductOption)
