
n,m = map(int, input().split(' '))
graph=[list(map(int, input())) for _ in range(m)]

def dbfs (x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m :
        return False

    if graph[x][y]==0:
        graph[x][y]=1
        dbfs(x-1,y)
        dbfs(x+1,y)
        dbfs(x,y-1)
        dbfs(x,y+1)
        return True

    return False
result =0
for i in range(n):
    for j in range(m):
        if dbfs(i,j)==True:
            result+=1
print(result)
