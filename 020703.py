n,m=map(int, input().split())
arr=list(map(int,input().split()))

h=max(arr)
while h>=0:
    for i in arr:
        if h < i:
            sum+=(i-h)

    if sum ==m:
        print(h)
        break
    else:
        sum=0
        h -=1
        continue
