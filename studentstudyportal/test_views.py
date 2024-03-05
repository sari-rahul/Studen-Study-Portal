from django.test import TestCase
from django.urls import reverse
from .views import handler404


class TestErrorPages(TestCase):

    def test_error_handler404(self):
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
    

    