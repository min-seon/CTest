#답 참고
n = int(input())
arr= list(input().split(' '))

dx = [0,0,-1,1] #LR
dy= [-1, 1,0,0] #UD
#추가
num=['L','R','U','D']

x=1
y=1

for i in arr:
    for j in range(len(num)):
        if i == num[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    if nx <1 or ny <1 or nx>n or ny>n:
        continue

    x=nx
    y=ny

print(x,y)




