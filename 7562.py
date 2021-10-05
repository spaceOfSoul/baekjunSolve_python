from collections import deque
import sys

testCase = int(sys.stdin.readline())
dr = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
result = []

def bfs(I, i, p, g):
  if p == g:
    return 0
  que = deque()
  que.append(p)

  while que:
    x,y = que.popleft()
    for k in range(8):
      nx = x + dr[k][0]
      ny = y + dr[k][1]

      if 0<=nx<I and 0<=ny<I and i[nx][ny] == 0:
        i[nx][ny] = i[x][y] + 1
        if i[nx][ny] == i[g[0]][g[1]]:
          return i[g[0]][g[1]]
        que.append((nx,ny))


for _ in range(testCase):
  I = int(sys.stdin.readline())
  i = [[0] * I for _ in range(I)]

  presentPos = list(map(int, sys.stdin.readline().split()))
  goalPos = list(map(int, sys.stdin.readline().split()))

  result.append(bfs(I, i, presentPos,goalPos))

for w in result:
  print(w)