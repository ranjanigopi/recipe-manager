# Generated by Django 3.1.3 on 2020-12-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipemanager', '0007_auto_20201202_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit_type',
            field=models.CharField(choices=[('gm', 'Gram'), ('ml', 'MilliLitre')], default='Select unit type', max_length=64),
        ),
    ]