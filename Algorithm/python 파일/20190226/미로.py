def point(data):
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                return x, y
def bfs(x, y):
    global G, V
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue=[]
    queue.append([x, y])
    visited[x][y] = 1
    while len(queue) != 0:
        v = queue.pop(0)
        for k in range(4):
            nx = v[0] + dx[k]
            ny = v[1] + dy[k]

            if nx == N or nx < 0: continue
            if ny == N or ny < 0: continue

            if data[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append([nx,ny])
                visited[nx][ny] = visited[v[0]][v[1]] + 1

            if data[nx][ny] == 3:
                visited[nx][ny] = visited[v[0]][v[1]]
                return visited[nx][ny] - 1
    return 0

import sys
sys.stdin = open("미로_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    sx, sy = point(data)
    ans = bfs(sx, sy)

    print(f'#{tc} {ans}')