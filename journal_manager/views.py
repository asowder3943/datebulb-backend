from rest_framework import viewsets
from idea_manager.models import DateIdea
from journal_manager.serializers import ImageSerializer, JournalSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer


class JournalViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            shared=self.request.data.get('shared'),
            images=self.request.data.get('images')
        )

    queryset = DateIdea.objects.all().order_by('-created_date')
    serializer_class = JournalSerializer
