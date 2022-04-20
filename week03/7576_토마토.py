import sys
from collections import deque

n, m = map(int, input().rstrip().split())

tomatos = [list(map(int, input().rstrip().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque([])
for i in range(m):
    for j in range(n):
        if tomatos[i][j] == 1:
            que.append([i,j])

def bfs():
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < m and 0 <= ny < n):
                continue

            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                que.append([nx,ny])
            
bfs()

days = 0

flag = True
for tomato in tomatos:
    for i in tomato:
        if i == 0:
            flag = False
            break
    days = max(days, max(tomato))

print(days-1 if flag else -1)