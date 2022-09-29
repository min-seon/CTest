#국영수
n=int(input())
arr=[list(input().split()) for _ in range(n)]

#arr=sorted(arr, key=lambda x:x[1], reverse = True)

arr.sort( key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])  )


for i in range(n):
    print(arr[i][0])