import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = []
plusVal = [[0] * (m+1) for _ in range(n+1)]
for _ in range(n):
  arr.append(list(map(int, input().split())))

for i in range(1,n+1):
  for j in range(1,m+1):
    plusVal[i][j] = arr[i-1][j-1] + plusVal[i-1][j] + plusVal[i][j-1] - plusVal[i-1][j-1]

k = int(input())
result = []
for _ in range(k):
  i,j,x,y = map(int, input().split())
  result.append( plusVal[x][y] - plusVal[i-1][y] - plusVal[x][j-1] + plusVal[i-1][j-1])

for i in result:
  print(i)