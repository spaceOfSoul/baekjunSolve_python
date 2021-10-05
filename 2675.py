t = int(input())

result = [''] * t
for j in range(t):
  r, s = map(str, input().split())

  for i in s:
    for _ in range(int(r)):
      result[j] += i

for i in result:
  print(i)