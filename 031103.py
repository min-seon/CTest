#문자열 뒤집기

s=input()
arr=list(s)

toone=0
tozero=0
for i in range(len(arr)):
    if arr[i] =='1': #모두 1로 바꾸는 경우
        if arr[i-1] == arr[i]:
            continue
        else: toone+=1
    if arr[i] =='0':
        if arr[i-1] == arr[i]:
            continue
        else: tozero+=1

print(min(toone,tozero))



