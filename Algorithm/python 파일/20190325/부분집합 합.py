# 부분집합 합이 10인경우


L = list(range(1, 11))

A = [0 for _ in range(len(L))]

result = []

def powerset(n, k):

    if n == k:
        sums = 0
        for i in range(len(A)):
            if A[i]:
                sums += L[i]
        if sums == 10:
            for i in range(len(A)):
                if A[i]:
                    print(L[i], end=" ")
            print()


    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)


powerset(len(L), 0)