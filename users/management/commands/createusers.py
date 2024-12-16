from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание пользователей."""

    def handle(self, *args, **kwargs):

        # Список пользователей ('эл.адрес', 'название', 'пароль')
        users_list = [
            ("igor@sky.pro", "Igor", "123"),
            ("ivan@sky.pro", "Ivan", "123"),
            ("irina@sky.pro", "Irina", "123"),
        ]

        # Создание пользователей
        for user_item in users_list:

            # Проверка наличия пользователя, иначе создание
            if not User.objects.filter(email=user_item[0]).exists():
                user = User.objects.create(email=user_item[0], name=user_item[1])
            else:
                user = User.objects.get(email=user_item[0])

            # Установка параметров
            user.set_password(user_item[2])
            user.is_active = True

            # Особые параметры для администратора
            if user_item[0] == "admin@sky.pro":
                user.is_staff = True
                user.is_superuser = True

            user.save()
