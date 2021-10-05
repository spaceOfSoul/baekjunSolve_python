import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def canGo(graph, v, w):
  que = deque()
  que.append(v)
  can = False
  while que:
    nxt = que.popleft()
    for i in graph[nxt]:
      if i == w:
        can = True
        break
      que.append(i)
    if can:
      break

result = []
for _ in range(t):
  n ,k = map(int, input().split())
  d = list(map(int, input().split()))
  techTree = [[] for _ in range(k)]

  for _ in range(k):
    x,y = map(int,input().split())
    techTree[x-1].append(y-1)

  w=int(input())
  start = 0
  for i in range(n):
    if canGo(techTree, i, w-1):
      start = i
      break