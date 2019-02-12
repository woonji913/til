import sys
sys.stdin = open("괄호검사_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    word = input()
    # print(word)

    new_word = []
    for i in word:
        if i == '(' or i == '{' or i == ')' or i == '}':
            new_word.append(i)
    # print(new_word)

    n = 0
    for i in range(len(new_word)):
        if new_word[i] == '(':
            n += 1
        elif new_word[i] == ')':
            n -= 1
        elif new_word[i] == '{':
            n += 2
        else:
            n -= 2

    if n == 0:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')