import sys

T = int(sys.stdin.readline())
d=[[1,0],[0,1],[1,1],[1,2],[2,3]]

result = []

for _ in range(T):
  n = int(sys.stdin.readline())

  if n >= len(d):
    for i in range(len(d),n+1):
      d.append([d[i-1][0] + d[i-2][0],d[i-1][1] + d[i-2][1]])
    
  result.append(d[n])

for i in range(T):
  print(result[i][0], end = ' ')
  print(result[i][1])