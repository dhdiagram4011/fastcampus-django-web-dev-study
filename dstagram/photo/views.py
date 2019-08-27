from django.shortcuts import render

# Create your views here.

# 클래스형뷰I(CRUD) 함수형뷰(다른 구조를 만들어야 될때)
# 클래스형 뷰는 제네릭 뷰를 상속받아서 만든다.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

from .models import Photo
class PhotoList(ListView):
    model = Photo
    #앱이름/모델명_list.html
    template_name = 'photo/photo_list.html'


