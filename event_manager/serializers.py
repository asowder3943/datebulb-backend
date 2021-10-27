from rest_framework import serializers
from event_manager.models import Event
from idea_manager.serializers import DateIdeaSerializer


class EventSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    ideas = DateIdeaSerializer(many=True, read_only=True)
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    participants = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
