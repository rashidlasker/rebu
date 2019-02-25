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

class test_meal(TestCase):
    def setUp(self):
        call_command('loaddata', 'rebu/fixtures/rebu/rebu_testdata.json', verbosity = 0)

    def test_verify_meal_exists(self):
        response = self.client.get(reverse('meal', args = [1]))
        self.assertEqual(response.status_code, 200)

    def test_existing_meal(self):
        response = self.client.get(reverse('meal', args = [2]))
        self.assertContains(response, 'true')
        self.assertContains(response, 'Steak Chinoise')

    def test_new_meal(self):
        data = {
                "name": "Cheeseburger",
                "calories": 100,
                "description": "wild shrimp, herb-shellfish broth, saffron aioli",
                "spice": 0,
                "price": 2,
                "tags": "healthy yummy food",
                "takeout_available": "False",
                "num_plates": 2,
                "start": "2019-02-04T00:01:00-05:00",
                "end": "2019-02-04T00:04:00-05:00",
                "cook": 1
               }
        
        response_post = self.client.post('/api/v1/meals/create/', data)
        response = self.client.get('/api/v1/meals/4/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        self.assertContains(response, 'Cheeseburger')

    def test_update_meal(self):
        data = {"name": "Hamburger"}
        response_post = self.client.post('/api/v1/meals/1/', data)
        response = self.client.get('/api/v1/meals/1/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        self.assertContains(response, 'Hamburger')

    def test_delete_meal(self):
        response = self.client.delete('/api/v1/meals/3/')
        self.assertContains(response, 'true')
        response_false = self.client.get('/api/v1/meals/3/')
        self.assertContains(response_false, 'false')

    def tearDown(self):
        pass

class test_layer(TestCase):
    def setUp(self):
        call_command('loaddata', 'rebu/fixtures/rebu/rebu_testdata.json', verbosity = 0)

    def test_all(self):
        response = self.client.get(reverse('all'))
        self.assertEqual(response.status_code, 200)

    def test_newest(self):
        response = self.client.get(reverse('newest'))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass

class test_review(TestCase):
    def setUp(self):
        call_command('loaddata', 'rebu/fixtures/rebu/rebu_testdata.json', verbosity = 0)

    def test_verify_review_exists(self):
        response = self.client.get(reverse('review', args = [1]))
        self.assertEqual(response.status_code, 200)

    def test_existing_review(self):
        response = self.client.get(reverse('review', args = [1]))
        self.assertContains(response, 'true')
        self.assertContains(response, 'food')

    def test_new_meal(self):
        data = {
                "rating": 2,
                "description": "good food",
                "eater": 1,
                "cook": 1,
                "meal": 1
               }
        
        response_post = self.client.post('/api/v1/reviews/create/', data)
        response = self.client.get('/api/v1/reviews/2/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        self.assertContains(response, 'good food')

    def test_update_review(self):
        data = {"description": "okay"}
        response_post = self.client.post('/api/v1/reviews/1/', data)
        response = self.client.get('/api/v1/reviews/1/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        self.assertContains(response, 'okay')

    def test_delete_review(self):
        response = self.client.delete('/api/v1/reviews/1/')
        self.assertContains(response, 'true')
        response_false = self.client.get('/api/v1/reviews/1/')
        self.assertContains(response_false, 'false')

    def tearDown(self):
        pass
