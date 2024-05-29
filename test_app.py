# it's testing,

import unittest
from app import app

class GoGameApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_case_1(self):
        response = self.app.get('/0/0/0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"max_draws": 0})

    def test_case_2(self):
        response = self.app.get('/1/1/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"max_draws": 2})

    def test_case_3(self):
        response = self.app.get('/3/4/5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"max_draws": 6})

    def test_case_4(self):
        response = self.app.get('/3/3/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"max_draws": -1})

if __name__ == '__main__':
    unittest.main()

