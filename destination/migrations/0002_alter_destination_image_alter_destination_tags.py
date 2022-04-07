# Generated by Django 4.0.3 on 2022-04-07 17:25

import destination.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.URLField(default='https://i.ibb.co/RvmN9CH/Biwako-Sunset.jpg'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='tags',
            field=models.JSONField(default=destination.models.tag_default, verbose_name='tags'),
        ),
    ]