n = int(input())

board = []
for _ in range(n):
  board.append( list(map(str, input()) ))

count = []

def column(arr,i):
  return [row[i] for row in arr]

def countCandy():
  maxNum = 0
#row check
  for i in board:
    cc = 0
    cach = ''
    fullCandy = False
    for j in i:
      if cach == '':
        cach = j
        cc =1
      else:
        if j == cach:
          cc += 1
        else:
          cach = j
          if cc > maxNum:
            maxNum = cc
          cc = 1
      if cc == n:
        fullCandy = True
        break
    if cc > maxNum:
            maxNum = cc
    if fullCandy:
      break

#col check
  for i in range(n):
    cc= 0
    cach = ''
    fullCandy = False
    for j in column(board,i):
      if cach == '':
        cach = j
        cc =1
      else:
        if j == cach:
          cc += 1
        else:
          cach = j
          if cc > maxNum:
            maxNum = cc
          cc = 1
      if cc == n:
        fullCandy = True
        break
    if cc > maxNum:
            maxNum = cc
    if fullCandy:
      break
  return maxNum

def couCandy_row(a):
  maximum = 0
  cc = 0
  cach = ''
  for i in column(board,a):
    if cach == '':
      cach = i
      cc = 1
    else:
      if i == cach:
        cc+=1
      else:
        cach = i
        if cc > maximum:
          maximum = cc
        cc = 1
  if cc > maximum:
    maximum = cc
  return maximum

def couCandy_col(a):
  maximum = 0
  cc = 0
  cach = ''
  for i in board[a]:
    if cach == '':
      cach = i
      cc = 1
    else:
      if i == cach:
        cc+=1
      else:
        cach = i
        if cc > maximum:
          maximum = cc
        cc = 1
  if cc > maximum:
    maximum = cc
  return maximum

dx = [1,-1,0,0]
dy = [0,0,1,-1]
pas = countCandy()
count.append(pas)

if pas != n:
  for i in range(n):
    for j in range(n):
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx <n and 0 <= ny < n:
          board[i][j],board[nx][ny] = board[nx][ny], board[i][j]
          for l in (i,j):
            count.append(couCandy_row(l))
            count.append(couCandy_col(l))
          board[i][j],board[nx][ny] = board[nx][ny], board[i][j]

print(max(count))