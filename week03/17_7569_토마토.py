import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int, input().split())

tomatos = [[list(map(int,input().rstrip().split())) for j in range(n)]for i in range(h)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

que = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 1:
                que.append([i,j,k])

def bfs():
    while que:
        z,y,x = que.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if not (0 <= nx < m and 0 <= ny < n and 0 <= nz < h):
                continue
            
            if not tomatos[nz][ny][nx]:
                tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
                que.append([nz,ny,nx])
bfs()
flag = True
days = 0
for tomato in tomatos:
    for i in tomato:
        for j in i:
            if j == 0:
                flag = False
                break
        days = max(days, max(i))
print(days-1 if flag else -1)