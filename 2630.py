import sys
input = sys.stdin.readline

n = int(input())

whiteCount = 0
blueCount = 0

paper = []
for _ in range(n):
  paper.append(list(map(int, input().split())))

def countColor( x,y,nn ):
  global whiteCount, blueCount
  state = paper[x][y]
  for i in range(x,nn+x):
    for j in range(y,nn+y):
      if paper[i][j] != state:
        countColor(x + nn//2,y,nn//2)
        countColor(x,y + nn//2,nn//2)
        countColor(x,y,nn//2)
        countColor(x+nn//2,y+nn//2,nn//2)
        return
  if state == 0:
    whiteCount +=1
  else:
    blueCount += 1

countColor(0,0,n)
print(whiteCount)
print(blueCount)  