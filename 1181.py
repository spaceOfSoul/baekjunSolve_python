import sys
input = sys.stdin.readline

dictionary = {}
n = int(input())
for _ in range(n):
  s = input().rstrip()
  dictionary[s] = len(s)

result = list(sorted(dictionary.items(),key = lambda item: (item[1],item[0])))

for i in result:
  print(i[0])