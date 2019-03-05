for tc in range(10):
    # 정점의 수
    N = int(input())

    # 이진 트리 만들기
    tree = [0 for _ in range(N+1)]

    # 트리 채우기
    for i in range(N):
        input_T = input().split()
        # print(input_T)
        tree[int(input_T[0])] = input_T[1:]

    # 후위순회, 스텍쌓기
    stack = []
    def postorder(n):
        if len(tree[n]) > 1:
            postorder(int(tree[n][1]))
            postorder(int(tree[n][2]))
            stack.append(tree[n][0])
        else:
            stack.append(tree[n][0])
    postorder(1)

    # 스텍에서 연산하기
    i = 0
    op = ['+', '-', '*', '/']
    while len(stack) != 1:
        if stack[i] in op:
            if stack[i] == '+':
                stack[i] = int(stack[i-2]) + int(stack[i-1])
            elif stack[i] == '-':
                stack[i] = int(stack[i - 2]) - int(stack[i - 1])
            elif stack[i] == '*':
                stack[i] = int(stack[i - 2]) * int(stack[i - 1])
            else:
                stack[i] = int(stack[i - 2]) // int(stack[i - 1])
            stack.pop(i-2)
            stack.pop(i-2)
            i -= 2
        i += 1

    print('#{} {}'.format(tc+1, stack[0]))