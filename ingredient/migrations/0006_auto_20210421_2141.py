# Generated by Django 3.1.4 on 2021-04-21 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_inventoryingredient_auto_ordering'),
        ('ingredient', '0005_auto_20210421_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='inventory_ingredient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='ingridients',
                to='stock.inventoryingredient'
            ),
        ),
    ]
