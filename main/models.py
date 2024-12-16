from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from config.settings import AUTH_USER_MODEL


class Habit(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="название привычки",
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="автор",
        null=True,
        blank=True,
    )
    place = models.CharField(
        max_length=50,
        verbose_name="место выполнения",
    )
    start_time = models.TimeField(
        auto_now=False, verbose_name="время начала выполнения"
    )
    is_enjoy = models.BooleanField(
        default=False,
        verbose_name="приятная привычка",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="связанная привычка",
        related_name="habits",
        null=True,
        blank=True,
    )
    period = models.PositiveSmallIntegerField(
        verbose_name="периодичность (дни)",
        default=1,
        # Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
        validators=[MaxValueValidator(7), MinValueValidator(1)],
    )
    reward = models.CharField(
        max_length=50,
        verbose_name="вознаграждение",
        null=True,
        blank=True,
    )
    duration = models.PositiveSmallIntegerField(
        verbose_name="время выполнения (с)",
        default=120,
        # Время выполнения должно быть не больше 120 секунд.
        validators=[MaxValueValidator(120)],
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="публичная привычка",
    )
    send_time = models.DateTimeField(
        auto_now=False,
        verbose_name="время следующей отправки сообщения в Телеграм",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
        ordering = ("name",)

    def __str__(self):
        return self.name
