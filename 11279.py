import sys
import heapq
input = sys.stdin.readline

n = int(input())
x = []
que = []
for _ in range(n):
  x.append(int(input()))

for i in x:
  if i == 0:
    if not que:
      print(0)
    else:
      z=heapq.heappop(que)
      print(z[1])
  else:
    heapq.heappush(que,(-i,i))