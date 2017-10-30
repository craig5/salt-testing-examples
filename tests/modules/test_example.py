"""
Test the example module.
"""
# core python packages
# third party packages
# custom packages
import common_utils


class TestExampleModule(common_utils.BaseTestClass):

    def setUp(self):
        pass

    def test_foo(self):
        """Testing example.foo function."""
        self.logger.debug('test example.foo')


if __name__ == '__main__':
    pass
