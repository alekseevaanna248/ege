#19-21 (24)
'''
def ff(a, b, h):
    if a >= 479 or b >= 479: return h%2==0
    if h == 0:
        return 0
    hod = [(a+1,b), (b + 1, a), (a+3, b), (a, b+3), (a*2, b), (a, b*2)]
    h = h - 1
    if h % 2 == 0:
        return any(ff(*el, h) for el in hod)
    return all(ff(*el, h) for el in hod)
print("#19-----", [s for s in range(1, 479) if ff(239, s,1)])
print("#19", [s for s in range(1, 479) if ff(239, s,2)])
print("#19", [s for s in range(1, 479) if ff(239, s,2)])
print("#20", [s for s in range(1, 479) if ff(239, s,3) and not ff(239, s, 1)])
print("#21", [s for s in range(1, 479) if ff(239, s,4) and not ff(239, s, 2)])
'''


#23
'''
def ff(a, b):
    if a > b or a == 17:
        return 0
    if a == b:
        return 1
    return ff(a+1, b) + ff(a*2, b) + ff(a**2, b)
print(ff(2, 16)*ff(16, 65))
'''


#25
'''
A = []
for a in range(10):
    for b in range(10):
        s0 = "671" + str(a) + str(b) + '1'
        #emp
        n = int(s0)
        if n %2023==0:
            A.append(n)
        #1-9
        for c in range(10):
            s = s0+str(c)
            n = int(s)
            if n %2023==0:
                A.append(n)
        #two signs
        for c in range(100):
            s = s0 + str(c).zfill(2)
            n = int(s)
            if n %2023==0:
                A.append(n)
A.sort()
for x in A:
    print(x, x//2023)
    '''


#24
'''
from re import *
with open("24.txt") as f:
    s = f.readline()
print(s[:3])

r = '([BCDF][AEU][BCDF])+'

A = finditer(r, s)
m = 0
for x in A:
    
    m = max(m, x.end() - x.start())
print(m)
'''


#26
with open("26 (1).txt") as f:
    N, M = list(map(int, f.readline().split()))
    A = list(map(int, f.readlines()))
print(N, M)
print(A[:10])
A.sort()
c = 0
su = 0
for i in range(len(A)):
    if su + A[i] <= M:
        su += A[i]
        c+=1
        j = i
print(c)
su -= A[j]
c-=1
for i in range(j, len(A)):
    if su + A[i] > M:
        print(i, A[i-1])
        break







        
    
























            
        




























