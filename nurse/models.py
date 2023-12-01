from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Chat(models.Model):
    message = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
    
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    county = models.CharField(max_length=50)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.username