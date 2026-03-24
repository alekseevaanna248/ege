#2
'''
print("x y z w")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f = ( (x and y) <= (not z) ) and (x <= y) or w
                if not f:
                    print(x, y, z, w)
                    '''

#4
'''
def p4(n):
    s = ""
    if n == 0:
        return "0"
    while n > 0:
        e = n % 4
        n //= 4
        s = str(e) + s
    return s
print(p4(13))

def ff(n):
    r = p4(n)
    if n % 4 == 0:
        r += r[len(r) - 2:]
    else:
        r = r + p4(sum(list(map(int, list(r)))) * 4)
    return int(r, 4)

m = 10**8
for n in range(1, 1000):
    r = ff(n)
    if r % 2 == 0 and r % 3 == 0 and r > 211:
        m = min(m, r)
print(m)
'''


#8
# p r o f i m a t k   a i k m o p r t f
#                     0 1 2 3 4 5 6 7 8



'''
def p9(n):
    s = ""
    if n == 0:
        return "0"
    while n > 0:
        e = n % 9
        n //= 9
        s = str(e) + s
    return s
print(p9(13))
def check(s):
    if s.count('0') == 2 and all([s.count(str(j)) == 1 for j in range(2, 9)]) and s[0] != '5' \
       and not "11" in s:
        return True
    return False
c = 0
for n in range(0, 9 ** 11):
    s = p9(n).zfill(11)
    if check(s):
        c += 1
print(c)

'''
#9
'''
with open("9 (1).csv") as f:
    A = [list(map(int, x.split(';'))) for x in f.readlines()]
print(A[:10])

def check(A):
    D = {}
    m = -10**9
    for x in A:
        m = max(x, m)
        if x not in D:
            D[x] = 1
        else:
            D[x] += 1
    B = sorted(D.values())
    if B == [1, 1, 1, 1, 3] and D[m] == 3 and abs(m) % 10 == 0:
        return True
    return False

for i in range(len(A)):
    if check(A[i]):
        print(i + 1)
        break
        '''

#13
'''
from ipaddress import *
net = ip_network("190.202.83.62/22", 0)
N = net.hosts()
c = 0
for nod in N:
    c += 1
    if c == 1:
        a = nod
    b = nod
print(a)
print(b)
'''

#14
'''
n = 4 * 28 ** 10 + 3 * 28 ** 6 + 28 ** 3
def p28(n):
    s = []
    if n == 0:
        return '0'
    while n > 0:
        e = n % 28
        n //= 28
        s.append(e)
    return s[::-1]
print(p28(n))

m = 0
for x in range(1, 28001):
    s = p28(n - x)
    b = s.count(0)
    if b > m:
        m = b
        res = x
print(b, res)
print(n - res)
'''

#16
'''
F = ['*'] * 260000
G = ['*'] * 260000
G0 = ['*'] * 10
for i in range(1, 10):
    G0[i] = i // 20 + 45
    
for n in range(len(G) - 1, -1, -1):
    if n >= 250 * 10**3:
        G[n] = n // 20 + 45
    else:
        G[n] = G[n + 9] - 2
for n in range(len(F)):
    if n >= 25:
        F[n] = F[n - 6] + 4137
    elif n >= 9:
        F[n] = 7 * (G[n - 9] - 40)
    else:
        F[n] = 7 * (G0[9 - n] - 40)
print(F[680])
'''

#17
'''
def troh(A):
    c = 0
    for x in A:
        if 100 <= abs(x) <= 999 and abs(x) % 10 == 9:
            c += 1
    return c
with open("17.txt") as f:
    A = list(map(int, f.readlines()))
print(A[:10])

m = -10**12
for x in A:
    if x > m and abs(x) % 100 == 42:
        m = x
print(m)
c = 0
masu = -10**9
for i in range(len(A) - 2):
    B = A[i: i + 3]
    if troh(B) == 1 and sum(B) > m:
        c += 1
        masu = max(masu, sum(B))
print(c, masu)
'''

#19
'''
def hod(a, b):
    return ((a+1, b), (a, b + 1), (a * 2, b), (a, b * 2))
from itertools import *
game = set(x for x in product(range(1, 200), repeat = 2))
print(len(game))
win1 = set(x for x in game if any(sum(el) >= 81 for el in hod(*x)))
print(len(win1))
game -= win1
st = set(x for x in game if any(el in win1 for el in hod(*x)))
print("###st##")
S = []
for x in st:
    if x[0] == 7:
        s = x[1]
        if 1 <= s <= 73:
            S.append(s)
print(sorted(S))
print(len(st))

los1 = set(x for x in game if all(el in win1 for el in hod(*x)))
game -= los1
win2 = set(x for x in game if any(el in los1 for el in hod(*x)))
print("###win2##")
S = []
for x in win2:
    if x[0] == 7:
        s = x[1]
        if 1 <= s <= 73:
            S.append(s)
print(sorted(S))
game -= win2
los2 = set(x for x in game if all(el in win1 or el in win2 for el in hod(*x)))
print("###los2##")
S = []
for x in los2:
    if x[0] == 7:
        s = x[1]
        if 1 <= s <= 73:
            S.append(s)
print(sorted(S))
print(len(st))
'''


#23
'''
A = ['*'] * 50
for n in range(len(A)):
    if n < 16:
        A[n] = set("")
    elif n == 16:
        A[n] = set("0")
    else:
        A[n] = set()
        
print(A)
for n in range(17, 49):
    for i in range(1, 5):
        #print(n, i)
        for x in A[n-(2 ** (i - 1))]:
            if x[-1] != str(i):
                A[n].add(x + str(i))
print(A[20])
print(len(A[48])    )
'''


#24
from re import *
with open("24.txt") as f:
    s = f.readline()
r = '[A-Za-z]+@[A-Za-z]+_[A-Za-z]+'
A = findall(r, s)
print(len(A))
m = 0
for x in A:
    if len(x) > m:
        m = len(x)
        y = x
Y = y.split('@')[1]
print(len(Y))

    








    































                 
        




    
    
    
