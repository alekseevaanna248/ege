#24562
'''def dist(z1, z2):
    x1, y1 = z1
    x2, y2 = z2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def dist1(z, A):
    su = 0
    for z1 in A:
        su += dist(z, z1)
    return su
def centre(A):
    m0 = 10**12
    for i in range(len(A)):
        d1 = dist1(A[i], A[:i] + A[i + 1:])
        if d1 < m0:
            z0 = A[i]
            m0 = d1
    return z0

        
A1 = []
A2 = []
with open("27A_24562.txt") as f:
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if x < -40:
            A1.append(z)
        else:
            A2.append(z)
x1, y1 = centre(A1)
x2, y2 = centre(A2)
print(abs(int((x1 + x2) * 10 ** 4)))
print(abs(int((y1 + y2) * 10 ** 4)))

B1 = []
B2 = []
B3 = []
with open("27B_24562.txt") as f:
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if x < -30 and y < 30:
            B1.append(z)
        elif 0 < x < 10:
            B2.append(z)
        elif x > 10 and y < -2.1655:
            B3.append(z)
z01 = centre(B1)
z02 = centre(B2)
z03 = centre(B3)
B1.remove(z01)
B2.remove(z02)
B3.remove(z03)
x1, y1 = centre(B1)
x2, y2 = centre(B2)
x3, y3 = centre(B3)
print(abs(int((x1 + x2 + x3) * 10 ** 4)))
print(abs(int((y1 + y2 + y3) * 10 ** 4)))
'''
    
#24670
'''def dist(z1, z2):
    x1, y1 = z1
    x2, y2 = z2
    return abs(x1 - x2) + abs(y1 - y2)
def dist1(z, A):
    su = 0
    for z1 in A:
        su += dist(z, z1)
    return su
def centre(A):
    m0 = 10**12
    for i in range(len(A)):
        d1 = dist1(A[i], A[:i] + A[i + 1:])
        if d1 < m0:
            z0 = A[i]
            m0 = d1
    return z0

with open("27A_24670.txt") as f:
    A1 = []
    A2 = []
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if x < 10:
            A1.append(z)
        else:
            A2.append(z)
x1, y1 = centre(A1)
x2, y2 = centre(A2)
avx = (x1 + x2) / 2
avy = (y1 + y2) / 2    
print(int(avx*10**4), int(avy*10**4))
            
with open("27B_24670.txt") as f:
    B1 = []
    B2 = []
    B3 = []
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if x < 10:
            B1.append(z)
        elif y < 20:
            B2.append(z)
        else:
            B3.append(z)
x1, y1 = centre(B1)
x2, y2 = centre(B2)
x3, y3 = centre(B3)
avx = (x1 + x2 + x3) / 3
avy = (y1 + y2 + y3) / 3
print(int(avx*10**4), int(avy*10**4))'''


#24898
'''def dist(z1, z2):
    x1, y1 = z1
    x2, y2 = z2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def dist1(z, A):
    su = 0
    for z1 in A:
        su += dist(z, z1)
    return su
def centre(A):
    m0 = 10**12
    for i in range(len(A)):
        d1 = dist1(A[i], A[:i] + A[i + 1:])
        if d1 < m0:
            z0 = A[i]
            m0 = d1
    return z0

A1 = []
A2 = []
with open ("27_A_24898.txt") as f:
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if x < 30:
            A1.append(z)
        else:
            A2.append(z)
x1, y1 = centre(A1)
x2, y2 = centre(A2)
p1 = x1 + y1
p2 = x2 + y2
print(int(p1*10**4), int(p2*10**4))
    
with open("27B_24898.txt") as f:
    B1 = []
    B2 = []
    B3 = []
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        #...
'''


#23766
'''def dist(z1, z2):
    x1, y1 = z1
    x2, y2 = z2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def dist1(z, A):
    su = 0
    for z1 in A:
        su += dist(z, z1)
    return su
def centre(A):
    m0 = 10**12
    for i in range(len(A)):
        d1 = dist1(A[i], A[:i] + A[i + 1:])
        if d1 < m0:
            z0 = A[i]
            m0 = d1
    return z0

with open("27_A_23766.txt") as f:
    A1 = []
    A2 = []
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if y < 10:
            A1.append(z)
        else:
            A2.append(z)
x1, y1 = centre(A1)
x2, y2 = centre(A2)
px = min(x1, x2)
py = min(y1, y2)
print(int(px*10**4), int(py*10**4))

with open("27_B_23766.txt") as f:
    B1 = []
    B2 = []
    B3 = []
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if 10 < y < 20:
            B1.append(z)
        elif 20 < y < 30:
            if x < 17:
                B2.append(z)
            else:
                B3.append(z)
def qq(A):
    z0 = centre(A)
    m = 0
    for z in A:
        m = max(m, dist(z0, z))
    return m
#print(len(B1), len(B2), len(B3))
x1, y1 = centre(B1)
x2, y2 = centre(B2)
x3, y3 = centre(B3)
m1 = qq(B1)
m2 = qq(B2)
m3 = qq(B3)
q2 = max(m1, m2, m3)
q1 = dist(centre(B3), centre(B1))
print(int(q1*10**4), int(q2*10**4))'''

#23571
def dist(z1, z2):
    x1, y1 = z1
    x2, y2 = z2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def dist1(z, A):
    su = 0
    for z1 in A:
        su += dist(z, z1)
    return su
def centre(A):
    m0 = 10**12
    for i in range(len(A)):
        d1 = dist1(A[i], A[:i] + A[i + 1:])
        if d1 < m0:
            z0 = A[i]
            m0 = d1
    return z0

with open("27_A_23571.txt") as f:
    A1 = []
    A2 = []
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if y < 15:
            A1.append(z)
        else:
            A2.append(z)
x1, y1 = centre(A1)
x2, y2 = centre(A2)
px = x1 + x2
py = y1 + y2
print(int(px*10**4), int(py*10**4))

def min_dist(A1, A2):
    m = 10**8
    for z1 in A1:
        for z2 in A2:
            d = dist(z1, z2)
            m = min(m, d)
    return m

def max_dist(A1, A2):
    m = 0
    for z1 in A1:
        for z2 in A2:
            d = dist(z1, z2)
            m = max(m, d)
    return m

with open("27_B_23571.txt") as f:
    B1 = []
    B2 = []
    B3 = []
    f.readline()
    for s in f.readlines():
        s = s.replace(',', '.').split()
        x, y = float(s[0]), float(s[1])
        z = (x, y)
        if 10 < x < 30:
            if x > 20:
                B1.append(z)
            elif y < 14:
                B2.append(z)
            else:
                B3.append(z)
q1 = min(min_dist(B1, B2), min_dist(B1, B3), min_dist(B3, B2))
q2 = max(max_dist(B1, B2), max_dist(B1, B3), max_dist(B3, B2)) 
print(int(q1*10**4), int(q2*10**4))
