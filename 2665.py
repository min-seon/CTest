from collections import deque

n = int(input())
group = [list(map(int, input())) for i in range(n)]
visited = [[-1] * n for i in range(n)]
#이동할 네 방향 정의(상,하,좌,우)
dx = [-1, 1,0, 0]
dy = [0, 0, -1, 1]


def bfs():
    de = deque()
    de.append([0, 0])
    visited[0][0] = 0
    # 큐가 빌 때 까지 반복
    while de:
        x, y = de.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 노드를 처음 방문하는 경우에만 최단거리 등록
            if 0 <= nx < n and 0 <= ny < n: #공간을 벗어날 경우 무시
                if visited[nx][ny] == -1:
                    if group[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        de.append([nx, ny])
                    else:
                        visited[nx][ny] = visited[x][y]
                        de.appendleft([nx, ny])


bfs()
print(visited[n - 1][n - 1])
#결국 최단거리 구하는 문제