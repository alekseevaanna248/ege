#7
'''print(700*0.75)
#11
print(12*2**30/12345678)
print(1044*8/1234)
print(2**6)
#12
print(500+101)'''
#13
'''def check(A):
    c = 0
    for x in A:
        if x % 2 != 0:
            c += 1
    if c == 2:
        return True
    return False
from ipaddress import *
net = ip_network("202.71.92.91/18", 0)
ans = ""
for node in net.hosts():
    dv = list(map(int, str(node).split('.')))
    if check(dv):
        ans = node
print(ans)'''
#14
'''a = 30**30 + 443*900**14+76*2700**12 - 81000**9
c = 0
while a > 0:
    e = a % 30
    a //= 30
    if e > 15:
        c+=1
print(c)'''
#15
'''def ff(n):
    if n < 10:
        return n + 10
    return ff(n - 8) + 2 ** n
ans = (ff(4000) + 2 * ff(3992)) / ff(3984)
print(ans)'''

#17
'''def check(A):
    c = 0
    for x in A:
        if 99 < x <= 999:
            c += 1
    if c == 2:
        return True
    return False
with open("17_24539.txt") as f:
    A = list(map(int, f.readlines()))
m = 0
for x in A:
    if x > m and 99 < x <= 999:
        m = x
co = 0
masu = 0
for i in range(len(A) - 2):
    a = A[i]
    b = A[i + 1]
    c = A[i + 2]
    if check([a, b, c]) and abs(a * b * c) % m == 0:
        co += 1
        masu = max(masu, abs(a + b + c))
print(co, masu)
'''

#25
from re import *
r = "\d{2}2\d*\d{2}"
for n in range(112211, 10**10):
    if n % 2026 == 0 and match(r, str(n)) and str(n) == str(n)[::-1]:
        print(n, n//2026)
