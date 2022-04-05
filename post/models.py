from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    featured = models.BooleanField(null=True, default=False)

    # get url to post's own page
    def get_absolute_url(self):
        return reverse("post-view", kwargs={"my_id": self.id})
    
