"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 어떤 url 로 접근하면 어떤 View를 동작시킬 지 결정해야 한다 . 여기에 기록해 준다
#앱 안에 urls.py를 따로 만들어서 별도로 관리함
# url routing table 이라고 부름
urlpatterns = [
    #www.naver.com/admin/
    path('admin/', admin.site.urls),
]
