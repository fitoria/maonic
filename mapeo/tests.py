from django.test.client import Client
from django.test import TestCase

class MapeoViewsTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_obtener_lista(self):
        response = self.client.get('/mapeo/lista/familia/')
        self.assertEqual(response.status_code, 200)
        print response

    def test_obtener_lista_valid_view(self):
        pass
