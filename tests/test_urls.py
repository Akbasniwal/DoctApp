from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, search, login


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('list')
        print(resolve(url))
