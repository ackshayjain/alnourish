
from django.db import models
# import os


class Culture(models.Model):

    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    volume = models.IntegerField()
    # desc = models.TextField(max_length=400)
    # location = models.CharField(max_length=100)

    # lat = models.FloatField(default="0")
    # lon = models.FloatField(default="0")

    # pic = models.ImageField(upload_to='img')

    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
