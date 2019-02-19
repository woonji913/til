def push(item):
    stack.append(item)

def operator(x, y, cal):
    if cal == '+':
        return int(x) + int(y)
    elif cal == '-':
        return int(x) - int(y)
    elif cal == '*':
        return int(x) * int(y)
    elif cal == '/':
        return int(x) // int(y)

import sys
sys.stdin = open("cal_input.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = input()
    # print(data)
    #
    op = ['+', '-', '*', '/']
    stack = []
    for i in data:
        # print(stack)
        if i not in op and i != '.':
            push(i)
        elif i in op:
    #         if len(stack) < 2:
    #             result = 'error'
    #             break
            else:
                a = stack.pop()
                b = stack.pop()
                push(operator(b, a, i))
    #     elif i == '.':
    #         if len(stack) > 1:
    #             result = 'error'
    #             break
    #
    #         else:
    #             result = stack.pop()
    #         break
    #
    # print(f'#{tc} {result}')
    print(stack)