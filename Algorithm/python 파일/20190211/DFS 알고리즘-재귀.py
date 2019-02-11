def dfs(v):
    global G, visited, n
    visited[v] = 1
    print(v, end=" ")

    for w in range(n):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open("input.txt")

n, e = map(int, input().split())
n += 1
temp = list(map(int, input().split()))

G = [[0 for _ in range(n)] for _ in range(n)] # 2차원 초기화
visited = [0 for i in range(n)] # 방문처리

for i in range(0, len(temp), 2): #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(n):
    print("{} {}".format(i, G[i]))


dfs(1)

# dfs = (G, 1, n)