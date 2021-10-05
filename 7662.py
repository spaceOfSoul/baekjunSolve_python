import heapq
import sys

que=[]
t  = int(sys.stdin.readline())

for _ in range(t):
  k = int(sys.stdin.readline())
  
  commend = []
  for _ in range(k):
    commend.append(list(sys.stdin.readline().rstrip().split()))
  
  for i in commend:
    if i[0] == 'I':
      heapq.heappush( int(i[1]))