from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from event_manager.models import Event


class JournalImage(models.Model):
    image = ImageField(upload_to='journal_images')


class Journal(models.Model):
    owner = models.ForeignKey(
        User, related_name='journals', on_delete=models.CASCADE)
    shared = models.ManyToManyField(User, related_name='journals_shared')
    created_date = models.DateTimeField()
    message = models.TextField()
    images = models.ManyToManyField(JournalImage, related_name="journals")
    events = models.ManyToManyField(Event, related_name="journals")

    def __str__(self) -> str:
        return f"{self.owner} - {self.message}"
