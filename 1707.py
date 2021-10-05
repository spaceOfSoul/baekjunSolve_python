import sys
from collections import deque

sys.setrecursionlimit(10**6)

k = int(sys.stdin.readline())
result = []

def bfs(grp, size, color, start):
  que = deque()
  que.append(start)
  color[start] = 1
  while que:
    nxt = que.popleft()
    for i in grp[nxt]:
      if color[i] == 0:
        que.append(i)
        color[i] = color[nxt] * -1
      elif color[i] == color[nxt]:
        return False
  return True

for _ in range(k):
  v, e = map(int, sys.stdin.readline().split())

  graph = [[] for _ in range(v)]
  color = [0] * v
  
  for _ in range(e):
    x1, x2 = map(int, sys.stdin.readline().split())
    graph[x1-1].append(x2-1)
    graph[x2-1].append(x1-1)

  r = True
  for i in range(v):
    if color[i] == 0:
      if not bfs(graph,v,color, i):
        r = False
        break
  result.append(r)

for i in result:
  if i:
    print("YES")
  else:
    print("NO")