from rest_framework import serializers
from main.validators import (
    validate_reward_and_habit,
    validate_related_habit,
    validate_enjoy_habit,
)

from main.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для Habit."""

    class Meta:
        model = Habit
        fields = (
            "id",
            "name",
            "owner",
            "place",
            "start_time",
            "is_enjoy",
            "period",
            "reward",
            "duration",
            "is_public",
            "related_habit",
            "send_time",
        )
        validators = [
            validate_reward_and_habit,
            validate_related_habit,
            validate_enjoy_habit,
        ]


class HabitDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для RETRIVE Habit."""

    class Meta:
        model = Habit
        fields = "__all__"
