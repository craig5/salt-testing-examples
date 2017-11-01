"""
An example module with more stuff.
"""
# core python packages
# third party packages
# custom packages


def cmd_run():
    output = __salt__['cmd.run']('echo "foo..."')
    return output


if __name__ == '__main__':
    __salt__ = dict()
