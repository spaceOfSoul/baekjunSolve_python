n = input()

c1 = 0
c2 = 0
for i in range(len(n)//2):
  c1 += int(n[i])

for i in range(len(n)//2,len(n)):
  c2 += int(n[i])

if c1 == c2:
  print('LUCKY')
else:
  print('READY')