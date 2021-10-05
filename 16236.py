import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

sea = []
for _ in range(n):
  sea.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]
sharkSize = 2

startPos = []
for i in range(n):
  br = False
  for j in range(n):
    if sea[i][j] == 9:
      startPos.append(i)
      startPos.append(j)
      br = True
      break
  if br:
    break

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(srt):
  q,w = srt[0],srt[1]
  sea[q][w] = 0
  que = deque()
  que.append((q,w))
  
  while que:
    x,y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<= nx < n and 0 <= ny < n and sea[nx][ny] <= sharkSize and visited[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        que.append((nx,ny))

result = 0
eatCount = 0
while True:
  bfs(startPos)

  min_dist = int(1e9)
  for i in range(n):
    for j in range(n):
      if 0< sea[i][j] < sharkSize and visited[i][j] != 0:
        if visited[i][j] < min_dist:
          min_dist = visited[i][j]
          startPos[0] = i
          startPos[1] = j
  
  if min_dist == int(1e9):
    break
  
  result += min_dist
  eatCount += 1
  if eatCount == sharkSize:
    sharkSize += 1
    eatCount = 0
  visited = [[0] * n for _ in range(n)]

print(result)