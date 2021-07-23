from django.db import models
from django.urls import reverse

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=1024)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry:entries")
    
    