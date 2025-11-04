#8
'''def check(s):
    for i in range(len(s)-2):
        n1=1
        n2=1
        n3=1
        if s[i] in Ev:
            n1=0
        if s[i+1] in Ev:
            n2 = 0
        if s[i+2] in Ev:
            n3=0
        if (n1+n2+n3 == 0) or (n1 * n2 *n3 == 1):
            return False
    return True
from itertools import *
B = ['0', '1', '2', '3', '4', '5', '6', '7', '8', \
     '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
Ev = []
Odd = []
for i in range (17):
    if i %2 == 0:
        Ev.append(B[i])
    else:
        Odd.append(B[i])
A=list(permutations(B, 6))
c = 0
for x in A:
    if x[0] != '0' and check(x):
        c+=1
print(c)'''


#9
'''with open ("9_21976.csv") as f:
    A = [list(map(int, x.strip().split(';'))) for x in f.readlines()]
def ff(A):
    Ev = set()
    Odd =set()
    for x in A:
        if x % 2 == 0:
            Ev.add(x)
        else:
            Odd.add(x)
    sue = 0
    for x in Ev:
        sue += x
    sue **= 2
    suo = 0
    for x in Odd:
        suo += x**3
    if sue > suo:
        return True
    return False
for x in A:
    if len(set(x)) == 4 and ff(x):
        su = sum([y for y in x])
print(su)'''


#12
'''s = '1' + '8' * 110
while '1' in s:
    if "18" in s:
        s = s.replace('18', '8881', 1)
    else:
        s = s.replace('1', '888', 1)
su = sum([int(x) for x in s])
print(su)'''


#16
'''A=[0] * 75 * 10**3
for i in range(75*10**3):
    if i < 110:
        A[i] = i
    else:
        A[i] = (i - 7) * A[i - 8]
f = (A[74914] - A[74898]) / (16 * A[74890])
print(f)'''


#17
'''def check1(B):
    mi = 0
    pl = 0
    p = 1
    for x in B:
        if x < 0:
            mi += x
        else:
            pl += x
        p*=x
    if abs(mi) <= pl and ((abs(abs(p) - 7)) % 10 == 0):
        return abs(p)
    return False
    
with open ("17_21990.txt") as f:
    A = list(map(int, f.readlines()))
m = 0
c = 0
pm = 0
for x in A:
    m = max(m, x)
for i in range(len(A) - 2):
    B = [A[i], A[i + 1], A[i+2]]
    if check1(B):
        c+=1
        pm = max(check1(B), pm)
print(c, pm)'''


#23
'''def ff(a, b):
    if a < b or a == 20:
        return 0
    if a == b:
        return 1
    return ff(a-2,b) + ff(a-3,b) + ff(int(a**0.5),b)
print(ff(26,3))'''

#25
'''def pp(n):
    d = 2
    su = 0
    c = 0
    while d * d <= n:
        while n % d == 0:
            if d % 10 == 7:
                su += d
                c+=1
            n //= d
        d+=1
    if n % 10 == 7:
        su += n
        c+=1
    if c == 0:
        return 0
    return su // c

for n in range(750000-1, 0,-1):
    f = pp(n)
    if f!=0 and f % 111 == 0:
        print(n, f)'''


#26
'''with open ("26_22127.txt") as f:
    n = int(f.readline())
    A = [list(map(int, x.split())) for x in f.readlines()]
A.sort()
B = [(0,0)]
for x in A:
    if B[-1][1] < x[1]:
        B.append((x[0] - 1, x[1]))
print(B[:7], B[len(B) - 7:])
c=0
d = 0
for i in range(1,len(B)):
    if B[i][0] > B[i-1][1]:
        c+=1
        d += B[i][0] - B[i-1][1]
if B[-1][1] < 10**3*3600*24:
    c+=1
    d+=10**3*3600*24 - B[-1][1]
print(c, d)'''


#24
with open ("24_21981.txt") as f:
    s = f.readline()
co = 0
l=0
m=0
for r in range(len(s)):
    if '0' <= s[r] <= 'F':
        if s[r] == 'B':
            co += 1
        while s[l] == '0' or s[l] > 'F':
            l += 1
        while co > 10:
            if s[l] == 'B':
                co-=1
            l+=1
            
        if co == 10:
            m = max(r - l + 1, m)
    else:
        l = r + 1
        co = 0
print(m)
    
    
            
    
