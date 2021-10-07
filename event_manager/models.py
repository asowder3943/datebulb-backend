from django.db import models
from django.contrib.auth.models import User
from idea_manager.models import DateIdea


class Event(models.Model):
    owner = models.ForeignKey(
        User, related_name='event_owner', on_delete=models.CASCADE)
    ideas = models.ManyToManyField(DateIdea, related_name='events')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(
        User, related_name='event_participants')
