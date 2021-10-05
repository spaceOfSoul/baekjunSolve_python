import sys

x, b = map(int, sys.stdin.readline().split())
r=[]
result = 0
while x>0:
  if x >= b:
    r.append(x % b)
    x = x//b
  else:
    r.append(x)
    break

jari = 0

for i in range(len(r)):
  result += r[i] * (b ** i)

print(result)