import sys
import math

t = int(sys.stdin.readline())
result=[]

for _ in range(t):
  x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())

  if x1 == x2 and y1== y2 and r1 == r2:
    result.append(-1)
    continue

  distance = math.sqrt((max(x1,x2) - min(x1,x2))**2 + ( max(y1,y2) - min(y1,y2) )**2)

  if distance == (r1+r2) or max(r1,r2) == (min(r1,r2)+distance):
    result.append(1)
  elif distance > (r1+r2) or max(r1,r2)> (min(r1,r2)+distance):
    result.append(0)
  else:
    result.append(2)

for i in result:
  print(i)