from django.test import TestCase, Client
from django.urls import reverse
from rebu.models import user, eater, cook, meal, plate, eater_rating, review

class test_user(TestCase):
    def setUp(self):
        pass

    def test_create_user(self):
        response = self.client.get("/api/v1/users/1/")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass

class test_meal(TestCase):
    def setUp(self):
        pass

    def test_descriptive_testname(self):
        self.assertTrue(True)

    def tearDown(self):
        pass
