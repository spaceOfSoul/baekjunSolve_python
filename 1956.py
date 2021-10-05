import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

graph = [[INF] * v for _ in range(v)]
for _ in range(e):
  a,b,c = map(int, input().split())
  graph[a-1][b-1] = c

for i in range(v):
  for j in range(v):
    for k in range(v):
      graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

cycles = []
for i in range(v):
  if graph[i][i] != INF:
    cycles.append(graph[i][i])

if not cycles:
  print(-1)
else:
  print(min(cycles))