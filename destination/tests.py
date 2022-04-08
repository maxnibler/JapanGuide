from django.test import TestCase
from django.urls import reverse

from .models import Destination
# Create your tests here.

class URLTests(TestCase):
    # Tests the Destination Page
    @classmethod
    def setUpTestData(cls):
        cls.item = Destination.objects.create(
            name='Testing',
            description='Testing',
            region=('KY', 'Kyushu'),
        )
        cls.route = '/destination/'

    # Destination List tests
    def test_dest_list_byname(self):
        response = self.client.get(reverse('destination-list'))
        self.assertEqual(response.status_code, 200)
        
    def test_dest_list_page(self):
        response = self.client.get(self.route)
        self.assertEqual(response.status_code, 200)
        
    def test_dest_list_template(self):
        response = self.client.get(self.route)
        self.assertTemplateUsed(response, 'destination/destination_list.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'navbar.html')

    def  test_dest_list_contains_correct_1(self):
        response = self.client.get(self.route)
        self.assertContains(response, '<h1 class="title">Destination List</h1>')
        self.assertContains(response, '<div class="columns">')
        self.assertContains(response, '<div class="column">')

    # Destination Detail tests
    def test_dest_det_byname(self):
        url = reverse('destination-detail', args=[self.item.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_dest_det_page(self):
        url = self.route+str(self.item.pk)+'/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_dest_det_template(self):
        url = self.route+str(self.item.pk)+'/'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'destination/destination_detail.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'navbar.html')

    def  test_dest_det_contains_correct_1(self):
        url = self.route+str(self.item.pk)+'/'
        response = self.client.get(url)
        self.assertContains(response, '<h1 class="title">Testing</h1>')
        self.assertContains(response, '<div class="columns">')
        self.assertContains(response, '<div class="column">')

