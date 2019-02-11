def ladder(w, h, L):
    L[w][h] = 2
    if w == 0:
        return h
    else:
        if h != 0 and h != 99:
            if L[w][h+1] == 1:
                return ladder(w, h+1, L)
            elif L[w][h-1] == 1:
                return ladder(w, h-1, L)
            else:
                return ladder(w-1, h, L)
        elif h == 0:
            if L[w][h+1] == 1:
                return ladder(w, h+1, L)
            else:
                return ladder(w-1, h, L)
        else:
            if L[w][h-1] == 1:
                return ladder(w, h-1, L)
            else:
                return ladder(w-1, h, L)


import sys
sys.stdin = open("ladder_input.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    H = 0
    for i in range(100):
        if data[99][i] == 2:
            H = i

    print(f'#{tc} {ladder(99, H, data)}')