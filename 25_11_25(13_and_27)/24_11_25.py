#23856
'''print(bin(116)[2:].zfill(8))
print(bin(172)[2:].zfill(8))
print(bin(95)[2:].zfill(8))
#11
print(172+95+64+int("1111",2))
#346'''


#23854
'''print(bin(252)[2:].zfill(8))
print(bin(106)[2:].zfill(8))
print("451721041")'''


#23751
'''print(int("10"+'1'*6, 2))
print("191191255254")'''

#23197
'''from ipaddress import *
net = ip_network("45.172.106.203/22",0)
print(net)
print(bin(104)[2:].zfill(8))
print("45172107254")'''


#21978
'''print(bin(248)[2:].zfill(8))
print(bin(71)[2:].zfill(8))
print(bin(98)[2:].zfill(8))
print(int('1'*5+'0'*3, 2))
print("9871255248")'''


#21744
'''from ipaddress import *
net = ip_network("95.24.2.9/23",0)
c=0
for node in net:
    dv = bin(int(node))[2:].zfill(32)
    if dv.count('0')%2==0:
        c+=1
print(c)'''


#20807
from ipaddress import *
net = ip_network("172.16.192.0/18",0)
c=0
for node in net:
    dv = bin(int(node))[2:].zfill(32)
    if dv.count('1') % 5 != 0:
        c+=1
print(c)
