from rest_framework import viewsets
from idea_manager.serializers import DateIdeaSerializer
from idea_manager.models import DateIdea
from datetime import datetime as dt


class DateIdeaViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, created_date=dt.now())

    queryset = DateIdea.objects.all().order_by('-created_date')
    serializer_class = DateIdeaSerializer
