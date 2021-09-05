from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DateIdea(models.Model):
    owner = models.ForeignKey(User, related_name='ideas', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.description 

