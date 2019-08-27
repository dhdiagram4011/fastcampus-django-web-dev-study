from django.urls import path
from .views import *

#url패턴, 뷰 , urlpattern의 이름  as_view : 클래스형 뷰를 함수형 뷰로 변경
urlpatterns = [
    path("",PhotoList.as_view(), name='photo_list'),

    path("detail/<int:pk>/",PhotoDetail.as_view(), name='photo_detail'),
    path("update/<int:pk>/",PhotoUpdate.as_view(), name='photo_update'),
    path("delete/<int:pk>/",PhotoDelete.as_view(), name='photo_delete'),
    path("upload/",PhotoCreate.as_view(), name='photo_create'),


]

