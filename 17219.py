import sys
input = sys.stdin.readline

n, m = map(int, input().split())
passDict = {}
for _ in range(n):
  a,b = map(str, input().split())
  b.rstrip()
  passDict[a] = b

result = []
for _ in range(m):
  want = input().rstrip()
  result.append(passDict[want])

for i in result:
  print(i)