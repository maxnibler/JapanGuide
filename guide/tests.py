from django.test import TestCase
from django.urls import reverse

from .models import Guide
# Create your tests here.

class URLTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.item = Guide.objects.create(
            name='Testing',
            description='Test Description',
            contents='Test Contents',
            tags={"tags":["tag1","tag2"]},
        )
        cls.route = '/guide/'
        return super().setUpTestData()

    # Guide List Tests
    def test_guide_list_byname(self):
        response = self.client.get(reverse('guide-list'))
        self.assertEqual(response.status_code, 200)
        
    def test_guide_list_page(self):
        response = self.client.get(self.route)
        self.assertEqual(response.status_code, 200)

    # Guide Detail Tests
    def test_guide_det_byname(self):
        url = reverse('guide-detail', args=[self.item.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_guide_det_page(self):
        url = self.route+str(self.item.pk)+'/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_guide_det_template(self):
        url = self.route+str(self.item.pk)+'/'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'guide/guide_detail.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'navbar.html')

    def  test_guide_det_contains_correct_1(self):
        url = self.route+str(self.item.pk)+'/'
        response = self.client.get(url)
        self.assertContains(response, '<h1 class="title">Testing</h1>')
        self.assertContains(response, '<p>Test Description</p>')
        self.assertContains(response, '<p>Test Contents</p>')




