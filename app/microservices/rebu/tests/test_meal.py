from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, meal
from urllib.parse import urlencode
from django.core.management import call_command

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
        #self.assertEqual(response.content, 'Cheeseburger')
        self.assertContains(response, 'wild shrimp, herb-shellfish broth, saffron aioli')
        # currently failing don't know why, testing with assertEqual response.content

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