from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            id=1,
            email='test@test.test',
            passwrod='test'
        )
        self.user.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            id=1,
            place="work",
            time="13:00:00",
            action="smoking",
            pleasant_habit=True,
            binding_habit=None,
            period=1,
            reward="сон",
            execution_time="00:01:00",
            is_publish=True,
            owner=self.user
        )

    def test_destroy_habit(self):
        """
        Тестирование удаление привычки
        """
        response = self.client.delete(
            '/habit/1/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_habit(self):
        """
        Создание привычки
        """
        response = self.client.post(
            '/habit/',
            place="home",
            time="19:00:00",
            action="sleep",
            pleasant_habit=True,
            binding_habit=None,
            period=2,
            reward="сон",
            execution_time="00:00:30",
            is_publish=True,
            owner=self.user
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.data['is_publish'],
            True
        )

    def test_update_habit(self):
        response = self.client.put(
            '/habit/1/',
            {'is_publish': False}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_habit(self):
        response = self.client.get(
            '/habit/'
        )

        self.assertEquals(
            response.json(),
            {
                'place': "work",
                'time': "13:00:00",
                'action': "smoking",
                'pleasant_habit': True,
                'binding_habit': None,
                'period': 1,
                'reward': "сон",
                'execution_time': "00:01:00",
                'is_publish': True,
            }
        )
