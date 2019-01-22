from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.DecimalField(decimal_places=2,max_digits=5)
    age = models.PositiveIntegerField()
    weight = models.DecimalField(decimal_places=2,max_digits=5)

    def __str__(self):
        return self.user
