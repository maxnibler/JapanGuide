from django.test import TestCase
from django.urls import reverse

from .models import Guide
# Create your tests here.

class URLTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.item = Guide.objects.create(
            name='Testing',
        )
        cls.route = '/guide/'
        return super().setUpTestData()

    # Guide List Tests
    def test_dest_list_byname(self):
        response = self.client.get(reverse('guide-list'))
        self.assertEqual(response.status_code, 200)
        
    def test_dest_list_page(self):
        response = self.client.get(self.route)
        self.assertEqual(response.status_code, 200)

    # Guide Detail Tests
    


