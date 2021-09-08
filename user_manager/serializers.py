from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    # take plain text as input, but store passwords as hashes
    def create(self, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(
                validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(
                validated_data["password"])
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = '__all__'
