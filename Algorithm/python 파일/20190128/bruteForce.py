def BruteForce(p, t):
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(p) : return i -len(p) #검색 성공
    else: return -1                   #검색 실패


p = "is"
t = "this is a book!"
print(BruteForce(p, t))