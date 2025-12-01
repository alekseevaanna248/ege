#27
'''def dist(z1, z2):
    x1, y1 = z1
    x2, y2 = z2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def ff(A):
    m = 0
    su = 0
    c = 0
    for i in range(len(A)):
        for z in A[:i]+A[i+1:]:
            m = max(m, dist(A[i], z))
            su += dist(A[i], z)
            c += 1
    return (su / c) / m
with open("27_A.txt") as f:
    A1 = []
    A2 = []
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if x < 420 and y < 300:
            A1.append(z)
        elif x > 600 and y > 600:
            A2.append(z)
p1 = min(ff(A1), ff(A2))
p2 = (ff(A1) + ff(A2)) / 2
print(int(p1*10**4))
print(int(p2*10**4))'''


#17
'''with open("17.txt") as f:
    A = list(map(int, f.readlines()))
m = 10**12
m1 = 10**12
for x in A:
    if 99 < x <= 999:
        if x <= m:
            m1 = m
            m = x
        elif x < m1:
            m1 = x

c = 0
masu = 0
for i in range(len(A)-1):
    if (A[i] + A[i+1]) < m1**2:
        c += 1
        masu = max(masu, A[i] + A[i+1])
print(c)
print(masu)'''
        
#14
'''masu = 0
a0 = 2 + 5 * 14**2 + 4 * 14**4 + 1 * 14**5
b0 = 3 + 2 * 14**2 + 1 * 14**4 + 3 * 14**5
for x in range(14):
    for y in range(14):
        a = a0 + x * 14 + y * 14**3
        b = b0 + y * 14 + x * 14**3
        if (a+b)%9 == 0:
            if x + y >= masu:
                masu = x + y
                ans = (a+b)//9
print(ans)'''


#2
'''print("a b c d")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            for d in [0, 1]:
                f = ((a and b) <= c) and ((b and c) <= d)
                if not f:
                    print(a, b, c, d)'''

#25
'''def cc(n):
    A = set()
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            A.add(d)
            A.add(n//d)
    return len(A)
def ff(n):
    A = set()
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            A.add(d)
            A.add(n//d)
    if not A:
        return 0
    return min(A) + max(A)

ans = []
c=0
for n in range(650000, 10**6):
    if cc(n) == 6 and 999 < ff(n) <= 9999:
        ans.append((n, ff(n)))
        c+=1
    if c == 5:
        break
for i in range (4, -1, -1):
    print(*ans[i])'''


#24
from re import *
with open("24.txt") as f:
    s = f.readline()
s = s.replace('4', 'a')
s = s.replace('3', 'e')
r = '(yandex)+(yande|yand|yan|ya|y|)'
A = finditer(r,s)
m = 0
for x in A:
    start = x.span()[0]
    end = x.span()[1]
    s = end - start
    m = max(m, s)
print(m)


                
            
        
