import sys
import heapq
input = sys.stdin.readline

n = int(input())

commend = []
for _ in range(n):
  commend.append(int(input()))

que = []
result = []
for i in commend:
  if i == 0:
    if que:
      result.append(heapq.heappop(que))
    else:
      result.append((0,0))
  else:
    heapq.heappush(que,(abs(i), i))

for i in result:
  print(i[1])