from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, meal
from urllib.parse import urlencode
from django.core.management import call_command

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
                "gender": "Male",
                "password": "password",
                "username": "js4be"
               }

        response_post = self.client.post('/api/v1/users/create/', data)
        response = self.client.get('/api/v1/users/4/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        self.assertContains(response, 'John')

    def test_update_user(self):
        data = {"first_name": "Jacob"}
        response_post = self.client.post('/api/v1/users/1/', data)
        response = self.client.get('/api/v1/users/1/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        self.assertContains(response, 'Jacob')

    def test_delete_user(self):
        response = self.client.delete('/api/v1/users/3/')
        self.assertContains(response, 'true')
        response_false = self.client.get('/api/v1/users/3/')
        self.assertContains(response_false, 'false')

    def tearDown(self):
        pass