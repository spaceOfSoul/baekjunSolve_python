from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

stack = deque()
ptr = 0

result = []
for _ in range(n):
  commend = input().rstrip().split()
  if commend[0] == 'push':
    stack.append(int(commend[1]))
    ptr+=1
  elif commend[0] == 'pop':
    if ptr == 0:
      result.append(-1)
    else:
      result.append(stack.pop())
      ptr -= 1
  elif commend[0] == 'size':
    result.append(ptr)
  elif commend[0] == 'empty':
    if ptr == 0:
      result.append(1)
    else:
      result.append(0)
  else:#top
    if ptr > 0:
      result.append(stack[ptr-1])
    else:
      result.append(-1)

for i in result:
  print(i)