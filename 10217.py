import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

t = int(input())

def djs(grp,n):
  costs = [inf] * n
  times = [inf] * n
  que = []
  costs[0] = 0
  times[0] = 0
  heapq.heappush(que,(0,0,0))

  while que:
    time_,cost, now = heapq.heappop(que)
    if times[now] < time_:
      continue
    
    for i in grp[now]:
      nxtcost = i[1] + cost
      nxttime = i[2] + time_

      if nxttime < times[i[0]]:
        if nxtcost < costs[i[0]]:
          times[i[0]] = nxtcost

for _ in range(t):
  n, m, k = map(int, input().split())
  graph = [[] for _ in range(n)]
  for _ in range(k):
    u,v,c,d = map(int, input().split())
    graph[u-1].append(list(v,c,d))