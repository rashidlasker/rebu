from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, meal
from urllib.parse import urlencode
from django.core.management import call_command
import json

class test_user(TestCase):
    def setUp(self):
        call_command('loaddata', 'rebu/fixtures/rebu/rebu_testdata.json', verbosity = 0)

    def test_verify_user_exists(self):
        response = self.client.get(reverse('user', args = [1]))
        self.assertEqual(response.status_code, 200)

    def test_existing_user(self):
        response = self.client.get(reverse('user', args = [2]))
        self.assertContains(response, 'true')
        self.assertContains(response, 'Rashid')

    def test_new_user(self):
        data = {
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
              }
        
        response_post = self.client.post('/api/v1/users/create/', data)
        response = self.client.get('/api/v1/users/4/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        self.assertContains(response, 'John')

    def test_delete_user(self):
        response = self.client.delete('/api/v1/users/3/')
        self.assertContains(response, 'true')
        response_false = self.client.get('/api/v1/users/3/')
        self.assertContains(response_false, 'false')

    def tearDown(self):
        pass

class test_meal(TestCase):
    def setUp(self):
        call_command('loaddata', 'rebu/fixtures/rebu/rebu_testdata.json', verbosity = 0)

    def test_verify_meal_exists(self):
        response = self.client.get("/api/v1/meals/1/")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
