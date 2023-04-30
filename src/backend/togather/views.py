from togather.models import User
from django.shortcuts import get_object_or_404
from togather.serializers import TogatherUserViewSerializer, TogatherUserAddSerializer
from rest_framework import viewsets


class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        "default": None,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])


class UserViewSet(MultiSerializerViewSet):
    queryset = User.objects.all()
    serializer_class = TogatherUserViewSerializer

    serializers = {"default": TogatherUserViewSerializer, "create": TogatherUserAddSerializer}
