from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from event_manager.serializers import EventSerializer
from event_manager.models import Event
from idea_manager.serializers import DateIdeaSerializer
from idea_manager.models import DateIdea
from journal_manager.models import Journal
from journal_manager.serializers import JournalSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination


class DashboardView(ObjectMultipleModelAPIView):
    pagination_class = None

    def get_querylist(self):

        user = self.request.user
        print(user.id)
        querylist = [
            {'queryset': Event.objects.filter(
                participants__id=user.id), 'serializer_class': EventSerializer},
            {'queryset': DateIdea.objects.filter(
                owner=user), 'serializer_class': DateIdeaSerializer},
            {'queryset': Journal.objects.filter(
                owner=user), 'serializer_class': JournalSerializer}

        ]
        return querylist
