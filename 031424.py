#안테나
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

sum=0
for i in arr:
    for j in arr:
        if i >= j :
            sum += (i-j)
        else:
            sum += (j-i)

    if i is arr[0]:
        minimum=sum
        sum=0
        miniI=i

    else:
        if minimum > sum:
            miniI=i

        minimum=min(sum,minimum)
        sum=0

print(miniI)

#arr.sort()
#print(arr[(n-1)//2])
#무조건 중간이 정답이라 위가 정답