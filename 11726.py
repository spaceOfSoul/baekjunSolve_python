import sys

n = int(sys.stdin.readline())
d = [0,1,1,2,3,5]

for i in range(6, n+2):
  d.append((d[i-1] + d[i-2]) % 10007)

print(d[n+1])