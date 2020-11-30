from django.shortcuts import render
from .models import AddIngredient

# Create your views here.


def index(request):
    return render(request, "recipemanager/index.html")


def add_ingredient(request):
    form = AddIngredient(request.POST or None)
    if form.is_valid():
        i = Ingredient(
            **form.cleaned_data,
                      )
        i.save()
    return render(request, "recipemanager/add_ingredient.html", {
        "form" : form
    })

