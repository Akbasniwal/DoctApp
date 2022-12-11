from django.test import TestCase, Client
from django.urls import reverse
from home.models import User, Patient, Doctor, Appointment


class TestViews(TestCase):
    def test_user_list(self):
        client = Client()
        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
