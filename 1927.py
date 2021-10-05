import heapq
import sys
input = sys.stdin.readline

n= int(input())

commend = []
for _ in range(n):
  commend.append(int(input()))

que = []
for i in commend:
  if i == 0:
    if que:
       print(heapq.heappop(que))
    else:
      print(0)
  else:
    heapq.heappush(que, i)