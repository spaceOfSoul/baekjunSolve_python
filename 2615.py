import sys

pan = []
for _ in range(19):
  pan.append(list(map(int, sys.stdin.split())))

direction = [(1,0),(-1,0),]
p=[]
for i in range(19):
  for j in range(19):
    if pan[i][j] != 0:
      p.append(pan[i][j])
      for 