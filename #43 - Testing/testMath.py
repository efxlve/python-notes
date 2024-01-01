import unittest
from Math import Math


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.math = Math()

    def test_add(self):
        result = self.math.sumTwoNumbers(10, 20)
        self.assertEqual(30, result)

    def test_multiply(self):
        result = self.math.mulTwoNumbers(10, 20)
        self.assertEqual(200, result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
