from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, meal
from urllib.parse import urlencode
from django.core.management import call_command

#need to edit this, is just framework for testing new authenticator calls

class test_meal(TestCase):
    def setUp(self):
        call_command('loaddata', 'rebu/fixtures/rebu/rebu_testdata.json', verbosity = 0)

    def test_verify_user_exists(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        pass