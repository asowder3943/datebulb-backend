from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from idea_manager.serializers import DateIdeaSerializer
from idea_manager.models import DateIdea
from idea_manager.permissions import IsOwner
# Create your views here.

class DateIdeaViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = DateIdea.objects.all().order_by('-created_date')
    serializer_class = DateIdeaSerializer
    permission_classes = [IsOwner]

