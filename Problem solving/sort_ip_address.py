import socket

list_of_ips=['1.2.3.4', '4.2.3.3', '1.2.3.5', '1.2.3.2', '1.2.3.1']

# list_of_ips = ['192.168.204.111', '192.168.99.11', '192.168.102.105']
# print sorted(list_of_ips, key=lambda ip: long(''.join(["%02X" % long(i) for i in ip.split('.')]), 16))

# Basically sorted fuction need two things - a list to be sorted and a key.
a =  sorted([x.split('.') for x in list_of_ips], key=lambda item:item)
print ['.'.join(z) for z in a]