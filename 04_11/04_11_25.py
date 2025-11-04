'''print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f = (z <= y) or ((w <= x)<=y)
                if f == 0:
                        print(x, y, z, w)'''


#5
'''def rep(s):
    s1 = "1"
    for x in s[1:]:
        if x == '1':
            s1+='00'
        else:
            s1 += x
    return s1
        
def ff(n):
    s=bin(n)[2:]
    if n % 2 == 0:
        s = len(s) * '1'
    else:
        s = rep(s)
    return int(s, 2)

A=[]
for n in range(1000):
    r = ff(n)
    if r <= 600:
        A.append((r,n))
A.sort(key = lambda x: (-x[0], -x[1]))
print(A[0])'''

from turtle import *
speed(10)
k = 10
up()
for x in range(-35*k, 35*k, k):
    for y in range(-35*k, 35*k, k):
        setpos(x,y)
        down()
        dot (k * 0.4, "blue")
        up()
setpos(0,-10*k)    
lt(90)
down()
fd(30*k)
lt(60)
fd(24*k)
rt(240)
fd(54*k)
lt(120)
fd(24*k)
lt(60)
up()
fd(30*k)
rt(90)
fd(20*k)
lt(90)
down()
for _ in range(17):
    fd(6*k)
    lt(90)
    fd(80 * k)
    lt(90)
        
