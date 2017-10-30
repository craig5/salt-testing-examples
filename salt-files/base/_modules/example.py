"""
An example module.
"""
# core python packages
# third party packages
# custom packages


def foo():
    output = __salt__['cmd.run']('echo "foo..."')
    return output


if __name__ == '__main__':
    __salt__ = dict()
    pass
