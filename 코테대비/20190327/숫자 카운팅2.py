n = int(input())
narr = list(map(int, input().split()))
m = int(input())
marr = list(map(int, input().split()))

# 왼쪽 탐색
def lowerbound(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if narr[m] == data:
            sol = m
            e = m-1
        elif narr[m] < data:
            s = m+1
        else:
            e = m-1

    return sol

# 오른쪽 탐색
def upperbound(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if narr[m] == data:
            sol = m
            s = m+1
        elif narr[m] < data:
            e = m-1
        else:
            e = m-1
    return sol


narr.sort()
for i in range(m):
    a = lowerbound(0, n-1, marr[i])
    if a>=0:
        b = upperbound(a, n-1, marr[i])
        print(b-a+1, end=" ")
        # print(a)
    else:
        print(0, end=' ')