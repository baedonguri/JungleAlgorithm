from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]
team, enemy = 0,0

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(row,col, start):
    que = deque()
    que.append([row,col])
    cnt = 0
    while que:
        x,y = que.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                if start == graph[nx][ny]:
                    graph[nx][ny] = 0
                    cnt += 1
                    que.append([nx,ny])
    return (cnt ** 2 if cnt else 1)

    
for i in range(n):        
    for j in range(m):
        if graph[i][j]:
            if graph[i][j] == 'W':
                team += bfs(i,j, graph[i][j])
            else:
                enemy += bfs(i,j, graph[i][j])

print(team, enemy)