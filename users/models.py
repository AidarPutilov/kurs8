from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите Email",
    )
    name = models.CharField(
        max_length=20,
        verbose_name="имя пользователя",
        help_text="Введите имя пользователя",
        blank=True,
        null=True,
    )
    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="Telegram ID",
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("name",)

    def __str__(self):
        return self.name
