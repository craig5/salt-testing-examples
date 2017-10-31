"""
Test the simple module.
"""
# core python packages
import imp
import os
import unittest
# third party packages
# custom packages


class TestSimpleModule(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        tests_dir = os.path.dirname(this_dir)
        base_dir = os.path.dirname(tests_dir)
        modules_dir = os.path.join(
            base_dir, 'salt-files', 'base', '_modules')
        simple_file = os.path.join(modules_dir, 'simple.py')
        self.simple_py = imp.load_source('simple', simple_file)

    def test_foo(self):
        self.assertEqual(self.simple_py.foo(), 'foo')


if __name__ == '__main__':
    pass
