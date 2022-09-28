#미로탈출
from collections import deque
n,m = map(int, input().split())
graph=[list(map(int,input())) for _ in range(m)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dbfs(x,y):
    #graph[x][y]=0
    queue=deque()
    queue.append((x,y))
    #sum = 0
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= n or nx < 0 or ny <0 or ny>=m :
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny]==1:
                #x=nx
                #y=ny
                graph[nx][ny]=graph[x][y]+1
                #sum+=1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(dbfs(0,0))
