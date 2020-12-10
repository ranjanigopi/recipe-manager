from django.shortcuts import render
from .form.AddPantryItem import AddPantryItem
from .models import Unit, Item, ShoppingList, Ingredient, Step, Recipe, Pantry
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db.models import ObjectDoesNotExist

import json


# Create your views here.


def index(request):
    return render(request, "recipemanager/index.html")


def ingredient_menu(request):
    return render(request, "recipemanager/ingredient.html")


def recipe_menu(request):
    return render(request, "recipemanager/recipe.html")


def add_shoppinglist(request, recipe_id):
    ingredients = Ingredient.objects.filter(recipe=recipe_id)
    for ingredient in ingredients:
        s = ShoppingList(item=ingredient.item, quantity=ingredient.quantity, unit=ingredient.unit)
        s.save()
    return HttpResponseRedirect(reverse("shopping-list"))


def shoppinglist_menu(request):
    shopping_lists = ShoppingList.objects.all()
    return render(request, "recipemanager/shoppinglist.html", {
        "shopping_lists": shopping_lists
    })


def pantry(request):
    item = Pantry.objects.all()
    return render(request, "recipemanager/pantry.html", {
        "items": item
    })


def view_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    ingredients = Ingredient.objects.filter(recipe=id)
    steps = Step.objects.filter(recipe=id)
    unavailable = request.GET.get("unavailable") == "true"
    return render(request, "recipemanager/recipe-view.html", {
        "recipe": recipe,
        "ingredients": ingredients,
        "steps": steps,
        "unavailable": unavailable
    })


def add_pantry_item(request):
    form = AddPantryItem(request.POST or None)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "cancel":
            return HttpResponseRedirect(reverse("pantry"))
        if action == "create" and form.is_valid():
            name = form.cleaned_data["Name"]
            quantity = form.cleaned_data["Quantity"]
            unit = form.cleaned_data["Unit"]
            add_item(name, quantity, unit)
            form = AddPantryItem(None)
    return render(request, "recipemanager/add_pantry_item.html", {
        "form": form
    })


def all_recipe(request):
    recipes = Recipe.objects.all()
    return render(request, "recipemanager/all_recipe.html", {
        "recipes": recipes
    })


def done_recipe(request, id):
    ingredient = Ingredient.objects.filter(recipe_id=id)
    for ing in ingredient:
        p = Pantry.objects.get(item_id=ing.item_id)
        u = Unit.objects.get(id=ing.unit_id)
        p.quantity -= (ing.quantity * u.rate)
        if p.quantity < 0:
            p.quantity = 0
        p.save()
    return HttpResponseRedirect(reverse("all-recipe"))


def ingredient_in_pantry(ingredient):
    try:
        return Pantry.objects.get(item=ingredient.item).quantity >= \
               ingredient.quantity * Unit.objects.get(id=ingredient.unit_id).rate
    except ObjectDoesNotExist:
        return False


def available_recipe(request):
    recipes = Recipe.objects.all()
    available_recipes = []
    unavailable_recipes = []
    for recipe in recipes:
        if all(ingredient_in_pantry(ingredient) for ingredient in recipe.ingredient_recipe_id.all()):
            available_recipes.append(recipe)
        else:
            unavailable_recipes.append(recipe)
    return render(request, "recipemanager/recipe_availability.html", {
        "available_recipes": available_recipes,
        "unavailable_recipes": unavailable_recipes,
    })


def add_recipe(request):
    if request.method == "GET":
        return render(request, "recipemanager/add_recipe.html", {
            'units': Unit.objects.all()
        })


def add_item(name, new_quantity, unit):
    item = add_new_item(name, unit)
    rate = Unit.objects.get(unit=unit).rate
    pantry_item = Pantry.objects.filter(item=item)
    quantity = new_quantity * rate
    if pantry_item.exists():
        p = pantry_item[0]
        p.quantity += quantity
    else:
        p = Pantry(item=item, quantity=quantity)
    p.save()


def add_new_item(name, unit):
    item = Item.objects.filter(name=name)
    if item.exists():
        return item[0]
    else:
        base_unit = Unit.objects.get(unit=unit).base_unit
        item = Item(name=name, unit_type=base_unit)
        item.save()
        return item


@csrf_exempt
def save_recipe(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        image = data.get('image')
        time = data.get('time')
        r = Recipe(name=name, image=image, time=time)
        r.save()
        recipe_ingredient = data.get('ingredients')
        for ing in recipe_ingredient:
            unit = Unit.objects.get(id=ing['unit'])
            item = add_new_item(ing['ingredient'], unit)
            i = Ingredient(quantity=ing['quantity'], item=item, recipe=r, unit=unit)
            i.save()
        steps = data.get('steps')
        for step in steps:
            s = Step(order=step['stepNumber'], name=step['stepName'], description=step['stepProcedure'], recipe=r)
            s.save()
        return HttpResponse(status=204)
    return HttpResponse(status=400)
