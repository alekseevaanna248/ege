#19
'''
from functools import *
@cache
def ff(a):
    hod = [a + 1, a + 4, a * 2]
    if any([el >= 58 for el in hod]): return 'p1'
    if all([ff(el) == 'p1' for el in hod]): return 'v1'
    if any([ff(el) == 'v1' for el in hod]): return 'p2'
    if all([ff(el) == 'p2' or ff(el) == 'p1' for el in hod]): return 'v2'

for s in range(1, 58):
    print(s, ff(s))
'''


#23
'''
def ff(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return ff(a + 1, b) + ff(a + 2, b) + ff(a + 3, b)
print(ff(5, 7) * ff(7, 11))
'''


#25
'''
def ff(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return n // d + d
    return 0

c = 0
for n in range(700000 + 1, 10**9):
    m = ff(n)
    if m % 10 == 4:
        c += 1
        print(n, m)
    if c >= 5:
        break
        '''

#24
'''
from re import *
with open("24_17563.txt") as f:
    s = f.readline()
print(s[:7])
r = '([1-9]\d*)([-*]([1-9]\d*))*'
A = finditer(r, s)
m = 0
for x in A:
    l = x.span()[0]
    r = x.span()[1]
    if m < r - l:
        print(r - l, s[l:r])
        input()
        m = r - l
print(m)
'''


#26
with open ("26_17565.txt") as f:
    N, S = list(map(int, f.readline().split()))
    D = {}
    for x in f.readlines():
        id, n1, n2, n3, sob = list(map(int, x.split()))
        su = n1 + n2 + n3
        if su not in D:
            D[su] = [[sob, id]]
        else:
            D[su].append([sob, id])
for x in D:
    D[x] = sorted(D[x], key = lambda y: (-y[0], y[1]))
A = sorted(D.items(), reverse = True)
print(A[:5])

rest = S
for y in A:
    if len(y[1]) <= rest:
        rest -= len(y[1])
        id = y[1][-1][1]
    else:
        c = len(y[1])
        break
print(rest)
print(id, c)
        
        





