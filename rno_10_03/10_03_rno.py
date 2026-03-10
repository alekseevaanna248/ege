#4
'''
print(2 * 2 + 2 + 3 + 3 * 2 + 4 + 4)
'''

#6
'''
from turtle import *

k = 15
up()
tracer(0, 0)
for x in range(-20 * k, 20 * k, k):
    for y in range(-20 * k, 20 * k, k):
        setpos(x, y)
        dot(0.3*k, "blue")
setpos(0, 0)
lt(90)
down()
for _ in range(10):
    fd(10 * k)
    for _ in range(2):
        fd(10 * k)
        rt(90)
update()        
print(9*19)
'''

#9
'''
with open("9_2702.csv") as f:
    A = [list(map(int, x.split(';'))) for x in f.readlines()]
print(A[:10])

def ff(A):
    D = {}
    for x in A:
        if x not in D:
            D[x] = 1
        else:
            D[x] += 1
    B = sorted(D.items(), key = lambda x: -x[1])
    L = sorted(D.values(), reverse = True)
    if L == [3]:
        a = B[0][0]
        if 4 * a < a**2 <= 5 * 4 * a:
            return 0
    elif L == [2, 1]:
        a = B[0][0]
        b = B[-1][0]
        if 2 * (a + b) < a * b <= 5 * 2 * (a + b):
            return b
    return 0

su = 0
for x in A:
    res = ff(x)
    su += res
print(su)
####????????????????????????? квадрат не прямоугольник?!
'''


#16
'''
F = ['*'] * 100
G = ['*'] * 100

F[:3] = [0,0,0]
G[0] = 2

for n in range(1, 100):
    if n > 2 and n % 2 == 1:
        F[n] = F[n - 1] - n
    elif n > 2 and n % 2 == 0:
        F[n] = F[n - 2] + G[n - 1] + 2
    if n % 2 != 0:
        if n == 1:
            G[n] = F[n - 1] - 2 * 2
        elif n >= 2:
            G[n] = F[n - 1] - 2 * G[n - 2]
    elif n % 2 == 0:
        if n == 1:
            G[n] = 2 * 1 - 2 * G[n - 1]
        elif n >= 2:
            G[n] = 2 * F[n - 2] - 2 * G[n - 1]
print(F[96])
print(F[76])
'''


#19
'''
from itertools import *
def check(a, b):
    if a >= 50 or b >= 50:
        if a + b <= 109:
            return True
    return False
def hod(a, b):
    return [(a + 1, b), (a, b + 1), (a + 2, b), (a, b + 2), (a * 2, b), (a, b * 2)]
game = set([x for x in product(range(1, 50), repeat = 2)])
win1 = set(x for x in game if any(check(*el) for el in hod(*x)))
game -= win1
los1 = set(x for x in game if all(el in win1 for el in hod(*x)))
game -= los1
win2 = set(x for x in game if any(el in los1 for el in hod(*x)))
game -= win2
los2 = set(x for x in game if all(el in win1 or el in win2 for el in hod(*x)))
game -= los2
for u in sorted(win1):
    if u[0] == 24 or u[1] == 24:
        print(u)
print(len(win1))
print(len(win2))
for u in sorted(los2):
    if u[0] == 24 or u[1] == 24:
        print(u)
        '''

#25
'''
def check(n):
    f = 0
    if n % 111 == 0:
        if f == 0:
            f = 1
        else:
            return False
    if n % 113 == 0:
        if f == 0:
            f = 2
        else:
            return False
    if n % 127 == 0:
        if f == 0:
            f = 3
        else:
            return False
    if f == 1:
        return 111
    if f == 2:
        return 113
    if f == 3:
        return 127
    return False
A = set()
for a in range(0, 10):
    for b in range(0, 10):
        s = str(a) + "15" + str(b) + "7424"
        m = int(s)
        res = check(m)
        if res:
            A.add((m, m // res))
for b in range(0, 100):
    s =  "15" + str(b) + "7424"
    m = int(s)
    res = check(m)
    if res:
        A.add((m, m // res))
for a in range(0, 100):
    s = str(a) + "15" + "7424"
    m = int(s)
    res = check(m)
    if res:
        A.add((m, m // res))
if check(157424):
    A.add(157424, m // check(157424))
for x in sorted(A):
    print(*x)
    '''


#25
with open("24.txt") as f:
    s = f.readline()
print(s[:4])
D = {}
for x in s:
    if x not in D:
        D[x] = 1
    else:
        D[x] += 1
A = sorted(D.items(), key = lambda x: -x[1])
print(A)
ma = ['D', 'V', 'E']
mi = ['F', 'N', 'I']
c = 0
for i in range(len(s)-1):
    if s[i] in mi and s[i+1] in ma or s[i] in ma and s[i + 1] in mi:
        c += 1
print(c)
        

            
    
            
