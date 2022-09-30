n, x = map(int,input().split())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    if x==i:
        sum+=1
if sum==0:
    print(-1)
else:
    print(sum)