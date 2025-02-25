from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser import serializers as djoser_serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]


class UserCreateSerializer(djoser_serializers.UserCreateSerializer):
    class Meta(djoser_serializers.UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ["username", "password"]
