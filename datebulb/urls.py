from django.contrib import admin


from django.urls import include, path
from rest_framework import routers

from idea_manager import views as idea_views
from event_manager import views as event_views

from user_manager.views import UserDetailView
from allauth.account.views import confirm_email

router = routers.DefaultRouter()
router.register(r'dateideas', idea_views.DateIdeaViewSet)
router.register(r'events', event_views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('me/', UserDetailView.as_view())
]
