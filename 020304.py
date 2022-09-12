n,k = map(int, input().split(' '))

count=0
while n>=2:
    if n%k==0:
        n = int(n / k)
        count += 1
    else:
        n=n-1
        count += 1

print(count)