from django.db import models
from django.db.models.fields import CharField, DateTimeField

#test model for tracks

class Track(models.Model):
    title = CharField(max_length=200)
    image = CharField(max_length=1000, blank=True)
    created_at = DateTimeField(auto_now_add=True)
