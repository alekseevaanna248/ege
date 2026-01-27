#1202
'''
def hod(a, b):
    return [(a - 1, b), (a, b - 1), ((a + 1) // 2, b), (a, (b + 1) // 2)]
from itertools import *
heap = set(product(range(1, 100), repeat = 2))
#print(heap)
win1 = set(x for x in heap if any(sum(el) <= 32 for el in hod(*x)) )
heap -= win1
los1 = set(x for x in heap if all(el in win1 for el in hod(*x)) )
heap -= los1
win2 = set(x for x in heap if any(el in los1 for el in hod(*x)) )
heap -= win2
win1_2 = win1 | win2
los2 = set(x for x in heap if all(el in win1_2 for el in hod(*x)) )
#print(*win1, sep = '\n')

for s in range(23, 100):
    A = (10, s)
    if A in los2:
        print(A)
        '''

#10102
'''
def hod(a):
    return [a + 1, a * 2]
from itertools import *
heap = set(range(1, 129))
win1 = set(x for x in heap if any(el >= 129 for el in hod(x)) )
heap -= win1
los1 = set(x for x in heap if all(el in win1 for el in hod(x)) )
heap -= los1
win2 = set(x for x in heap if any(el in los1 for el in hod(x)) )
heap -= win2
win1_2 = win1 | win2
los2 = set(x for x in heap if all(el in win1_2 for el in hod(x)) )
#print(*win1, sep = '\n')

for s in range(23, 100):
    if s in los2:
        print(s)
        '''

#17875
'''
from functools import *
@cache
def g(a):
    hod = [a - 2, a - 5, a // 3]
    if a <= 19: return 'w'
    if any(g(x) == 'w' for x in hod): return "p1"
    if all(g(x) == 'p1' for x in hod): return 'v1'
    if any(g(x) == 'v1' for x in hod): return 'p2'
    if all(g(x) == 'p2' or g(x) == 'p1' for x in hod): return 'v2'
for s in range(1, 100):
    print(s, g(s))
    '''

#23759
from functools import *
@cache
def g(a):
    hod = [a - 3, a - 5, a // 4]
    if a <= 30: return 'w'
    if any(g(x) == 'w' for x in hod): return "p1"
    if all(g(x) == 'p1' for x in hod): return 'v1'
    if any(g(x) == 'v1' for x in hod): return 'p2'
    if all(g(x) == 'p2' or g(x) == 'p1' for x in hod): return 'v2'
for s in range(31, 500):
    print(s, g(s))
