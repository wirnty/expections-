import unittest
from exceptions import ExceptionErr

class TestExceptions(unittest.TestCase):
    def test_custom_error(self):
        with self.assertRaises(exceptions.ExceptionErr):
            raise exceptions.ExceptionErr("Something went wrong")

if __name__ == "__main__":
    unittest.main()
