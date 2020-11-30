
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add-ingredient', views.add_ingredient, name="add_ingredient",)
]
