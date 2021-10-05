import sys
import heapq

input = sys.stdin.readline

v,e = map(int, input().split())
k = int(input())
distance = [int(1e9)] * v

graph = [[]for _ in range(v)]
for _ in range(e):
  u,ver, w = map(int, input().split())
  graph[u-1].append((ver-1,w))

def djs(s):
  que = []
  heapq.heappush(que,(0,s))
  distance[s] = 0

  while que:
    dist, now = heapq.heappop(que)
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(que, (cost, i[0]))

djs(k-1)

for i in distance:
  if i == int(1e9):
    print('INF')
  else:
    print(i)