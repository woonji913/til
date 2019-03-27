def wrap(L):
    while len(L) != 1:
        L.sort(reverse=True)
        a = L.pop()+L.pop()
        L.append(a)
        result.append(a)

N = int(input())
L = list(map(int, input().split()))
result = []
wrap(L)
print(sum(result))