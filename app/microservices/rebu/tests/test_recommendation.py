from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, meal
from urllib.parse import urlencode
from django.core.management import call_command

class test_recommendation(TestCase):
    def setUp(self):
        call_command('loaddata', 'rebu/fixtures/rebu/rebu_testdata.json', verbosity = 0)

    def test_verify_recommendation_exists(self):
        response = self.client.get(reverse('recommendation', args = [1]))
        self.assertEqual(response.status_code, 200)

    def test_existing_recommendation(self):
        response = self.client.get(reverse('recommendation', args = [2]))
        self.assertContains(response, 'true')
        self.assertContains(response, '1')

    def test_recommendation_meal(self):
        data = {
                "meal": 1,
                "recommended_meals": "2,3"
               }

        response_post = self.client.post('/api/v1/recommendations/create/', data)
        response = self.client.get('/api/v1/recommendations/4/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        #self.assertEqual(response.content, 'Cheeseburger')
        self.assertContains(response, '2,3')
        # currently failing don't know why, testing with assertEqual response.content

    def test_update_recommendation(self):
        data = {"recommended_meals": "2,3"}
        response_post = self.client.post('/api/v1/recommendations/1/', data)
        response = self.client.get('/api/v1/recommendations/1/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')
        self.assertContains(response, '2,3')

    def test_delete_recommendation(self):
        response = self.client.delete('/api/v1/recommendations/3/')
        self.assertContains(response, 'true')
        response_false = self.client.get('/api/v1/recommendations/3/')
        self.assertContains(response_false, 'false')

    def tearDown(self):
        pass