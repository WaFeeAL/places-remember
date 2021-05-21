from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from .views import home_page, post_memory

User = get_user_model()


class MemoryModelTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')

    def test_add_memory(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        request.method = 'POST'
        request.POST = {'user': self.user,
                        'location_name': 'Красноярск',
                        'location_address': 'Красноярск',
                        'location_memories': 'Красноярск'}
        response = post_memory(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/home')

    def test_get_memory_list(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        request.method = 'GET'

        response = home_page(request)
        self.assertEqual(response.status_code, 200)
