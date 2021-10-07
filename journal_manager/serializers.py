from datetime import datetime
from rest_framework import serializers
from journal_manager.models import Journal


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()


class JournalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    shared = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_date = serializers.DateTimeField()
    message = serializers.CharField()
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Journal
        fields = '__all__'
