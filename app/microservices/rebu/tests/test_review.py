from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, meal
from urllib.parse import urlencode
from django.core.management import call_command

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
