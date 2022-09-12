n=int(input())
arr=list(input().split(' '))
x=1
y=1

for i in arr:
    if i == 'R':
        x+=1
        if x>n or x<=0:
            x-=1
    elif i =='L':
        x-=1
        if x>n or x<=0:
            x+=1
    elif i =='U':
        y+=1
        if y>n or y<=0:
            y-=1
    else:
        y-=1
        if y>n or y<=0:
            y+=1

print(y,x)
