from django.db import models
from django.contrib.auth.models import User
from idea_manager.models import DateIdea

# Create your models here.

class Event(models.Model):
    ideas = models.ManyToManyField(DateIdea)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(User)
    #participants = models.ForeignKey(User, related_name='participants', on_delete=models.CASCADE)
