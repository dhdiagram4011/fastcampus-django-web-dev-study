# 기존 뷰가 있다
# 기능, 탬플릿 파일
# 상속받아서 오버라이드

## 장고의 로그인 페이지는 장고 관리자의 로그인 페이지를 디자인을 바꾸어서 이용한다


from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

]

