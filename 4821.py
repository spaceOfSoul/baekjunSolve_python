result = []

while True:
  n = int(input())
  pageList = []

  if n == 0:
   break

  pages = input()
  ran = pages.split(',')
  
  for i in ran:
    if i.isdecimal():
      if int(i) <= n:
        pageList.append(int(i))
      continue
      
    a, b = map(int, i.split('-'))
    if a> b:
        continue
    for i in range(a,b+1):
      if i <= n:
        pageList.append(i)

  result.append(len(set(pageList)))

for i in result:
  print(i)