from django.db import models
from django.urls import reverse

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=300)
    rating = models.IntegerField(default=3)

    def get_absolute_url(self):
        return reverse("destination-detail", kwargs={"pk": self.pk})
    