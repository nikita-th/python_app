import os
import unittest
import json
from flask_testing import TestCase
from src import app, db  # Replace 'your_main_file' with the actual name of your main file

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an in-memory database for testing
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_example_endpoint(self):
        response = self.client.get('/test')
        data = json.loads(response.data.decode('utf-8'))

        # Add your assertions based on the expected behavior of the /test endpoint
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)

    def test_error_endpoint(self):
        response = self.client.get('/error')
        data = json.loads(response.data.decode('utf-8'))

        # Add your assertions based on the expected behavior of the /error endpoint
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)

    # Add more test cases for other endpoints as needed

if __name__ == '__main__':
    unittest.main()
