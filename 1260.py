from collections import deque

n,m,v = map(int, input().split())

graph = [[0] * (n+1)for _ in range(n+1)]
_visited = [False] * (n+1)

for i in range(m):
  m1,m2 = map(int, input().split())
  graph[m1][m2] = graph[m2][m1] =1

result = []
def dfs(v):
  _visited[v] = True
  result.append(v)
  for i in range(n+1):
    if not _visited[i] and graph[v][i] == 1:
      dfs(i)
  return result

def bfs(v):
  result = []
  queue = deque()
  queue.append(v)
  _visited[v] = True

  while queue:
    v = queue.popleft()
    result.append(v)

    for i in range(n+1):
      if not _visited[i] and graph[v][i] == 1:
        queue.append(i)
        _visited[i] = True
  return result

print(" ".join(map(str,dfs(v))))
_visited = [False] * (n+1)
print(" ".join(map(str,bfs(v))))