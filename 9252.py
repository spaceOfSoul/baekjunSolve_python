import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

a_size = len(a)
b_size = len(b)

dp = [[0] * (b_size + 1) for _ in range(a_size + 1)]

for i in range(a_size):
    for j in range(b_size):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[a_size][b_size])
result = ''

i = a_size
j = b_size

while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        result += b[j - 1]
        i -= 1
        j -= 1

print(result[::-1])
