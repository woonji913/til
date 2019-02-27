# str1 = '()()()(((())()'
# str2 = ')(()()())((('
string = str(input())

def plate(string):
    cnt = 10
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            cnt += 5
        else:
            cnt += 10
    return cnt

print(plate(string))
# print(plate(str1))
# print(plate(str2))