from django.test import TestCase

# Create your tests here.

class URLTests(TestCase):
    # Tests the Destination Page
    def test_TestDestinationListView(self):
        response = self.client.get('/destination/')
        self.assertEqual(response.status_code, 200)

    def test_TestDestinationDetailView(self):
        response = self.client.get('/destination/2/')
        self.assertEqual(response.status_code, 200)
