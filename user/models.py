from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.DecimalField(decimal_places=2, 'Round height in inches to nearest two deciml places')
    age = models.PositiveIntegerField()
    weight = models.DecimalField(decimal_places=2,'Round weight in inches to nearest two deciml places')

    def __str__(self):
        return self.user
