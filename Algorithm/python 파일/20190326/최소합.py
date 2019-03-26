import sys
sys.stdin = open("최소합input.txt", "r")

def iswall(x, y, N):
    if x<0 or x>=N: return True
    if y<0 or y>=N: return True
    return False

def comparison(start):
    



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    print(data)

    sums = data[0][0]
