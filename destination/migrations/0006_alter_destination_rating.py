# Generated by Django 4.0.3 on 2022-04-06 16:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0005_alter_destination_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
