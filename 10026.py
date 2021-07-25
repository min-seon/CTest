import sys
sys.setrecursionlimit(100000)
#줄 길이 입력
n= int(input())
# 2 차원 리스트로 입력받기
graph=[list(input()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

#이동할 네 방향 정의(상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
see=0
nosee=0

def dfs(x,y):
    color=graph[x][y]
#1)적록색약이 아닌경우
    #색깔이 같고 방문한적이 없을 때
    # 현재 노드를 방문 처리
    visited[x][y] = True
    #현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<n and -1<ny<n:  #현재 노드와 연결된 색깔이 같은 노드 재귀적으로 방문
            if graph[nx][ny]==color and visited[nx][ny]==False:
                dfs(nx,ny)

#방문처리를 하고 dfs호출한다
for i in range(n):
    for j in range(n):
        if visited[i][j] ==False:
            dfs(i, j)
            see +=1

#2)적록색약인 경우 R을 G로 바꾸기
for i in range(n):
     for j in range(n):
         if graph[i][j] =='R':
                graph[i][j]='G'

#초기화
visited=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            nosee+= 1

print(see,nosee)