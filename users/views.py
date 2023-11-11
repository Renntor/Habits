from rest_framework import generics
from users.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.permissions import IsOwner
from users.serializers import UserSerializers


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializers


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwner]
    serializer_class = UserSerializers

    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        return self.destroy(request, *args, **kwargs)
