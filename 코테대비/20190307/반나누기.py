def classroom(T1, T2, K_Min, K_Max):
    ABC = [[] for _ in range(3)]
    for i in score:
        if i >= T2:
            ABC[2].append(i)
        elif i < T1:
            ABC[0].append(i)
        else:
            ABC[1].append(i)
    person = [len(ABC[0]), len(ABC[1]), len(ABC[2])]
    if max(person) <= K_Max and min(person) >= K_Min:
        return max(person) - min(person)

T = int(input())
for tc in range(T):
    N, K_Min, K_Max = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()

    div_class = []
    for T1 in range(1, 101):
        for T2 in range(T1+1, 101):
            p = classroom(T1, T2, K_Min, K_Max)
            if p:
                div_class.append(p)
    print(div_class)
    if div_class:
        print(min(div_class))
    else:
        print(-1)