from rest_framework import serializers
from togather.models import TogatherUser, Event
from django.contrib.auth.models import User


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]


class TogatherUserViewSerializer(serializers.HyperlinkedModelSerializer):
    user = UserViewSerializer()

    class Meta:
        model = TogatherUser
        fields = ["user", "phone_number", "friends"]


class TogatherUserAddSerializer(serializers.HyperlinkedModelSerializer):
    user = UserAddSerializer()

    class Meta:
        model = TogatherUser
        fields = ["user", "phone_number", "friends"]
        depth = 1
