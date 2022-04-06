# Generated by Django 4.0.3 on 2022-04-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0002_destination_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='location',
            field=models.CharField(choices=[('UAA', 'Ueno/Asakusa/Akihabara'), ('IKE', 'Ikebukuro'), ('SNK', 'Shinjuku/Nakano/Kichioji'), ('ARO', 'Asakasa/Roppongi'), ('SHS', 'Shibuya/Harajuku/Shimokitazawa'), ('SME', 'Shinagawa/Meguro/Ebisu'), ('KYT', 'Kyoto')], default='UAA', max_length=3),
        ),
        migrations.AlterField(
            model_name='destination',
            name='region',
            field=models.CharField(choices=[('TO', 'Tokyo'), ('KA', 'Kansai')], default='TO', max_length=2),
        ),
    ]