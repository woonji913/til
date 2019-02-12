import sys
sys.stdin = open("그래프_input.txt", "r")


T = int(input())
for N in range(T):
    V, E = map(int, input().split())
    L = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for C in range(E):
        a, b = map(int, input().split())
        L[a][b] = 1
    S, G = map(int, input().split())
