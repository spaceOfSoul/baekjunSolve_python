n = int(input())
m = int(input())

s = input()
s+= ' '

count = 0
pLoop = 0
i = 1
while i < m:
  if s[i-1] == 'I'and s[i] == 'O'and s[i+1] == 'I':
        pLoop +=1
        i += 2
  else:
    if pLoop -n+1 > 0:
      count += pLoop-n+1
    pLoop =0
    i+=1

print(count)