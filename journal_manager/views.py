from rest_framework import viewsets
from journal_manager.models import JournalImage, Journal
from journal_manager.serializers import ImageSerializer, JournalSerializer
from datetime import datetime as dt

class ImageViewSet(viewsets.ModelViewSet):
    queryset = JournalImage.objects.all()
    serializer_class = ImageSerializer



class JournalViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            shared=self.request.data.get('shared'),
            images=self.request.data.get('images'),
            created_date=dt.now()
        )

    queryset = Journal.objects.all().order_by('-created_date')
    serializer_class = JournalSerializer
