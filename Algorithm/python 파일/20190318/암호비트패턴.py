asc = [[0,0,0,0],
       [0,0,0,1],
       [0,0,1,0],
       [0,0,1,1],
       [0,1,0,0],
       [0,1,0,1],
       [0,1,1,0],
       [0,1,1,1],
       [1,0,0,0],
       [1,0,0,1],
       [1,0,1,0],
       [1,0,1,1],
       [1,1,0,0],
       [1,1,0,1],
       [1,1,1,0],
       [1,1,1,1],]

password = [[0,0,1,1,0,1],
           [0,1,0,0,1,1],
           [1,1,1,0,1,1],
           [1,1,0,0,0,1],
           [1,0,0,0,1,1],
           [1,1,0,1,1,1],
           [0,0,1,0,1,1],
           [1,1,1,1,0,1],
           [0,1,1,0,0,1],
           [1,0,1,1,1,1]]

def xtoo(x):
    if x <= '9':
        return ord(x) - ord('0')
    else:
        return ord(x) - ord('A') + 10

def otob(x):
    global B
    for i in range(4):
        B.append(asc[x][i])

# A = '0DEC'
A = '0269FAC9A0'
# 0000 1111 1001 0111 1010 0011
B = []

for i in range(len(A)):
    otob(xtoo(A[i]))

def findp(x):
    for i in range(10):
        cnt = 0
        for j in range(6):
            if x+j > len(B)-1:
                return 0
            if B[x+j] == password[i][j]:
                cnt += 1
            else:
                break
        if cnt == 6:
            ans.append(i)
            return 6
    return 0

id = 0
ans = []
while id < len(B):
    a = findp(id)
    if a == 0:
        id += 1
    else:
        id += a
print(*ans)
