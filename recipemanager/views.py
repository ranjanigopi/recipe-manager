from django.shortcuts import render
from .form.AddItem import AddItem
from .models import Unit, Item, ShoppingList, Ingredient, Step, Recipe, Pantry
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db.models import ObjectDoesNotExist

import json


# Create your views here.


def index(request):
    return render(request, "recipemanager/index.html")


def add_shoppinglist(request, recipe_id):
    ingredients = Ingredient.objects.filter(recipe=recipe_id)
    for ingredient in ingredients:
        try:
            s = ShoppingList.objects.get(item=ingredient.item)
            s.quantity += s.quantity
        except ObjectDoesNotExist:
            s = ShoppingList(item=ingredient.item, quantity=ingredient.quantity, unit=ingredient.unit)
        finally:
            s.save()
    return HttpResponseRedirect(reverse("shopping-list"))


def add_shoppinglist_item(request):
    form = AddItem(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["Name"]
            quantity = form.cleaned_data["Quantity"]
            unit = form.cleaned_data["Unit"]
            add_shopping_item(name, quantity, unit)
            form = AddItem(None)
    return render(request, "recipemanager/add_item.html", {
        "form": form,
        "title": "Add Shopping List Item",
        "cancel_view": "shopping-list"
    })


def shoppinglist_menu(request):
    if request.method == "POST":
        action = request.POST.get("action")
        id = request.POST.get('id')
        if action == "buy":
            name = request.POST.get('name')
            quantity = int(request.POST.get('quantity'))
            unit = Unit.objects.get(id=request.POST.get('unit')).unit
            add_item(name, quantity, unit)
        s = ShoppingList.objects.get(id=id)
        s.delete()
    shoppinglists = ShoppingList.objects.all()
    return render(request, "recipemanager/shopping_list.html", {
        "shoppinglists": shoppinglists,
        "units": Unit.objects.all()
    })


def view_pantry(request):
    items = Pantry.objects.all()
    return render(request, "recipemanager/pantry.html", {
        "items": items
    })


def view_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    ingredients = Ingredient.objects.filter(recipe=id)
    steps = Step.objects.filter(recipe=id).order_by('order')
    return render(request, "recipemanager/recipe_view.html", {
        "recipe": recipe,
        "ingredients": ingredients,
        "steps": steps,
        "available": request.GET.get("available") == "true",
        "unavailable": request.GET.get("unavailable") == "true"
    })


def add_pantry_item(request):
    form = AddItem(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["Name"]
            quantity = form.cleaned_data["Quantity"]
            unit = form.cleaned_data["Unit"]
            add_item(name, quantity, unit)
            form = AddItem(None)
    return render(request, "recipemanager/add_item.html", {
        "form": form,
        "title": "Add Pantry Item",
        "cancel_view": "pantry"
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
    return HttpResponseRedirect(reverse("recipe"))


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


def add_shopping_item(name, new_quantity, unit_name):
    item = add_new_item(name, unit_name)
    unit = Unit.objects.get(unit=unit_name)
    rate = unit.rate
    shopping_item = ShoppingList.objects.filter(item=item)
    quantity = new_quantity * rate
    if shopping_item.exists():
        s = shopping_item[0]
        s.quantity += quantity
    else:
        s = ShoppingList(item=item, quantity=quantity, unit=unit)
    s.save()


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
