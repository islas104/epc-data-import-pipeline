import unittest
from app import app

class SoldPriceMapTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_data_api(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)
    
    def test_plot_page(self):
        response = self.app.get('/plot')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<img', response.data)

if __name__ == '__main__':
    unittest.main()
