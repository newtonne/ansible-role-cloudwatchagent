Ansible Role: CloudWatch Agent
==============================

Installs and configures the [AWS Unified CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html).

Requirements
------------

None

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

```
# Debian family
cwa_download_url: https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest
# RedHat family
cwa_download_url: https://s3.amazonaws.com/amazoncloudwatch-agent/redhat/amd64/latest
```
The URL from which to download the CloudWatch Agent package.

```
# Debian family
cwa_pkg_file: amazon-cloudwatch-agent.deb
# RedHat family
cwa_pkg_file: amazon-cloudwatch-agent.rpm
```
The name of the CloudWatch Agent package.

```
# Debian family
cwa_sig_file: amazon-cloudwatch-agent.deb.sig
# RedHat family
cwa_sig_file: amazon-cloudwatch-agent.rpm.sig
```
The name of the CloudWatch Agent GPG sig file.

```
cwa_gpg_url: https://s3.amazonaws.com/amazoncloudwatch-agent/assets
```
The URL from which to download the CloudWatch Agent GPG public key.

```
cwa_gpg_fingerprint: "937616F3450B7D806CBD9725D58167303B789C72"
```
The fingerprint of the CloudWatch Agent GPG public key. See [CloudWatch Agent GPG verification documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/verify-CloudWatch-Agent-Package-Signature.html).

```
cwa_mode: ec2
```
The mode in which to to run the agent. Can be `ec2`, `onPremise` or `auto`.

```
cwa_logfile: /opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log
```
The file into which events will be logged. Ensure it is specified in `cwa_config_map.agent.logfile` if amended from the default.

```
cwa_config_dir: /opt/aws/amazon-cloudwatch-agent/etc
```
The directory into which the agent config file will be placed.

```
cwa_config_map:
  metrics:
    metrics_collected:
      mem:
        measurement:
          - name: mem_used_percent
```
The CloudWatch Agent configuration. This YAML map will be converted to JSON and printed to the amazon-cloudwatch-agent.json file in `cwa_config_dir`. See [CloudWatch agent configuration documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html) for details of all configuration options.

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers

      vars:
        cwa_config_map:
          metrics:
            metrics_collected:
              disk:
                measurement:
                  - name: disk_used_percent
                resources:
                  - /
          logs:
            logs_collected:
              files:
                collect_list:
                  - file_path: /var/log/auth.log
                    log_group_name: auth
                    timestamp_format: "%b %d %H:%M:%S"
            log_stream_name: "{instance_id}"

      roles:
         - { role: newtonne.cloudwatchagent }

License
-------

MIT
