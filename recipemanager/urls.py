from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    # pantry page options
    path('pantry', views.view_pantry, name="pantry"),
    path('pantry/add', views.add_pantry_item, name="add-pantry-item"),

    # shopping list page options
    path('shopping-list', views.shoppinglist_menu, name="shopping-list"),
    path('shopping-list/add/<int:recipe_id>', views.add_shoppinglist, name="add-shopping-list"),

    # recipe page options
    path('recipe', views.recipe_menu, name="recipe"),
    path('recipe/all', views.all_recipe, name="all-recipe"),
    path('recipe/availability', views.available_recipe, name="available-recipe"),
    path('recipe/add', views.add_recipe, name="add-recipe"),
    path('recipe/save', views.save_recipe, name="save-recipe"),
    path('recipe/view/<int:id>', views.view_recipe, name="view-recipe"),
    path('recipe/done/<int:id>', views.done_recipe, name="done-recipe")
]
