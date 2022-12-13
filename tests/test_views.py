from django.test import TestCase, Client
from django.urls import reverse
from home.models import User, Patient, Doctor, Appointment


class TestViews(TestCase):
    def test_home(self):
        client = Client()
        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_search(self):
        client = Client()
        response = client.get(reverse('search'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    # def test_login(self):
    #     client = Client()
    #     response = client.get(reverse('patient_login'))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'login.html')
