from django.contrib import admin
from django.conf.urls.static import static

import datebulb.settings as settings

from django.urls import include, path
from rest_framework import routers

from idea_manager import views as idea_views
from event_manager import views as event_views
from journal_manager.views import ImageViewSet, JournalViewSet
from screen_views.views import DashboardView

router = routers.DefaultRouter()
router.register(r'ideas', idea_views.DateIdeaViewSet)
router.register(r'events', event_views.EventViewSet)
router.register(r'images', ImageViewSet)
router.register(r'journals', JournalViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dashboard/', DashboardView.as_view(), name = "dashboard")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
