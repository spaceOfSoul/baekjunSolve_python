import sys

t = int(sys.stdin.readline())
p = [1,1,1,2,2,3,4,5,7,9]
result = []

for _ in range(t):
  n = int(sys.stdin.readline())
  
  start = len(p)
  for i in range(start,n):
    p.append( p[i-2] + p[i-3] )
  result.append(p[n-1])

for i in result:
  print(i)