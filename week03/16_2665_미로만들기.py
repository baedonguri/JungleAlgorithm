from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9) 

n = int(input().rstrip())

# 상하좌우
dx = [-1,1,0,0] 
dy = [0,0, -1,1]

maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

def bfs():
    visited[0][0] = 0
    que = deque([(0,0)])

    while que:
        x,y = que.popleft()
        if x == n-1 and y == n-1:
            print(visited[x][y])
            return 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue
                
            if visited[nx][ny] == -1:
                if maze[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]
                    que.appendleft([nx,ny])
                elif maze[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx,ny])

bfs()

            
                
