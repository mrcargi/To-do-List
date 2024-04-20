from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True)
    
    

    
    def __str__(self):
        return self.title
