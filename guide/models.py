from django.db import models

# Create your models here.

class Guide(models.Model):
    name = models.CharField(max_length=200, default="Japan Guide")

