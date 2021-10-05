import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
  graph.append( list(map(int, input() )) )

def bfs():
  que = deque()
  que.append((0,0,0))
  visited[0][0][0] = 1
  is_break = 0

  while que:
    x, y, z = que.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
            visited[nx][ny][z] = visited[x][y][z] + 1
            que.append((nx,ny, z))
        elif z == 0 and graph[nx][ny] == 1 and visited[nx][ny][1] == 0:
          visited[nx][ny][1] = visited[x][y][z] + 1
          que.append((nx,ny,1))
          is_break = 1
      
  if visited[n-1][m-1][0] == 0 and visited[n-1][m-1][1] == 0:
    print(-1)
  else:
    print(visited[n-1][m-1][is_break])

bfs()