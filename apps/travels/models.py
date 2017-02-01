from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class TravelManager(models.Manager):
    def format_data(self, postData, user):
        df = postData['date_from'].split('-')
        dt = postData['date_to'].split('-')
        date_from = datetime(int(df[0]), int(df[1]), int(df[2]))
        date_to = datetime(int(dt[0]), int(dt[1]), int(dt[2]))

        return {
            'destination': postData['destination'],
            'description': postData['description'],
            'date_from': date_from,
            'date_to': date_to
        }

    def check_validity(self, data):
        errors = []

        if len(data['destination']) < 3:
            errors.append('Destination needs to be more than 3 characters.')
        if len(data['description']) < 3:
            errors.append('Description needs to be more than 3 characters.')

        if not data['date_from'] or not data['date_to']:
            errors.append('You need to enter dates.')
        else:
            df = data['date_from'].split('-')
            dt = data['date_to'].split('-')
            date_from = datetime(int(df[0]), int(df[1]), int(df[2]))
            date_to = datetime(int(dt[0]), int(dt[1]), int(dt[2]))

            if date_from < datetime.now() or date_to < datetime.now():
                errors.append('The dates must be future based.')

            if date_from > date_to:
                errors.append("The 'from date' needs to be before the 'to date'.")

        return errors

# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    added_by    = models.ForeignKey('log_and_reg.User', on_delete=models.CASCADE)
    date_from   = models.DateTimeField(default=datetime.now)
    date_to     = models.DateTimeField(default=datetime.now)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = TravelManager()
