#23
'''
A = [0] * 300
A[105] = 1
for i in range(104, 21, -1):
    if i == 51 or i == 42:
        A[i] = 0
    else:
        A[i] = A[i + 1] + A[i + 5] + A[i * 2 - 1] + A[i * 2]
B = [0] * 300
B[22] = 1
for i in range(21, 7, -1):
    B[i] = B[i + 1] + B[i + 5] + B[i * 2 - 1] + B[i * 2]
print(B[:22])
print(A[22]*B[8])
#65921705960
'''

#8
'''
def p6(n):
    s = ""
    while n > 0:
        e = n % 6
        n //= 6
        s = str(e) + s
    return s.zfill(7)
from itertools import *
arr = list(product("234", repeat = 3))
print(len(list(arr)))
# А - 0 И - 1 Н - 2 С - 3 Ф - 4 Ы - 5

c = 0
for n in range(6 ** 7):
    s = p6(n)
    #print(s)
    #input()
    if any(["".join(x) in s for x in arr]) and (s[-1] == '0' or \
                                      s[-1] == '1' or s[-1] == '5'):
           c += 1
print(c)
'''

#2
print("x y z w")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f = ((x == z) <= (y or not(w))) and (x and y)
                if not f:
                    print(x, y, z, w)
