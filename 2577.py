abc=[]

for _ in range(3):
  abc.append(int(input()))

gop = 1
for i in abc:
  gop *= i

result = [0] * 10
for i in str(gop):
  result[int(i)] += 1

for i in result:
  print(i)