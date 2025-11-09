#249
#print(240, 144, 248&182, 0)
#FCDA

#250
'''print("net:", end = '  ')
print(bin(111)[2:].zfill(8), bin(81)[2:].zfill(8), bin(192)[2:].zfill(8), \
      bin(0)[2:].zfill(8), sep = '.')
print("node:", end = ' ')
print( bin(111)[2:].zfill(8), bin(81)[2:].zfill(8), bin(200)[2:].zfill(8), \
      bin(27)[2:].zfill(8), sep = '.')
print(int("11110000", 2))'''
#240

#251
'''print("net_:", end = ' ')
print(bin(154)[2:].zfill(8), bin(201)[2:].zfill(8), bin(192)[2:].zfill(8), \
      bin(0)[2:].zfill(8), sep = '.')
print("node:", end = ' ')
print( bin(154)[2:].zfill(8), bin(201)[2:].zfill(8), bin(208)[2:].zfill(8), \
      bin(17)[2:].zfill(8), sep = '.')
print(int("11100000", 2))
#224'''


#252
'''print(135, 12, 170 & 248, 0)
#EBGA'''

#256
'''print("net_:", end = ' ')
print(bin(111)[2:].zfill(8), bin(81)[2:].zfill(8), bin(192)[2:].zfill(8), \
      bin(0)[2:].zfill(8), sep = '.')
print("node:", end = ' ')
print( bin(111)[2:].zfill(8), bin(81)[2:].zfill(8), bin(208)[2:].zfill(8), \
      bin(27)[2:].zfill(8), sep = '.')
print(int("11000000", 2))
#192'''

#260
'''print("node1:", end = ' ')
print(bin(211)[2:].zfill(8), bin(115)[2:].zfill(8), bin(61)[2:].zfill(8), \
      bin(154)[2:].zfill(8), sep = '.')
print("node2:", end = ' ')
print( bin(211)[2:].zfill(8), bin(115)[2:].zfill(8), bin(59)[2:].zfill(8), \
      bin(137)[2:].zfill(8), sep = '.')
print(int("11111000", 2))
#248'''

#262
'''print("node1:", end = ' ')
print(bin(121)[2:].zfill(8), bin(171)[2:].zfill(8), bin(15)[2:].zfill(8), \
      bin(70)[2:].zfill(8), sep = '.')
print("node2:", end = ' ')
print( bin(121)[2:].zfill(8), bin(171)[2:].zfill(8), bin(3)[2:].zfill(8), \
      bin(68)[2:].zfill(8), sep = '.')
print(int("11110000", 2))
#240'''

#6839
'''net = '.'.join([bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(32)[2:].zfill(8), \
      bin(160)[2:].zfill(8)])
mask = '.'.join([bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), \
      bin(240)[2:].zfill(8)])
print(net.count('1'))
print(net)
print(mask)
c=0
for i in range (2**4):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        c+=1
print(c)
#8'''

#6840
'''net = '.'.join([bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(248)[2:].zfill(8), \
      bin(176)[2:].zfill(8)])
mask = '.'.join([bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), \
      bin(240)[2:].zfill(8)])
print(net)
print(mask)
print(net.count('1'))
print(net.count('0') - 4)
c=0
for i in range (2**4):
    s = bin(i)[2:].zfill(4)
    if s.count('1') + 2 == s.count('0'):
        c+=1
print(c)
#4'''

#6942
'''for n in range (4,15):
    m = 2 + 3 * n + 1 * n**2
    if m < 70:
        print(int("132", n))
#56'''

#6844
'''net = '.'.join([bin(202)[2:].zfill(8), bin(75)[2:].zfill(8), bin(38)[2:].zfill(8), \
      bin(176)[2:].zfill(8)])
mask = '.'.join([bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), \
      bin(240)[2:].zfill(8)])
print(net)
print(mask)
c=0
for i in range (2**4):
    s = "11" + bin(i)[2:].zfill(4)
    if not "111" in s and not "000" in s:
        c+=1
print(c)
#5'''

