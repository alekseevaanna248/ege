'''def ff(n):
    if n >= 2025:
        return n * 3
    else:
        return n + ff(n + 1) - ff(n + 2)
print(ff(2005) + ff(2015))'''
#33


#17
'''with open ("17_19861.txt") as f:
    A = list(map(int, f.readlines()))
print(A[:3])
mi = 10**6   
for x in A:
    if x > 0 and x % 100 == 97:
        mi = min(x, mi)
print(mi)

c = 0
masu = -10**6
for i in range(len(A) - 1):
    if A[i] + A[i+1] < mi:
        masu = max(masu, A[i] + A[i+1])
        c += 1
print(c, masu)'''
#4968 289


#25
'''def ff(a, b):
    if a > b:
        return 0
    if a == 25:
        return 0
    if a == b:
        return 1
    return ff(a+2,b) + ff(a+5,b) + ff(a*2,b)
print(ff(2,13)*ff(13,34))'''
#180

#24
'''from re import *
r='\d+(\*\d+)*'
with open ("24_19866.txt") as f:
    A=f.readline()
B=finditer(r,A)
m = 0
for x in B:
    s = A[x.start(): x.end()]
    m=max(m,s.count('*'))
print(m+1)'''
#8


#25
def su(n):
    s=0
    while n > 0:
        e=n%10
        n//=10
        s+=e
    return s
for n in range(222222, 666667):
    if (n//(10**5)) % 2 == 0 and ((n//(10**4))%10) % 2 == 0 and n % 1235 == 0:
        print(su(n), n//1235)
