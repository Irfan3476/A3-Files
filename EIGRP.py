#Import required modules/packages/library
import pexpect
#Define Variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'
local_config_file = 'local_config.txt'

#Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address, encoding='utf-8', timeout = 20)

result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

#Check for error, if an error occurs display it and then exit
if result != 0:
    print('--- FAILURE! creating a session for: ', ip_address)
    exit()
#The session is expecting a password, enter details
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
    print('--- FAILURE! entering password: ', password)
    exit()

#Enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

#Check for error, if an error occurs display it and then exit
if result != 0:
    print('--- Failure! entering enable mode')
    exit()

#Send enable password details
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

#Check for error, if an error occurs display it and then exit
if result != 0:
    print('--- Failure! entering enable mode after sending password')
    exit()

#Enter configuration mode
session.sendline('configure terminal')

result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

session.sendline('router eigrp 100')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

session.sendline('network 192.168.1.0')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

session.sendline('network 10.0.0.0')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

session.sendline('network 20.0.0.0')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

session.sendline('no auto-summary')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

session.sendline('end')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

session.sendline('copy running-config startup-config')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
    print('--- Failure! configuring EIGRP')

