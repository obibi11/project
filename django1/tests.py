from django.test import TestCase
from django.urls import reverse
import json

class APITestCase(TestCase):
    def test_get_user(self):
        response = self.client.get(reverse('user_view', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_post_data(self):
        data = json.dumps({'name': 'Боб', 'age': 30})
        response = self.client.post('/api/post/', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
