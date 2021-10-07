from rest_framework import viewsets
from event_manager.serializers import EventSerializer
from event_manager.models import Event


class EventViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        participants=self.request.data.get('participants'),
                        ideas=self.request.data.get('ideas'))

    queryset = Event.objects.all().order_by('-start_time')
    serializer_class = EventSerializer
