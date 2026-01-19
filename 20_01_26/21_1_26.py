'''from turtle import *
showturtle()
tracer(0)
k = 8
up()
for x in range(-10*k, 10*k, k):
    for y in range(-10*k, 10*k, k):
        setpos(x, y)
        dot(k*0.5, "blue")
setpos(0, 0)
lt(90)
rt(315)
down()
print(1)
fd(3*k)
print(2)
down()
for _ in range(7):
    fd(72*k)
    rt(45)
    fd(43*k)
    rt(135)
done()'''


#14
'''
def pp(n, x):
    s = []
    while n > 0:
        e = n % x
        n //= x
        s.append(e)
    return s[::-1]
n = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255
for x in range(2, 1000):
    A = pp(n, x)
    if A[len(A) - 3:] == [0, 0, 1]:
        print(x)
#4
'''

#17

def check(A):
    A.sort()
    A = A[::-1]
    if A[0] > 0 and A[1] <= 0 and A[0] * A[1] * A[2] <= m * m1:
        return True
    return False
    

with open("17.txt") as f:
    A = list(map(int, f.readlines()))
print(A[:7])
m = -10**6
m1 = -10**6
c = 0
masu = -10**6
for x in A:
    if x > m:
        m1 = m
        m = x
    elif x == m:
        m1 = x
    elif x > m1:
        m1 = x
print(m, m1)

for i in range(len(A) - 2):
    if check(A[i: i + 3]):
        c += 1
        masu = max(masu, sum(A[i: i + 3]))
print(c, masu)
    
    

