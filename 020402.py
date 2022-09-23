n=input()
arr=list(n)
nowx=ord(arr[0])-96
nowy=int(arr[1])
print(nowx,nowy)
steps=[(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2),(-2,1),(-2,-1)]
result=0
for i in steps:
    nowx +=i[0]
    nowy +=i[1]
    if nowx>=9 or nowy>=9 or nowy<=0 or nowx<=0:
        nowx -= i[0]
        nowy -= i[1]
        continue
    else:
        result += 1
        nowx -= i[0]
        nowy -= i[1]

print(result)