"""
An example module with more stuff.
"""
# core python packages
# third party packages
# custom packages


class SaltWrapper(object):

    def __init__(self):
        self.salt = __salt__


def cmd_run():
    salt_wrapper = SaltWrapper()
    output = salt_wrapper.salt['cmd.run']('echo "foo..."')
    return output


if __name__ == '__main__':
    __salt__ = dict()
