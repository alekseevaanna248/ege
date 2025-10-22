#18141
'''def su(n):
    s = 0
    while n > 0:
        e = n % 10
        n //= 10
        s += e
    return s;

def ff(n):
    if n <= 10:
        return n
    if n % 2 == 0:
        return 2 * ff(n-2) + 6
    else:
        return ff(n-1)+2*n
def ff1():
    A = [0] * 28
    for i in range(11):
        A[i] = i
    for i in range(11, 28):
        if i % 2 == 0:
            A[i] = 2 * A[i - 2] + 6
        else:
            A[i] = A[i - 1] + 2 * i
    return A[27] - A[20]
print(su(ff1()))
print(su(ff(27) - ff(20)))
#20'''


#18123
'''def ff(n):
    if n >= 2010:
        return n
    return ff(n + 3) + ff(n + 2) + ff(n + 1)
def f1():
    A=[0] * 2020
    for i in range(2019, 1999, -1):
        if i >= 2010:
            A[i] = i
        else:
            A[i] = A[i + 1] + A[i + 2] + A[i + 3]
            #print(A[i])
    return (A[2000] - 2 * (A[2002] + A[2003])) // A[2004]
print(f1())
print((ff(2000) - 2 * (ff(2002) + ff(2003))) // ff(2004))
#1'''


#17974
'''def ff(n):
    if n < 5:
        return 4**4
    return 4 * ff(n - 4) + 4
def f1():
    A = [0] * 4049
    for i in range(4049):
        if i < 5:
            A[i] = 4**4
        else:
            A[i] = 4 * A[i - 4] + 4
    return A[4048] // A[4036]
print(f1())
print(ff(4048) // ff(4036))
#64'''


#17872
'''import sys
sys.setrecursionlimit(2050)
def ff(n):
    if n == 1:
        return 1
    return (n - 1) * ff(n - 1)
def f1():
    A = [0] * 2025
    A[1] = 1
    for i in range(2, 2025):
        A[i] = (i - 1) * A[i - 1]
    return (A[2024] + 2 * A[2023]) // A[2022]
print(f1())
print((ff(2024) + 2 * ff(2023)) // ff(2022))
#4094550'''


#17755
'''def ff(n):
    if n > 400:
        return n ** n
    return n + 6 + ff(n + 12)
def f1():
    A = [0] * 413
    for i in range (412, 71, -1):
        if i > 400:
            A[i] = i ** i
        else:
            A[i] = i + 6 + A[i + 12]
    return A[72] - A[108]
print(ff(72) - ff(108))
print(f1())
#270'''


#5
'''A = [0] * (3 + 44)
c = 0
c1 = 0
for i in range(8):
    if c > 0:
        A[c + 3] = 3 * A[c - 4 + 3]
        c = c - 3
    elif c == 0:
        A[c + 3] = 5
        c = -3
    else:
        A[c + 3] = A[c + 3 + 3]
        c = c + 4
for i in range(4, 44):
    A[i + 3] = 3 * A[i - 4 + 3]
print(A[43 + 3])
def ff(n):
    if n == 0:
        return 5
    if n > 0:
        return 3 * ff(n - 4)
    return ff(n + 3)
print(ff(43))
#7971615'''
