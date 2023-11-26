# tests/test_database.py
import unittest
from unittest.mock import patch, MagicMock
from src.database import db

class TestDatabase(unittest.TestCase):
    @patch('src.database.os.environ', {'DB_USER_NAME': 'test_user', 'DB_PASSWORD': 'test_password',
                                       'DB_NAME': 'test_db', 'DB_HOST': 'localhost'})
    def test_database_connection(self):
        with patch('src.database.SQLAlchemy') as mock_sqlalchemy:
            db.init_app(MagicMock())
            mock_sqlalchemy.assert_called_once()

    def test_database_url(self):
        with patch('src.database.os.environ', {'DB_USER_NAME': 'test_user', 'DB_PASSWORD': 'test_password',
                                               'DB_NAME': 'test_db', 'DB_HOST': 'localhost'}):
            from src.database import db_url
            self.assertEqual(db_url, "postgresql://test_user:test_password@localhost:5432/test_db")


if __name__ == '__main__':
    unittest.main()
