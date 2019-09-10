import sys
filename = "C:\Users\gaurav\\trunk\src\inSyncQA\TestCases\\api\\regression\cloudapp\\abc.txt"


contacts = []
with open(filename) as file:
    header = file.readline().strip().split('\t')
    for line in file:
        line = line.strip().split('\t')
        contact_map = zip(header, line)
        contacts.append(dict(contact_map))

print contacts

for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))


#sample txt file contant
# first	last	email
# gk	mi	gk@mi.com

