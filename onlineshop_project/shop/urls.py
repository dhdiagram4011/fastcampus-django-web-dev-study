from django.urls import path

from .views import *
urlpatterns = [
    path('product/<int:id>/<product_slug>/', product_detail, name='product_detail'),
]