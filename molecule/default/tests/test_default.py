import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_env_vars_added(host):
    f = host.file('/etc/pgbouncer/pgbouncer.ini')

    assert f.exists
