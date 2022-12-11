from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, search, plogin, dlogin


class TestUrls(SimpleTestCase):
    def test_home_url_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_search_url_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)

    def test_login_url_resolved(self):
        url = reverse('plogin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, plogin)
