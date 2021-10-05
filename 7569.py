import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().split())

arr = []

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

que = deque()

for i in range(h):
  arr.append([list(map(int, sys.stdin.readline().split())) for _ in range(n)])
  for j in range(n):
    for k in range(m):
      if arr[i][j][k] == 1:
        que.append((i,j,k))

def bfs():
  while que:
    z, y, x = que.popleft()

    for i in range(6):
      nz = z + dz[i]
      ny = y + dy[i]
      nx = x + dx[i]

      if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and arr[nz][ny][nx] == 0:
        arr[nz][ny][nx] = arr[z][y][x] + 1
        que.append((nz,ny,nx))
  
  result = -2

  for i in arr:
    for j in i:
      for k in j:
        if k == 0:
          return -1
        result = max(result, k)
  if result == -1:
    return -1
  else:
    return result -1

print(bfs())