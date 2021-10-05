import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
brokenButton = list(map(int, input().split()))
button = [0,1,2,3,4,5,6,7,8,9]
if brokenButton:
  for i in brokenButton:
    button.remove(i)

result = abs(100-n)

checking_1 = n
checking_2 = n
pas_1 = False
pas_2 = False
stop = False
stop_2 = False
while True and len(button) >= 1:
  if not stop:
    for j in str(checking_1):
      if int(j) in button:
        pas_1 = True
        continue
      else:
        checking_1 += 1
        pas_1 = False
        break
    if (checking_1 - n + len(str(checking_1)) >= result) or checking_1 > 1000000:
      stop = True

  if not stop_2:
    for j in str(checking_2):
      if int(j) in button:
        pas_2 = True
        continue
      else:
        checking_2 -= 1
        pas_2 = False
        break
    if (n-checking_2 + len(str(checking_2)) >= result) or checking_2 <0:
      stop_2 = True
  
  if pas_1:
    result = min(checking_1 - n + len(str(checking_1)), result)
  if pas_2:
    result = min(n - checking_2 + len(str(checking_2)), result)
  if stop and stop_2:
    break

print(result)