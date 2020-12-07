from django.shortcuts import render
from .form.AddPantryItem import AddPantryItem
from .models import Unit, Item, ShoppingList, Ingredient, Step, Recipe, Pantry
import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    return render(request, "recipemanager/index.html")


def ingredient(request):
    return render(request, "recipemanager/ingredient.html")


def recipe(request):
    return render(request, "recipemanager/recipe.html")


def shoppinglist(request):
    return render(request, "recipemanager/shoppinglist.html")


def pantry(request):
    item = Pantry.objects.all()
    return render(request, "recipemanager/pantry.html", {
        "items": item
    })


def add_pantry_item(request):
    form = AddPantryItem(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["Name"]
            quantity = form.cleaned_data["Quantity"]
            unit = form.cleaned_data["Unit"]
            add_item(name, quantity, unit)
            form = AddPantryItem(None)
    return render(request, "recipemanager/add_pantry_item.html", {
        "form": form
    })


def all_recipe(request):
    return render(request, "recipemanager/index.html")


def available_recipe(request):
    return render(request, "recipemanager/index.html")


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
        r = Recipe(name=name, image=image)
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
