from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование модели Habit."""

    def setUp(self):
        """Окружение для тестов."""
        self.user = User.objects.create(email="test@sky.pro")
        self.habit = Habit.objects.create(
            name="Test habit",
            owner=self.user,
            place="Test place",
            start_time="12:00:00",
            is_enjoy=False,
            period=1,
            reward="Test reward",
            duration=60,
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тестирование Habit RETRIVE."""
        url = reverse("main:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.habit.name)

    def test_habit_create(self):
        """Тестирование Habit CREATE."""
        url = reverse("main:habits-list")
        data = {
            "name": "Test habit 2",
            "place": "Test place 2",
            "start_time": "13:00:00",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Тестирование Habit UPDATE"""
        url = reverse("main:habits-detail", args=(self.habit.pk,))
        data = {"name": "Test habit new"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Test habit new")

    def test_habit_delete(self):
        """Тестирование Habit DELETE"""
        url = reverse("main:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Тестирование Habit LIST"""
        url = reverse("main:habits-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "name": self.habit.name,
                    "owner": self.user.pk,
                    "place": self.habit.place,
                    "start_time": self.habit.start_time,
                    "is_enjoy": self.habit.is_enjoy,
                    "period": self.habit.period,
                    "reward": self.habit.reward,
                    "duration": self.habit.duration,
                    "is_public": self.habit.is_public,
                    "related_habit": self.habit.related_habit,
                    "send_time": self.habit.send_time,
                },
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_public_list(self):
        """Тестирование Habit public LIST"""
        url = reverse("main:public_habits")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.habit.pk,
                "name": self.habit.name,
                "owner": self.user.pk,
                "place": self.habit.place,
                "start_time": self.habit.start_time,
                "is_enjoy": self.habit.is_enjoy,
                "period": self.habit.period,
                "reward": self.habit.reward,
                "duration": self.habit.duration,
                "is_public": self.habit.is_public,
                "related_habit": self.habit.related_habit,
                "send_time": self.habit.send_time,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_validate_reward_and_habit(self):
        """Тестирование выбора приятной привычки и вознаграждения одновременно."""
        url = reverse("main:habits-list")
        data = {
            "name": "Test habit 2",
            "place": "Test place 2",
            "start_time": "13:00:00",
            "reward": "Test reward 2",
            "related_habit": "Related_habit 2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_related_habit(self):
        """Тестирование привычки могут попадать только привычки с признаком приятной привычки."""
        url = reverse("main:habits-list")
        data = {
            "name": "Test habit 2",
            "place": "Test place 2",
            "start_time": "13:00:00",
            "reward": "Test reward 2",
            "related_habit": "Related_habit 2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_enjoy_habit(self):
        """Тестирование приятной привычки с вознаграждением."""
        url = reverse("main:habits-list")
        data = {
            "name": "Test habit 2",
            "place": "Test place 2",
            "start_time": "13:00:00",
            "is_enjoy": True,
            "reward": "Test reward 2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
