import sys
from collections import deque

n, k = map( int, sys.stdin.readline().split())

step = [0] * 100001

def bfs():
  que = deque()
  que.append(n)

  while que:
    pos = que.popleft()
    if pos == k:
      break
    
    for nxt in (pos + 1, pos - 1, pos * 2):
      if 0 <= nxt <= 100000 and step[nxt] == 0:
        step[nxt] = step[pos] + 1
        que.append(nxt)

bfs()
print(step[k])