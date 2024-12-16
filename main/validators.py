from rest_framework.serializers import ValidationError


def validate_reward_and_habit(value):
    """Невозможен выбор приятной привычки и вознаграждения одновременно."""

    reward = value.get("reward")
    related_habit = value.get("related_habit")
    if reward and related_habit:
        raise ValidationError(
            "Невозможен выбор приятной привычки и вознаграждения одновременно"
        )


def validate_related_habit(value):
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""

    related_habit = value.get("related_habit")
    if related_habit and not related_habit.is_enjoy:
        raise ValidationError("Связанная привычка должна быть приятной")


def validate_enjoy_habit(value):
    """У приятной привычки не может быть вознаграждения или связанной привычки."""

    is_enjoy = value.get("is_enjoy")
    reward = value.get("reward")
    related_habit = value.get("related_habit")
    if is_enjoy and (related_habit or reward):
        raise ValidationError(
            "У приятной привычки не может быть вознаграждения или связанной привычки"
        )
