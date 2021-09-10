from django.urls import include, path
from rest_framework import routers
from user_manager.views import *
from idea_manager import views as idea_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'dateideas', idea_views.DateIdeaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
