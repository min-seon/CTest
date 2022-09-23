#문자열 재정렬

s=input()
arr=list(s)
arr1=[]
arr2=[]
for i in arr:
    if i.isalpha() : # 문자인지 묻기
        arr1.append(i)
    else:
        arr2.append(i)
arr1=sorted(arr1)
arr2=sorted(arr2)
arr2=''.join(arr2)

result=''
for i in arr1:
    result += i
for j in arr2:
    result += j
print(result)