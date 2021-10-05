import sys

input = sys.stdin.readline

t = int(input())
d = [1, 2, 4]
result = []

for _ in range(t):
  n = int(input())
  for i in range(len(d),n):
    d.append(d[i-1]+d[i-2]+d[i-3])
  result.append(d[n-1])

for i in result:
  print(i)