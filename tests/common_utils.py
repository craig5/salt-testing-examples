"""
Common utilities for testing.
"""
# core python packages
import imp
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
        #
        self.tests_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = os.path.dirname(self.tests_dir)
        self.modules_dir = os.path.join(
            self.base_dir, 'salt-files', 'base', '_modules')
        self.logger.debug('Modules dir: {}'.format(self.modules_dir))

    def load_module(self, file_name):
        """
        Load the salt module given ('.../salt-files/base/_modules/')
        """
        full_path = os.path.join(self.modules_dir, file_name)
        module = imp.load_source(file_name, full_path)
        return module


if __name__ == '__main__':
    pass
