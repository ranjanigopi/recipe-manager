
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # index page options
    path('ingredient', views.ingredient, name="ingredient"),
    path('recipe', views.recipe, name="recipe"),
    path('shopping-list', views.shoppinglist, name="shopping-list"),

    # ingredient page options
    path('pantry', views.pantry, name="pantry"),
    path('pantry/add', views.add_pantry_item, name="add-pantry-item"),

    # recipe page options
    path('recipe/all', views.all_recipe, name="all-recipe"),
    path('recipe/available', views.available_recipe, name="available-recipe"),
    path('recipe/add', views.add_recipe, name="add-recipe"),


]
