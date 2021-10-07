from rest_framework import serializers
from journal_manager.models import Journal, JournalImage
from drf_extra_fields.fields import Base64ImageField


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = JournalImage
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    shared = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_date = serializers.DateTimeField(required=False)
    message = serializers.CharField()
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Journal
        fields = '__all__'
