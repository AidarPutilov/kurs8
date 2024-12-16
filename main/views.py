from rest_framework import viewsets
from rest_framework import generics

from main.models import Habit
from main.serializers import HabitSerializer, HabitDetailSerializer
from main.paginations import CustomPagination
from users.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet модели Habit."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        """Возвращает объекты пользователя."""
        return Habit.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от запроса."""
        if self.action == "retrieve":
            return HabitDetailSerializer
        return HabitSerializer

    def perform_create(self, serializer):
        """Назначение владельца."""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """Назначение разрешений."""
        if self.action in ("destroy", "update"):
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class HabitPublicListAPIView(generics.ListAPIView):
    """APIView LIST для публичных записей Habit."""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
