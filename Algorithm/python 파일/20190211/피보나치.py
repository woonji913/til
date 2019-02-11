# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)

# print(fibo(8))


'''
메모를 위한 배열을 할당하고, 모두 0으로 초기화한다.
memo[0]을 0으로 memo[1]은 1로 초기화한다.
'''
def fibo2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibo2(1000))