#이진탐색

n, target =list(map(int,input().split(' ')))
arr=list(map(int, input().split(' ')))

def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)

result=binary_search(arr,target,0,n-1)
if result ==None:
    print("no answer")
else:
    print(result+1)
