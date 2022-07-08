from sys import stdin
from collections import deque
input = stdin.readline

n,m = map(int, input().split())
r,c, d = map(int, input().split())
maze = [list(map(int, input().split())) for i in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def change(d):
    if d == 0: # 북 -> 서
        return 3
    elif d == 1: # 동 -> 북
        return 0 
    elif d == 2: # 남 -> 동
        return 1
    elif d == 3: #서 -> 동
        return 2

def back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


def bfs(r,c,d):
    cnt = 1
    maze[r][c] = 2
    que = deque([[r,c,d]])
    while que:
        x,y,dir = que.popleft()
        for i in range(4):
            dir = change(dir)
            nx = x + dy[dir]
            ny = y + dx[dir]
            if 0 <= nx < n and 0 <= ny < m and not maze[nx][ny]:                    
                cnt += 1
                maze[nx][ny] = 2
                que.append([nx,ny,dir])
                break
            elif i == 3:
                nx = x + dy[back(dir)]
                ny = y + dx[back(dir)]
                que.append([nx,nx,dir])

                if maze[nx][ny] == 1:
                    return cnt



print(bfs(r,c,d))