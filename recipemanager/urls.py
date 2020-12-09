
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # index page options
    path('ingredient', views.ingredient_menu, name="ingredient"),
    path('recipe', views.recipe_menu, name="recipe"),
    path('shopping-list', views.shoppinglist_menu, name="shopping-list"),

    # ingredient page options
    path('pantry', views.pantry, name="pantry"),
    path('pantry/add', views.add_pantry_item, name="add-pantry-item"),

    # recipe page options
    path('recipe/all', views.all_recipe, name="all-recipe"),
    path('recipe/available', views.available_recipe, name="available-recipe"),
    path('recipe/add', views.add_recipe, name="add-recipe"),
    path('recipe/save', views.save_recipe, name="save-recipe"),
    path('recipe/view/<int:id>', views.view_recipe, name="view-recipe"),
    path('recipe/done/<int:id>', views.done_recipe, name="done-recipe")
]
