# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. 
# The numbers cannot be 0 prefixed unless they are 0.

def valid_ip_num(st):
    if len(st)>=0 and len(st)<=3:
        if len(st) == 3:
            if int(st) > 255:
                return False

        if len(st) > 1 and st[0] == '0':
            return False
    else:
        return False

    return True

def validIPAddresses(st):
    # Write your code here.
    i=0
    valid_ips = []
    while (i<3):
        first = st[0:i+1] if valid_ip_num(st[0:i+1]) else False
        if first:
            j=0
            while(j<3):
                second = st[i+1:i+2+j] if valid_ip_num(st[i+1:i+2+j]) else False
                if second:
                    k=0
                    while(k<3):
                        third = st[i+j+2: i+j+k+3] if valid_ip_num(st[i+j+2: i+j+k+3]) else False
                        if third:
                            fourth = st[i+j+k+3: len(st)+1] if valid_ip_num(st[i+j+k+3: len(st)+1]) else False
                            if fourth:
                                ip=first+'.'+second+'.'+third+'.'+fourth
                                valid_ips.append(ip)
                        k=k+1
                j=j+1

        i=i+1

    return valid_ips

print(validIPAddresses('192168211346'))
