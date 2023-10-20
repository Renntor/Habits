from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            id=1,
            email='test@test.test',
            passwrod='test',
            is_superuser=True
        )
        self.user.force_authenticate(user=self.user)

    def test_destroy_user(self):
        """
        Тестирование удаление пользователя
        """
        response = self.client.delete(
            '/user/1/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_user(self):
        """
        Тестирование создания пользователя
        """
        response = self.client.post(
            '/user/create/',
            id=2,
            email='email@email.email',
            password='test'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.data['email'],
            'email@email.email'
        )

    def test_update_user(self):
        """
        Тестирование обновление пользователя
        """
        response = self.client.put(
            '/user/update/1/',
            {'phone': '11122333'}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEquals(
            response.data['phone'],
            '11122333'
        )

    def test_get_user(self):
        response = self.client.get(
            '/user/'
        )

        self.assertEquals(
            response.json(),
            {
                'email': 'test@test.test',
                'phone': None,
                'first_name': None,
                'last_name': None
            }
        )
