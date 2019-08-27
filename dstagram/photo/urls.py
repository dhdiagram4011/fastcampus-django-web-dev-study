from django.urls import path
from .views import PhotoList

urlpatterns = [
    path("",PhotoList.as_view(), name='photo_list'), #url패턴, 뷰 , urlpattern의 이름  as_view : 클래스형 뷰를 함수형 뷰로 변경
]

