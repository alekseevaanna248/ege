#8

def check(s):
    f = s.count('d') + s.count('e') + s.count('f')
    if f == 2:
        if 'ee' in s or 'dd' in s or 'ff' in s or "de" in s or "ef" in s or "df" in s or "ed" in s or "fe" in s or "fd" in s:
            if '5' in s:
                return True
    return False

c = 0
for n in range(16**5, 16**6):
    r = hex(n)[2:]
    if check(r):
        c += 1
        x = r
print(c, x)
#335241


#9
'''
def check(A):
    c = 0
    for x in A:
        if abs(x) % 2 == 0:
            c += 1
    B = sorted(A)
    if B == A and c == 3:
        return True
    return False
with open("9.csv") as f:
    A = [list(map(int, x.split(';'))) for x in f]
print(A[:9])

c = 0
for s in A:
    if check(s):
        c += 1
        su = sum(s)
print(c, su)
#1355
'''
#или
'''
def check(A):
    c = 0
    for x in A:
        if abs(x) % 2 == 0:
            c += 1
    B = sorted(A)
    if B == A and c == 3 and len(set(A)) == 6:
        return True
    return False
with open("9.csv") as f:
    A = [list(map(int, x.split(';'))) for x in f]
print(A[:9])

c = 0
for s in A:
    if check(s):
        c += 1
        su = sum(s)
print(c, su)
#1509
'''


#11
'''
print(2*26 + 10 + 15)
i = 7
I = 7 * 30 / 8
print(I)
print(2*2**20/(27+28))
#38130
'''

#17
'''
def check(A):
    c = 0
    for x in A:
        if 99 < x <= 999 or -99 <= x < -9:
            c += 1
    if c <= 2:
        return True
    return False
with open("17.txt") as f:
    A = list(map(int, f.readlines()))
print(A[:7])
m = 1000
for x in A:
    if 99 < x <= 999:
        m = min(m, x)
print(m)

masu = 0
c = 0
for i in range(len(A) - 2):
    a1 = A[i]
    a2 = A[i + 1]
    a3 = A[i + 2]
    if check([a1, a2, a3]) and (a1 + a2 + a3) >= m:
        c += 1
        masu = max(masu, a1 + a2 + a3)
print(c, masu)
#2442 27284
'''

#24
'''
with open("24.txt") as f:
    A = f.readline()
#A = "r6е79yyyiii88gg5у"
f = 0
s1 = [0, 0]
Words = []
for i in range(len(A)):
    x = A[i]
    if x.isdigit():
        f = 1
        if s1 != [0, 0]:
            s1[1] = i - 1
            Words.append(s1)
        s1 = [0, 0]
    elif x.isalpha() and f > 0:
        if f == 1:
            s1[0] = i
        f = 2
    else:
        f = 0
print(A[:32])
print(Words[:9])

mi = 10**7
ppp = 10**4
for l in range(len(Words) - ppp + 1):
    l1 = Words[l + ppp - 1][1] - Words[l][0] + 1 + 2
    mi = min(mi, l1)
print(mi)
#68616
'''

#26
'''
ANS1 = []
p = 3600 * 24 * 10**3
with open ("26.txt") as f:
    f.readline()
    A = [list(map(int, x.split())) for x in f]
print(A[:8])
A.sort()
B = []
prev_r = 0
for x in A:
    if x[1] > prev_r:
        B.append(x)
    prev_r = x[1]
delay = B[0][0]
c = 0
if delay > 0:
    c += 1
print(len(B))
for i in range(1, len(B)):
    cur = B[i]
    prev = B[i - 1]
    if cur[0] > prev[1]:
        c += 1
        delay += cur[0] - prev[1]
        ANS1.append((tuple(prev), tuple(cur)))
if B[-1][1] != p:
    c +=1
delay += p - B[-1][1]
print(c, delay)
#1035 1058639
'''



#25
'''
ans = []
for a in [0, 2, 4, 6, 8]:
    for b in [0, 2, 4, 6, 8]:
        s = "7" + str(a) + "23" + str(b) + "64" +'8'
        n = int(s)
        if n % 2026 == 0:
            ans.append(n)
        for c in range(100):
            s = "7" + str(a) + "23" + str(b) + "64" + str(c)+'8'
            n = int(s)
            if n % 2026 == 0:
                ans.append(n)
            if c <= 9:
                s = "7" + str(a) + "23" + str(b) + "64" + '0' + str(c)+'8'
                n = int(s)
                if n % 2026 == 0:
                    ans.append(n)
print(*sorted(ans), sep = '\n')
#782386498
#7023064168
#7023864438
#7623064068
#7623864338

'''
        
#27B
'''
def dist(z1, z2):
    x1, y1 = z1
    x2, y2 = z2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def diam(A):
    ans = [0, 0]
    m = 0
    for i in range(len(A)):
        for z in A[i + 1:]:
            r = dist(A[i], z)
            if r > m:
                m = r
                ans[0] = A[i]
                ans[1] = z
    return ans

def ma_dist(D1, D2):
    m = 0
    for z1 in D1:
        for z2 in D2:
            m = max(m, dist(z1, z2))
    return m
            
            
with open("27B.txt") as f:
    A1 = []
    A2 = []
    A3 = []
    for z in f:
        z = z.split()
        x = float(z[0])
        y = float(z[1])
        z = [x, y]
        if x > 25:
            A1.append(z)
        elif x < 0 and y < 0:
            A2.append(z)
        elif x < 0 and 0 < y < 15:
            A3.append(z)

D1 = diam(A1)
D2 = diam(A2)
D3 = diam(A3)

print(len(A1))
print(len(A2))
print(len(A3))

q1 = int(dist(D1[0], D1[1]) * 10**4)
print(q1)
q2 = max(ma_dist(D1, D2), ma_dist(D2, D3), ma_dist(D1, D3))
q2 = int(q2 * 10**4)
print(q2)
# 29254 488624
'''
     


        


