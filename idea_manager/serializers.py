from rest_framework import serializers
from idea_manager.models import DateIdea

class DateIdeaSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    created_date = serializers.DateTimeField()
    description = serializers.CharField()
    location = serializers.CharField()

    class Meta:
        model = DateIdea
        fields = '__all__'
    
