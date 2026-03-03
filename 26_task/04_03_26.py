#7602
with open("26_7602.txt") as f:
    f.readline()
    f.readline()
    A = [list(map(int, x.split())) for x in f.readlines()]
A.sort()
print(A[:10])
B = [[0, 0]] * 210
c = 0
for i in range(len(A)):
    for j in range(len(B)):
        if B[j][1] + 1 <= A[i][0]:
            c += 1
            box = j + 1
            B[j] = A[i]
            break
print(c, box)



#7626
'''with open("26_7626.txt") as f:
    f.readline()
    f.readline()
    A = [list(map(int, x.split())) for x in f.readlines()]
A.sort()
print(A[:10])
B = [[0, 0]] * 210
c = 0
for i in range(len(A)):
    for j in range(len(B)):
        if B[j][1] + 1 <= A[i][0]:
            c += 1
            box = j + 1
            B[j] = A[i]
            break
print(c, box)'''

#7826
'''
with open("26_7826.txt") as f:
    f.readline()
    A = [list(map(int, x.split())) for x in f.readlines()]
A.sort()
print(A[:10])
B = [[0, 0]] * 210
c = 0
for i in range(len(A)):
    for j in range(len(B)):
        if B[j][0] == A[i][0]:
            c += 1
            box = j + 1
            B[j][1] = max(A[i][1], B[j][1])
            break
    else:
        for j in range(len(B)):
            if B[j][1] + 1 <= A[i][0]:
                c += 1
                box = j + 1
                B[j] = A[i]
                break
print(c, box)'''
