#this is a script for switch IOS upgrade
#Target update include 2960X, 3850X, 9300X

import sys
import paramiko
import time
import getpass
import socket

username = raw_input('Username: ')
password = getpass.getpass('password: ')
ip_file = sys.argv[1]
cmd_file = sys.argv[2]

switch_with_authentication_issue = []
switch_not_reachable = []

iplist = open(ip_file, 'r')
for line in iplist.readlines():
    try:
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip,username=username,password=password)
        

