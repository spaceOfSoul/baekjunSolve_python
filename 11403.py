import sys
from collections import deque

n = int(sys.stdin.readline())
grp = []

for _ in range(n):
  grp.append( list(map(int, sys.stdin.readline().split())) )

def bfs(v):
  visit = [False]*n
  que = deque()
  que.append(v)

  while que:
    x = que.popleft()
    for i in range(n):
      if grp[x][i] == 1 and not visit[i]:
        visit[i] = True
        grp[v][i] = 1
        que.append(i)

for i in range(n):
  bfs(i)

for i in range(n):
  for j in grp[i]:
    print(j, end = ' ')
  print()