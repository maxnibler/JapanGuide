# Generated by Django 4.0.3 on 2022-04-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0009_alter_destination_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.URLField(),
        ),
    ]