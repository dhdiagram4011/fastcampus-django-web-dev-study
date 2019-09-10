from django.urls import path
from .views import *

app_name = 'cart'
urlpatterns = [
    path('remove/<product_id>/', remove, name='remove_product'),
    path('add/<int:product_id>/', add, name='add_product'),
    path("", detail, name='detail'),

]