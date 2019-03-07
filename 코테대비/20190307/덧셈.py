S, X = map(str, input().split())

for n in range(1, len(S)):
    if int(S[:n]) + int(S[n:]) == int(X):
        print("{}+{}={}".format(int(S[:n]), int(S[n:]), int(X)))
        break
else:
    print('NONE')