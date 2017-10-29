import unittest

class MyTest(unittest.TestCase):                 

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    def test_case1(self):
        # do something
        self.assertEqual(1, 1)            

if __name__ == '__main__':
    unittest.main() 