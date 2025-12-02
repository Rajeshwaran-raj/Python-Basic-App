
from django.urls import path
from . import views

urlpatterns=[
    path("items/", views.items_collection),
    path("items/<int:item_id>/", views.item_detail),
]
