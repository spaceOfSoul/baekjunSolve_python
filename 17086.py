import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
maxNum = 0

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]
for _ in range(n):
    arr.append(list(map(int, input().split())))


def bfs(r, c):
    que = deque()
    visited = [[False] * m for _ in range(n)]
    que.append((r, c))
    visited[r][c] = True
    returnNum = 0

    while que:
        que_size = len(que)
        returnNum += 1
        for _ in range(que_size):
            x, y = que.popleft()

            if arr[x][y] == 1:
                return returnNum - 1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))
    return 0


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            maxNum = max(maxNum, bfs(i, j))

print(maxNum)
