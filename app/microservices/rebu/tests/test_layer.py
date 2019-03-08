from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, meal
from urllib.parse import urlencode
from django.core.management import call_command

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