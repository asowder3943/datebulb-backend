from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from idea_manager.serializers import DateIdeaSerializer
from idea_manager.models import DateIdea
from user_manager.permissions import IsOwner


class JournalViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = DateIdea.objects.all().order_by('-created_date')
    serializer_class = DateIdeaSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsOwner()]
        elif self.request.method == "POST":
            return [IsAuthenticated()]
        return [permission() for permission in self.permission_classes]




def perform_create(self, serializer):
        serializer.save(participants=[user for user in self.request.participants], idea=[idea for idea in self.request.ideas])