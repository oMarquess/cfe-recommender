from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view),
    path('<int:pk>/', views.product_detail_view),
]
