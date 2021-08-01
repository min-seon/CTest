n,k = map(int, input().split())
list=[False for _ in range(n+1)] #초기화

#제거하면 True
temp = 0
for i in range(2,n+2):
    for j in range(i, n+1 ,i): #lsit 에서 옮겨야 할 i 정해주기
        if list[j] == False:
            list[j]=True #j임
            temp+=1
            if temp==k:
                print(j)
                break
