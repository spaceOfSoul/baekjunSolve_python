import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
  coins.append(int(input()))

result = 0
for i in range(len(coins)-1,-1,-1):
  result += k//coins[i]
  k%=coins[i]

print(result)