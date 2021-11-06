from django.db import models

# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)