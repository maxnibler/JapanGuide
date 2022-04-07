# Generated by Django 4.0.3 on 2022-04-07 17:17

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('region', models.CharField(choices=[('TO', 'Tokyo'), ('KA', 'Kansai'), ('TK', 'Tohoku'), ('HK', 'Hokkaido'), ('KY', 'Kyushu'), ('SK', 'Shikoku')], default=('TO', 'Tokyo'), max_length=2)),
                ('location', models.CharField(choices=[('UAA', 'Ueno/Asakusa/Akihabara'), ('IKE', 'Ikebukuro'), ('SNK', 'Shinjuku/Nakano/Kichioji'), ('ARO', 'Asakasa/Roppongi'), ('SHS', 'Shibuya/Harajuku/Shimokitazawa'), ('SME', 'Shinagawa/Meguro/Ebisu'), ('KYT', 'Kyoto'), ('SAP', 'Sapporo')], default=('UAA', 'Ueno/Asakusa/Akihabara'), max_length=3)),
                ('rating', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('tags', models.JSONField()),
            ],
        ),
    ]
