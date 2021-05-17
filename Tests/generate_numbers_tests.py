# To run these test right click on the code and choose run (assume using Pycharm)
import unittest

from Services.GenerateData import DataGenerator


class TestCreateMethod(unittest.TestCase):
    def test_both_zero(self):
        self.assertEqual(DataGenerator.create(0, 0), [])

    def test_both_same(self):
        self.assertEqual(DataGenerator.create(10, 10), [])

    def test_should_return_results(self):
        self.assertEqual(DataGenerator.create(0, 3), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
