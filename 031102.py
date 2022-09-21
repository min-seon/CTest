#곱하기 혹은 더하ㅣㄱ

s=input()
arr=list(s)
arr=list(map(int,arr))

result=arr[0]
for i in range(1,len(arr)):
    if result==0:
        result += arr[i]

    elif arr[i] == 0:
        result += arr[i]
    else:
        result *= arr[i]

print(result)


