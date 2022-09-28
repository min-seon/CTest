n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

arr1.sort()

for i in arr2:
        if i in arr1:
            print("yes", end =' ')
        else:
            print("no", end = ' ')
