from rest_framework import viewsets
from journal_manager.models import JournalImage, Journal
from journal_manager.serializers import ImageSerializer, JournalSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = JournalImage.objects.all()



class JournalViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            shared=self.request.data.get('shared'),
            images=self.request.data.get('images')
        )

    queryset = Journal.objects.all().order_by('-created_date')
    serializer_class = JournalSerializer
