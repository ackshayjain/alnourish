
from django.db import models
# import os
from datetime import datetime, timedelta


class Culture(models.Model):

    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    volume = models.IntegerField()

    test_date = models.CharField(max_length = 200,default='')
    ph_test = models.CharField(max_length=200,default='')

    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime.now() + timedelta(days=15))


    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
