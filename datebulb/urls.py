from django.urls import include, path
from rest_framework import routers
from user_manager import views as user_views
from idea_manager import views as idea_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'dateideas', idea_views.DateIdeaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
