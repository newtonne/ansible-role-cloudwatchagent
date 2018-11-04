import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name, mode", [
    ('/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json', 0o644),  # noqa: E501
    ('/etc/logrotate.d/cloudwatch-agent', 0o644),
])
def test_config(host, name, mode):
    file = host.file(name)
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == mode


def test_cwa_installed(host):
    pkg = host.package('amazon-cloudwatch-agent')
    assert pkg.is_installed


def test_cwa_running(host):
    service = host.service('amazon-cloudwatch-agent')
    assert service.is_running
    assert service.is_enabled
