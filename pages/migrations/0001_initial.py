# Generated by Django 4.0.3 on 2022-04-06 18:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('page', models.CharField(choices=[('HO', 'Home Page'), ('AB', 'About Page'), ('XX', 'Unused')], default='XX', max_length=2)),
                ('contents', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
