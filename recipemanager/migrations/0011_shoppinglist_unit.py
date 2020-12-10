# Generated by Django 3.1.3 on 2020-12-10 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipemanager', '0010_recipe_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shopping_unit_id', to='recipemanager.unit'),
        ),
    ]
