import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
cycle = False

graph = []
for _ in range(n):
  graph.append(input())

visited = [[False] * m for _ in range(n)]
cach = [[0] * m for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
  global cycle

  if visited[x][y]:
    cycle = True
    return -1
  
  if cach[x][y] != 0:
    return cach[x][y]
  
  for i in range(4):
    _grp = int(graph[x][y])
    nx = x + dx[i] * _grp
    ny = y + dy[i] * _grp

    if 0<=nx<n and 0<= ny < m and graph[nx][ny] != 'H':
      visited[x][y] = True
      cach[x][y] = max(cach[x][y],dfs(nx,ny) + 1)
      if cycle:
        return -1
      visited[x][y] = False
  return cach[x][y]

dfs(0,0)

if cycle:
  print(-1)
else:
  print(max(max(cach)) + 1)