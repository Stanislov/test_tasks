import unittest
from login import login
#target = __import__("login/__init__.py")
#login = target.login


class TestLogin(unittest.TestCase):
    def test_001_str_login(self):
        """
        Test 001: 'login'
        """
        data = 'regrer'
        result = login(data)
        self.assertEqual(result, 1)

    def test_002_list_login(self):
        """
        Test 002: list
        """
        data = [1, 58, 40]
        result = login(data)
        self.assertEqual(result, 0)




if __name__ == '__main__':
    unittest.main()