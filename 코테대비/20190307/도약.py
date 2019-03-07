N = int(input())
point = [int(input()) for _ in range(N)]
point.sort()
# print(point)

cnt = 0
for j in range(N-2):
    for i in range(j+1, N-1):
        jump1 = point[i] - point[j]
        for k in range(i+1, N):
            jump2 = point[k] - point[i]
            if jump1*2 >= jump2 >= jump1:
                cnt += 1
            if jump2 > jump1*2:
                break
print(cnt)
