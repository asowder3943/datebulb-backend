from rest_framework import serializers
from journal_manager.models import Journal


class JournalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_date = serializers.DateTimeField()
    message = serializers.CharField()
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Journal
        fields = '__all__'
