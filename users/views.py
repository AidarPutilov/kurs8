from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer
from users.models import User


class UserCreateAPIView(generics.CreateAPIView):
    """API CREATE для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """API GET для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """API RETRIVE для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """API PATCH для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    """API DELETE для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
