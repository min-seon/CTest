#모험가길드
n=int(input())
arr=map(int,input().split(' '))

# 답지엔 최댓값
sum=0
result=0
for i in arr:
    sum+=i
    if sum >= n:
        result +=1
        sum=0

print(result)
