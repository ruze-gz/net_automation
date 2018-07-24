import paramiko
import time
import getpass

username = raw_input('Username: ')
password = getpass.getpass('Password: ')

for i in range (11,16):
    ip = "192.168.2." + str(i)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)
    print "Successfully connected: ", ip
    command = ssh_client.invoke_shell()
    command.send("configure termianl\n")
    for n in range (10,21):
        print "Creating VLAN " + str(n)
        command.send("vlan " + str(n) + "\n")
        time.sleep(0.5)

    command.send("end\n")
    command.send("wr mem\n")
    time.sleep(2)
    output = command.recv(65535)
    print output
    
ssh_client.close





    