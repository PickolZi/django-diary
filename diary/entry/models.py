from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=1024)
    date = models.DateField(default = datetime.date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry:entries")
    
    