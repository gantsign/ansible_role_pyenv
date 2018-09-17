import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pyenv_install(host):
    pyenv = host.file('/home/test_usr1/.pyenv')
    assert pyenv.exists
    assert pyenv.is_directory
    assert pyenv.user == 'test_usr1'
    assert pyenv.group in ['test_usr1', 'users']


def test_version_bash(host):
    version = host.check_output('sudo --set-home --user test_usr1 ' +
                                'bash --login -i -c "pyenv --version"')
    pattern = r'pyenv [0-9\.]+'
    assert re.search(pattern, version)
