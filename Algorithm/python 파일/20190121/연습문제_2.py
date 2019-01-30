arr = [-7, -3, -2, 5, 8]
n = len(arr)
sum = 0
cnt = 0

for i in range(1, 1 << n):
    sum = 0
    for j in range(n):
        if i & (1 <<j):
            a = arr[j]
            sum += a
    if sum == 0:
        cnt += 1
        for j in range(n):
            if i & (1 << j):
                print(arr[j], end =" ")
    print()
print(f'개수 : {cnt}')
