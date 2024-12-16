from django.urls import path
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import HabitViewSet, HabitPublicListAPIView


app_name = MainConfig.name

router = DefaultRouter()
router.register(r"", HabitViewSet, basename="habits")

urlpatterns = [
    path("public/", HabitPublicListAPIView.as_view(), name="public_habits"),
] + router.urls
