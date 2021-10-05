countHome = int(input())
arr = []
houseScale = 0
for i in range(countHome):
  arr.append(list(map(int, input())))

def dfs(x, y):
  global houseScale
  if x <= -1 or x >= countHome or y <= -1 or y >= countHome:
    return False
  
  if arr[x][y] == 1:
    arr[x][y] = 0
    houseScale +=1

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

    return houseScale
  return False

HouseInfo = []

for i in range(countHome):
  for j in range(countHome):
    if dfs(i,j):
      HouseInfo.append(houseScale)
      houseScale = 0

print(len(HouseInfo))
HouseInfo.sort()
for i in range(len(HouseInfo)):
  print(HouseInfo[i])