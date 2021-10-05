import sys
input = sys.stdin.readline

n, m, x, y, k = map(int,input().split())

gameMap = []
for _ in range(n):
  gameMap.append( list(map(int, input().split())) )

commend = list(map(int, input().split()))

dice = [[0,0,0] for _ in range(4)]
dicePos = [1,1]

dm = [1,-1,0,0]
dn = [0,0,1,-1]


result = []
for i in commend:
  ny = y + dn[i-1]
  nx = x + dm[i-1]

  if nx < 0 or ny < 0 or nx >= m or ny >= n:
    continue
  
  y,x = ny,nx
  
  dicePos[0] += dn[i-1]
  if dicePos[0] == 4:
    dicePos[0] = 0
  dicePos[1] += dm[i-1]
  if dicePos[1] == 3:
    dicePos[1] = 0

  if gameMap[y][x] == 0:
    gameMap[y][x] = dice[dicePos[0]][dicePos[1]]
  else:
    dice[dicePos[0]][dicePos[1]] = gameMap[y][x]
    gameMap[y][x] = 0

  if i == 1 or i == 2:
    dnx = dicePos[1]
    for _ in range(2):
      dnx +=1
      if dnx == 3:
        dnx = 0
    result.append(dice[dicePos[0]][dnx])
  else:
    dny = dicePos[0]
    for _ in range(2):
      dny += 1
      if dny == 4:
        dny = 0
    result.append(dice[dny][dicePos[1]])

for i in result:
  print(i)