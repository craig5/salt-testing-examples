"""
Test the moar module.
"""
# core python packages
# third party packages
import mock
# custom packages
import common_utils


class SaltMock(object):

    def __init__(self):
        self.salt = {
            'cmd.run': self.cmd_run_mock
        }

    @classmethod
    def cmd_run_mock(*args):
        return 'foo...'


class TestMoarModule(common_utils.BaseTestClass):

    def setUp(self):
        self.moar_py = self.load_module('moar.py')

    def test_cmd_run(self):
        """Testing example.cmd_run funtion."""
        with mock.patch.object(self.moar_py, 'SaltWrapper', SaltMock):
            self.assertEqual(self.moar_py.cmd_run(), 'foo...')


if __name__ == '__main__':
    pass
