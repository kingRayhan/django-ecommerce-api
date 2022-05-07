from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from .views import product_details, product_list, colection_details


urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>', product_details),
    path('collections/<int:pk>', colection_details, name='collection-detail'),
]
