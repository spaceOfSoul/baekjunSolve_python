import sys
import heapq
from collections import deque
input = sys.stdin.readline

t = int(input())
result = []

def printable(imp, pages, m):
  b,c = pages.popleft()
  if -imp[0] == b:
    heapq.heappop(imp)
    if c == m:
      return 0
    return 1
  else:
    pages.append((b,c))
    return 2

for _ in range(t):
  que = []
  rq = deque()
  n, m = map(int, input().split())

  arr = list(map(int, input().split()))
  for i in range(n):
    heapq.heappush(que, -arr[i])
    rq.append((arr[i],i))

  count = 1
  while True:
    c=printable(que,rq,m)
    if c ==0:
      result.append(count)
      break
    elif c == 1:
      count += 1
    else:
      continue

for i in result:
  print(i)