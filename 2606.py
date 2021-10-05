count = int(input())
network = int(input())

coms = [[0] * count for _ in range(count)]
visit = [False] * count
infection = 0
for _ in range(network):
  m1, m2 = map(int, input().split())
  coms[m1-1][m2-1] = coms[m2-1][m1-1] = 1

def dfs(v):
  visit[v] = True

  for i in range(count):
    if not visit[i] and coms[v][i] == 1:
      dfs(i)

dfs(0)

for i in range(len(visit)):
  if visit[i] == True:
    infection += 1
print(infection -1)