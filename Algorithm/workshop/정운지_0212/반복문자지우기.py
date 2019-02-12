import sys
sys.stdin = open("반복_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    word = list(input())
    # print(word)

    i = 1
    while i != len(word):
        if word[i] == word[i-1]:
            del word[i-1], word[i-1]
            i = 0

        i += 1
        
    print(f'#{tc} {len(word)}')







