# Generated by Django 4.1.4 on 2022-12-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_recipe_directions_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]