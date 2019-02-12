import sys
sys.stdin = open("종이_input.txt", "r")

def facto(n):
  fac = 1
  for i in range(1, n + 1):
    fac *= i
  return fac

T = int(input())
for tc in range(1, T + 1):
    width= int(input()) // 10
    # print(width)

    # n 은 20*20의 최대 갯수
    n = width // 2
    # print(n)

    case = []
    for i in range(n+1):
        # small은 20*10 의 갯수
        small = width - i * 2

        if i == 0:
            result = 1
            case.append(result)
        else:
            result = (2**i) * (facto(i + small)//(facto(i)*facto(small)))
            case.append(result)

    print(f'#{tc} {sum(case)}')