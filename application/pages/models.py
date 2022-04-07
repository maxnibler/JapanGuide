from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class PageText(models.Model):
    PAGE_CHOICE = [
        ('HO', 'Home Page'),
        ('AB', 'About Page'),
        ('XX', 'Unused'),
    ]
    title = models.CharField(max_length=200)
    page = models.CharField(max_length=2, choices=PAGE_CHOICE, default='XX')
    contents = RichTextField(blank=True, null=True)
