from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
graph = [list(input().rstrip()) for i in range(n)]
team, enemy = 0,0

que = deque([[0,0]])
start = graph[0][0]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while que:
    x,y = que.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[x][y] == graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                que.append([nx,ny])
                

    
for i in graph:
    print(i)