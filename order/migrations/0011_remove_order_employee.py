# Generated by Django 3.1.4 on 2021-01-25 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20210125_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='employee',
        ),
    ]
