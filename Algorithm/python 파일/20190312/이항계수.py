def bino2(n, k):
    # B[][]
    for i in range(n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]

    return B[n][k]

B = [[0]*5 for _ in range(5)]
print(bino2(4, 3))


def test(a,b,n):
    result = 0
    for r in range(n+1):
        fact = 1
        div = 1
        div2 = 1
        if r == 0:
            pass
        else:
            for r2 in range(n,n-r,-1):
                fact *= r2
            for r3 in range(1,r+1):
                div *= r3
        result += (fact/div)*a**(n-r)*b**r
    return result
print(test(2,1,3))