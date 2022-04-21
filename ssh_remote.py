"""
@author: Ganesh Shankar Jadhawar
@goals: To develop python code which will run linux commands on remote hosts
This code is to login single remote host and run command on it.
"""

import paramiko

hostname = input("Enter the remote machine hostname or IP:")
username = input("Enter the username to login on remote host:")
password = input("Enter the password of above user:")
"""
# hostname = "127.0.0.1"
#username = "jadhgan"
#password = "Webmaster098765"
"""
commands = ["ls -lrt"]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

