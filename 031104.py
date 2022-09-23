n=int(input())
arr = map(int, input().split(' '))
arr=sorted(arr)

target=1
for x in arr:
    if target < x:
        break
    target +=x
print(target)
