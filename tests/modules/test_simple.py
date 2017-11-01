""" Test the simple module. """
import imp
import os
import unittest


class TestSimpleModule(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        simple_file = os.path.join(
            base_dir, 'salt-files', 'base', '_modules', 'simple.py')
        self.simple_py = imp.load_source('simple', simple_file)

    def test_foo(self):
        self.assertEqual(self.simple_py.foo(), 'foo')


if __name__ == '__main__':
    pass
