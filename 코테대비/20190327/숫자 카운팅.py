N = int(input())
arr = list(map(int, input().split()))
M = int(input())
farr = list(map(int, input().split()))

parr = [0]*(arr[-1]+1)
for i in arr: parr[i]+=1
for i in farr:
    if i>arr[-1]: print(0, end=" ")
    else: print(parr[i], end=" ")