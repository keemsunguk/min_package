import unittest
from minpkg.utils import Demo


class TestStringMethods(unittest.TestCase):
    """
    Demo unit test example
    """
    def setUp(self) -> None:
        """
        Set up expected
        :return: None
        """
        self.test_msg = "Hello min_package"

    def test_demo(self) -> None:
        """
        Testing demo
        :return: None
        """
        demo = Demo("Hello min_package")
        demo.show_message()
        self.assertEqual(self.test_msg, demo.message)
