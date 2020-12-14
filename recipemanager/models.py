from django.db import models

# Create your models here.

base = [('gm', 'Gram'), ('ml', 'MilliLitre')]


class Unit(models.Model):
    unit = models.CharField(max_length=40)
    base_unit = models.CharField(choices=base,max_length=40, default="Select base unit")
    rate = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.unit}"

# Items and its measuring units


class Item(models.Model):
    name = models.CharField(max_length=75, unique=True)
    unit_type = models.CharField(choices=base, max_length=64, default="Select unit type")

    def __str__(self):
        return f"{self.name}"

# Items available in pantry with quantity


class Pantry(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="pantry_item_id")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item} - {self.quantity}"


class Recipe(models.Model):
    name = models.CharField(max_length=75)
    image = models.URLField(default=None)
    time = models.IntegerField(default=0)

    def __str__(self):
        return f"Recipe: {self.name}"


class Step(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE, null=True, blank=True, related_name="recipe_id")

    order = models.IntegerField(default=0)
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.recipe}: {self.order} - {self.name} \n Description of the order: {self.description}"


class ShoppingList(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="shopping_item_id")
    quantity = models.IntegerField(default=0)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, related_name="shopping_unit_id")

    def __str__(self):
        return f"To shop:\n {self.item} - {self.quantity}"


# Ingredients to cook


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE,null=True,blank=True, related_name="ingredient_recipe_id")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="ingredient_item_id")
    quantity = models.IntegerField(default=0)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, related_name="ingredient_unit_id")

    def __str__(self):
        return f"Recipe id: {self.recipe} \n Item: {self.item} \n Quantity: {self.quantity} {self.unit.unit}"
