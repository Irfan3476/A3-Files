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

# Creating a loopack address
session.sendline('interface loopback 0')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

# Assigning an ip address to the interface of loopback 0
session.sendline('ip add 192.168.1.100.1 255.255.255.0')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

# Exiting the interface of loopack 0
session.sendline('exit')

# Entering into the interface of GigabitEthernet2
session.sendline('interface g2')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

# Assigning an ip address to the interface
session.sendline('ip add 192.168.61.103 255.255.255.0')
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

# Exiting the GigabitEthernet 2 interface
session.sendline('exit')

# Exiting configuration mode
session.sendline('exit')

#Display a sucess message if it works
print('------------------------------------------')
print('')
print('--- Success! connecting to: ', ip_address)
print('---               Username: ', username) 
print('---               Password: ', password)
print('') 
print('------------------------------------------')
print('Configured looback address')
print('Changed ip address of Gigabit Ethernet 2')



#Terminate the SSH session
session.close()