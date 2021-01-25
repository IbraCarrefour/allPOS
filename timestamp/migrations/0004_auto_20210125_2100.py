# Generated by Django 3.1.4 on 2021-01-25 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timestamp', '0003_timestapm_on_shift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestapm',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
