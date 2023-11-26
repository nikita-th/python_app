import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import app, db

class TestUserEndpoints(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_list(self):
        response = self.app.get('/user/list')
        self.assertEqual(response.status_code, 200)

    def test_user_add(self):
        data = {
            'designation': 'Test Designation',
            'email': 'test@example.com',
            'first_name': 'Test',
            'is_admin': False,
            'last_name': 'User',
            'middle_name': 'Middle',
            'oidc_id': 'test_oidc_id',
            'phone_number': '1234567890',
            'previous_exp': 'Test Experience'
        }
        response = self.app.post('/user/add', json=data)
        self.assertEqual(response.status_code, 200)

    def test_user_update(self):
        # Assuming there is at least one user in the database
        user_id = 1
        data = {
            'designation': 'Updated Designation',
            'email': 'updated@example.com',
            'first_name': 'Updated',
            'is_admin': True,
            'last_name': 'User',
            'middle_name': 'Middle',
            'oidc_id': 'updated_oidc_id',
            'phone_number': '9876543210',
            'previous_exp': 'Updated Experience'
        }
        response = self.app.put(f'/user/update/{user_id}', json=data)
        self.assertEqual(response.status_code, 200)

    def test_user_detail(self):
        # Assuming there is at least one user in the database
        user_id = 1
        response = self.app.get(f'/user/detail/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_user_delete(self):
        # Assuming there is at least one user in the database
        user_id = 1
        response = self.app.delete(f'/user/delete/{user_id}')
        self.assertEqual(response.status_code, 200)

class TestHealthCheckEndpoint(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'up')

