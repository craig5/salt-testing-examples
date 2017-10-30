"""
Common utilities for testing.
"""
# core python packages
import logging
import os
# third party packages
import unittest
# custom packages


class BaseTestClass(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(BaseTestClass, self).__init__(*args, **kwargs)
        logger_name = self.__class__.__name__
        self.logger = logging.getLogger(logger_name)
        self.test_dir = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    pass
