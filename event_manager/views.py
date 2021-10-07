from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from event_manager.serializers import EventSerializer
from event_manager.models import Event
from user_manager.permissions import IsOwner
from pprint import pprint
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(participants=self.request.data.get('participants'),
        ideas=self.request.data.get('ideas'))

    queryset = Event.objects.all().order_by('-start_time')
    serializer_class = EventSerializer 

    #def get_permissions(self):
    #    if self.request.method == "GET":
    #        return [IsOwner()]
    #    elif self.request.method == "POST":
    #        return [IsAuthenticated()]
    #    return [permission() for permission in self.permission_classes]


