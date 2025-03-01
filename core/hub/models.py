from django.db import models
from django.contrib.auth.models import User 

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=50, default="Python")
    objects = models.Manager()

    def __str__(self):
        return self.name