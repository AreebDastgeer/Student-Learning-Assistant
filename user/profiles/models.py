from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.JSONField(default=dict)
    learning_history = models.JSONField(default=list)

    def __str__(self):
        return self.user.username

