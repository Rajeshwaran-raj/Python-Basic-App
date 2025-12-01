from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.item_list_create, name='item_list_create'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
]
