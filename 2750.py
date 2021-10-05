n = int(input())
a=[]

for _ in range(n):
  a.append(int(input()))

for i in range(n):
  min_index = i
  for j in range(i + 1, n):
    if a[min_index] > a[j]:
      min_index = j
  a[i],a[min_index] = a[min_index], a[i]

for i in range(n):
  print(a[i])