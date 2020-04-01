import unittest
import requests

from src.api.config import PYTHON_MODULE_PORT


class ControllerStatusTest(unittest.TestCase):

    def setUp(self):
        self.url = f'http://localhost:{PYTHON_MODULE_PORT}/v1/status'
        self.status_code = 200
        self.response_message = True

    def test_status_code(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, self.status_code)

    def test_response_message(self):
        response = requests.get(self.url).json()
        self.assertEqual(response.get('response').get('ok'), self.response_message)
