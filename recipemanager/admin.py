from django.contrib import admin
from .models import Unit, Item, ShoppingList, Ingredient, Step, Recipe, Pantry

# Register your models here.
for model in [
    Unit,
    Item,
    ShoppingList,
    Ingredient,
    Step,
    Recipe,
    Pantry
]:
   admin.site.register(model)
