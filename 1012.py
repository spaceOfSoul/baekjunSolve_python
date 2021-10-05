import sys
sys.setrecursionlimit(10**6)

T = int(input())
jirung = []
def dfs(x,y):
  if x <= -1 or x >= m or y <= -1 or y >= n:
    return False
  
  if arr[x][y] == 1:
    arr[x][y] = 0
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

    return True
for q in range(T):
  count = 0
  m,n,k = map(int, input().split())

  arr = [[0] * n for _ in range(m)]

  for _ in range(k):
    m1, m2 = map(int, input().split())
    arr[m1][m2] = 1

  for i in range(n):
    for j in range(m):
      if dfs(j,i):
        count += 1
  jirung.append(count)

for i in range(len(jirung)):
  print(jirung[i])