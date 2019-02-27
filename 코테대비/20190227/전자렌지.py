T = int(input())

def microwave(T):
    A = 300
    B = 60
    C = 10

    if T >= 300:
        a = T // A
        b = (T - a*A) // B
        c = ((T - a*A) - b*B) // C
        if a*A + b*B + c*C == T:
            return a, b, c
        else:
            return -1

    elif T < 300 and T >= 60:
        a = 0
        b = T // B
        c = (T - b*B) // C
        if a*A + b*B + c*C == T:
            return a, b, c
        else:
            return -1

    elif T < 60:
        a = 0
        b = 0
        c = T // C
        if a*A + b*B + c*C == T:
            return a, b, c
        else:
            return -1

if microwave(T) == -1:
    print(microwave(T))
else:
    print(' '.join(list(map(str, microwave(T)))))