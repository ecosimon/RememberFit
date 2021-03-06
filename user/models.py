from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
        This model is a custom UserProfile so that each User in the future, can modify their information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(decimal_places=2,max_digits=5, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    weight = models.DecimalField(decimal_places=2,max_digits=5, null=True)

    def __str__(self):
        return self.user.username
