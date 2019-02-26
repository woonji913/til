def bfs(start):
    global D, V, S, G
    queue = []

    queue.append(start)
    visited[start] = 1 # 방문처리하기
    while len(queue) != 0:
        t = queue.pop(0)
        for p in range(1, V+1):
            if D[t][p] == 1 and visited[p] == 0:
                queue.append(p)
                visited[p] = visited[t] + 1

            if t == G:
                return visited[G] - visited[S]
    return 0

import sys
sys.stdin = open('노드_input.txt', 'r')

T = int(input())
for tc in range(T):
    V, E = list(map(int, input().split()))
    D = [[0 for i in range(V + 1)] for j in range(V + 1)] # 입력한 것
    data = []
    for i in range(E):
        data += list(map(int, input().split()))

        for i in range(0,len(data),2):
            D[data[i]][data[i + 1]] = 1
            D[data[i + 1]][data[i]] = 1

    S,G = list(map(int, input().split()))
    visited = [0 for _ in range(V + 1)]
    ans = bfs(S)

    print(f'#{tc + 1} {ans}')