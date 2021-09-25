from rest_framework.views import APIView
from rest_framework.response import Response
from.permissions import IsOwner


class UserDetailView(APIView):
    permission_classes = [IsOwner]

    def get(self, request, *args, **kwargs):
        return Response({"email": request.user.email})
