from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField

# Create your models here.

class Destination(models.Model):
    REGION_CHOICES = [
        ('TO', 'Tokyo'),
        ('KA', 'Kansai'),
        ('TK', 'Tohoku'),
        ('HK', 'Hokkaido'),
        ('KY', 'Kyushu'),
        ('SK', 'Shikoku'),
    ]
    LOCATION_CHOICES = [
        # Tokyo Areas
        ('UAA', 'Ueno/Asakusa/Akihabara'),
        ('IKE', 'Ikebukuro'),
        ('SNK', 'Shinjuku/Nakano/Kichioji'),
        ('ARO', 'Asakasa/Roppongi'),
        ('SHS', 'Shibuya/Harajuku/Shimokitazawa'),
        ('SME', 'Shinagawa/Meguro/Ebisu'),
        # Kansai Areas
        ('KYT', 'Kyoto'),
        # Hokkaido
        ('SAP', 'Sapporo'),
    ]
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    region = models.CharField(max_length=2, choices=REGION_CHOICES, default=REGION_CHOICES[0])
    location = models.CharField(max_length=3, choices=LOCATION_CHOICES, default='UAA')
    rating = models.IntegerField(default=5, validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )

    def get_absolute_url(self):
        return reverse("destination-detail", kwargs={"pk": self.pk})
    