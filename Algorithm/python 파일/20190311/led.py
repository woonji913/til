def onoff(led):
    cnt = 0
    for x in range(1, len(led)+1):
        if data[x-1] != led[x-1]:
            for i in range(1, len(led)//x+1):
                if led[i*x - 1] == 0:
                    led[i*x - 1] = 1
                else:
                    led[i*x - 1] = 0
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input()))

    first = [0]*N

    print("#{} {}".format(tc, onoff(first)))
