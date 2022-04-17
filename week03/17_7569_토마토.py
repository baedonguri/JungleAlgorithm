import sys
from collections import deque

m, n, h= map(int, input().rstrip().split())

tomatos = [[list(map(int, input().rstrip().split())) for i in range(n)]for depth in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


que = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 1:
                que.append([i,j,k])


while que:
    z,y,x = que.popleft()

    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if not (0 <= nz < h and 0 <= ny < n and 0 <= nx < m):
            continue

        if tomatos[nz][ny][nx] == 0:
            tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
            que.append([nz,ny,nx])

days = 0
flag = True

for i in tomatos:
    for j in i:
        for k in j:
            if k == 0:
                flag = False
                break
        days = max(days, max(j))

print(days-1 if flag else -1)