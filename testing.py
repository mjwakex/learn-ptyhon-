import sys
import unittest
import random

class MyTest(unittest.TestCase):
    def test_one(self):
        #test code
        pass

    def test_two(self):
        #test code
        pass

def suite():
    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromTestCase(MyTest)
    return testsuite

def test():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testsuite)
    return result