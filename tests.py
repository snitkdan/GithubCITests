import unittest

class DummyTest(unittest.TestCase):

    def dummy_test(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
