import sys
from collections import deque
input = sys.stdin.readline

result = []
t = int(input())
for _ in range(t):
  p = input().rstrip()
  n=int(input())

  que = deque(input().rstrip()[1:-1].split(","))
  if n==0:
    que = []
  reverse = 1;
  err = False
  
  for i in p:
    if i == 'R':
      reverse *= -1
    else:
      if que:
        if reverse == 1:
          que.popleft()
        else:
          que.pop()
      else:
        err = True
        break

  if not err:
    if reverse == 1:
      result.append("["+",".join(que)+"]")
    else:
      que.reverse()
      result.append("["+",".join(que)+"]")
  else:
    result.append("error")

for i in result:
  print(i)