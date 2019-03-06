def find(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 어차피 가장자리가 0 이기 때문에 N 의 범위를 벗어날 필요가 없음
    for h in range(1, N):
        for i in range(4):
            if hosu[x+dx[i]*h][y+dy[i]*h] == 0:
                return h

N = int(input())
hosu = [list(map(int,input().split())) for _ in range(N)]

# 동서남북중 0 과의 거리를 구하는데, 짧은 거리를 채택
for i in range(1,N):
    for j in range(1,N):
        if hosu[i][j] != 0: # 물 위치일때
            hosu[i][j] = find(i,j)

#한번만 돌렸을 때 상하좌우로
# 배수를 곱해주면 4방향으로 길이를 더 확장해서
#MAIN - 1의 위치를 찾아
# 4방향에서 0 이면 바로 RETURN
# 1이면 확장


# 총합
cnt = 0
for i in range(N):
    for j in range(N):
        cnt += hosu[i][j]

print(cnt)