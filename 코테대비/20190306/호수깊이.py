N = int(input())
hosu = [list(map(int, input().split())) for _ in range(N)]

for h in range(N):#높이 0부터 시작
    flag=0
    cnt = 0
    for i in range(1,N-1):
        for j in range(1,N-1):
          if hosu[i][j]>h:#높이보다 크면
              flag = 1
              cnt += 1
              if hosu[i-1][j]>h and hosu[i+1][j]>h and hosu[i][j-1]>h and hosu[i][j+1]>h:
                  hosu[i][j]+=1

    if flag ==0: break
print(hosu)
# sum_list = []
# for i in range(N):
#     sum_list.append(sum(hosu[i]))
#
# print(sum(sum_list))
