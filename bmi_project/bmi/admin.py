from django.contrib import admin

# Register your models here.
# 1. 모델을 관리자 페이지에 등록한다
# 2. 모델 목록에 보일 내용을 변경한다.
# 3. 관리자 페이지에 기능을 변경한다.

from .models import BMI

class BMIOption(admin.ModelAdmin):
    list_display = ['id','name','height','weight','bmi_level']


admin.site.register(BMI, BMIOption)


