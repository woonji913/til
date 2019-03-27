def pack(candy):
    global cnt
    candy.sort()
    candy.insert(0, candy.pop(0) + candy.pop(0))
    cnt += candy[0]

N = int(input())
candy = list(map(int, input().split()))
cnt = 0
while len(candy) >= 2: pack(candy)
print(cnt)