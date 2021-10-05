import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
arr = []
que = deque()
for i in range(n):
  arr.append(list( map(int, sys.stdin.readline().split())))
  for j in range(m):
    if arr[i][j] == 1:
      que.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
  while que:
    x, y = que.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
          arr [nx][ny] = arr[x][y] + 1
          que.append((nx, ny))
  
  why = False
  result = -2
  for i in arr:
    for j in i:
      if j == 0:
        why = True
      result = max(result, j)

  if why == True:
    return -1
  elif result == -1:
    return 0
  else:
    return result - 1
  
print(bfs())