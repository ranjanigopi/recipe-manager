from django.db import models
from django import forms


# Create your models here.
class AddIngredient(forms.Form):
    Name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"placeholder": "Enter ingredient name.."}))
    Quantity = forms.IntegerField(required=True,
                                  widget=forms.NumberInput(attrs={"placeholder": "Enter quantity..", "min_value": "0"}))


class Unit(models.Model):
    unit = models.CharField(max_length=40)

    def str(self):
        return f"{self.unit}"


class Item(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, related_name="item_unit")
    name = models.CharField(max_length=75)

    def str(self):
        return f"{self.name} - {self.unit}"


class Pantry(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="pantry_item_id")
    quantity = models.IntegerField(default=0)

    def str(self):
        return f"Added {self.quantity} of {self.item}"


class Recipe(models.Model):
    name = models.CharField(max_length=75)

    def str(self):
        return f"Recipe: {self.name}"


class Step(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.SET_NULL, null=True, blank=True, related_name="recipe_id")
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=1000)

    def str(self):
        return f"{self.recipe}: {self.order} - {self.name} \n Description of the order: {self.description}"


class ShoppingList(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="shopping_item_id")
    quantity = models.IntegerField(default=0)

    def str(self):
        return f"To shop:\n {self.item} - {self.quantity}"


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.SET_NULL,null=True,blank=True,related_name="ingredient_recipe_id")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="ingredient_item_id")
    quantity = models.IntegerField(default=0)

    def str(self):
        return f"Recipe id: {self.recipe} \n Item: {self.item} \n Quantity: {self.quantity}"

