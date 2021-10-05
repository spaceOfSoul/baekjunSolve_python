import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dw = [1,-1,0,0]
dh = [0,0,1,-1]

result = []

def dfs(y,x):
  if graph[y][x] == 0 or graph[y][x] == 2:
    return False

  graph[y][x] = 2
  for i in range(4):
    for j in range(4):
      ny = y + dh[i]
      nx = x + dw[j]

      if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
        dfs(ny,nx)
  
  return True

while True:
  w, h = map(int, input().split())

  if w==0 and h==0:
    break

  graph = []
  for _ in range(h):
    graph.append(list(map( int, input().split() )))

  c = 0
  for i in range(w):
    for j in range(h):
      if dfs(j,i):
        c += 1

  result.append(c)

for i in result:
  print(i)