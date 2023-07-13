from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} ({self.user.username})'