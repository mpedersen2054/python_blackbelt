from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class TravelManager(models.Manager):
    pass

# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    added_by    = models.OneToOneField('log_and_reg.User', on_delete=models.CASCADE)
    date_from   = models.DateTimeField(default=datetime.now)
    date_to     = models.DateTimeField(default=datetime.now)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = TravelManager()
