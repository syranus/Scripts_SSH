#!/usr/bin/env python3.8
import paramiko
from paramiko import SSHClient

host = "192.168.19.136"
user = "admin"
password = "L0gistik"

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(host, username=user, password=password)
stdout= client.exec_command('python3 /usr/local/libexec/nagios/check_pfusers.py')[1]
for line in stdout:
    print(line)

client.close()