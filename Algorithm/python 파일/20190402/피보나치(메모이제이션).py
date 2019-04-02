def fib(n):
    global arr
    if n == 1 or n == 2:
        return 1

    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])

    return arr

N = int(input())
arr = [1, 1]
fib(N)
print(arr[N-1])
