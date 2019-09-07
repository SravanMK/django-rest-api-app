from django.urls import path
from rest_framework import request

from . import views

urlpatterns = {
    path('stock/', views.Stock, name='Stock'),
    path('index/', views.StockTemplate.as_view(), name='Stock'),
    # url(r'^api-auth/', include('rest_framework.urls'))
    path('automail/', views.email),
}