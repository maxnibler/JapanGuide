from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
def tag_default():
    return {"list": []}

class Guide(models.Model):
    name = models.CharField(max_length=200, default="Japan Guide")
    description = models.TextField(blank=True, null=True)
    contents = RichTextField(blank=True, null=True)
    tags = models.JSONField("tags", default=tag_default)

    def get_absolute_url(self):
        return reverse("guide-detail", kwargs={"pk": self.pk})
    