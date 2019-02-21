from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, meal
from urllib.parse import urlencode
from django.utils.encoding import force_text

class test_user(TestCase):
    def setUp(self):
        data = urlencode({
                "pk": 4,
                "first_name": "John",
                "last_name": "Smith",
                "street": "107N Piedmont Ave",
                "zip_code": "22904",
                "state": "VA",
                "country": "US",
                "bio": "bio",
                "links": "docker.com",
                "language": "English",
                "gender": "Male"
              })
        self.client.post('/api/v1/users/create/', data, content_type="application/x-www-form-urlencoded")

    def test_verify_user_exists(self):
        response = self.client.get(reverse('user', args = [1]))
        self.assertEqual(response.status_code, 200)

    def test_existing_user(self):
        response = self.client.get('/api/v1/users/2/')
        self.assertEqual(response.content, 'true')
        self.assertContains(response, 'Rashid')

    def test_new_user(self):
        response = self.client.get('/api/v1/users/4/')
        self.assertContains(response, 'true')
        self.assertContains(response, 'John')

    def tearDown(self):
        pass

class test_meal(TestCase):
    def setUp(self):
        pass

    def test_verify_meal_exists(self):
        response = self.client.get("/api/v1/meals/1/")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
